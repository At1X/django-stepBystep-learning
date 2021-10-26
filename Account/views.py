from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib.auth import views
from .forms import CustomForms
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import (

                                    FormValid,
                                    ForbidAccess,
                                    DeleteAccess,
                                    MyShowObjectMixin,
                                    NormalUserForbidAcces,
                                    HasLoggined,
)
from django.views.generic import (
                                    ListView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView,
)

from food.models import foodModels
# from .models import User
@login_required()
def home(request):
    return render(request, 'registration/home.html')
# Create your views here.

class TheHome(LoginRequiredMixin, NormalUserForbidAcces, ListView):
    def get_queryset(self):
        if self.request.user.is_superuser:
            return foodModels.objects.all()
        else:
            return foodModels.objects.filter(user=self.request.user)
    template_name = 'registration/home.html'
class MyCreateView(LoginRequiredMixin,MyShowObjectMixin,FormValid, CreateView):
    model = foodModels
    template_name = 'registration/create-update.html'

class MyUpdateView(LoginRequiredMixin,MyShowObjectMixin,FormValid,ForbidAccess, UpdateView):
    model = foodModels
    template_name = 'registration/create-update.html'

class AuthorDeleteView(DeleteAccess, DeleteView):
    model = foodModels
    success_url = reverse_lazy('account:home')
    template_name = 'registration/deleteView.html'
class ProfileView(UpdateView):
    model = User
    template_name = 'registration/profile.html'
    form_class = CustomForms
    success_url = reverse_lazy('account:userProfile')
    def get_object(self, queryset=None):
        return User.objects.get(pk= self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(ProfileView, self).get_form_kwargs()
        kwargs.update(
            {
            'user': self.request.user
            }
        )
        return kwargs

#this class uses to access login view and inherit views.loginView to edit this built-in class
#uses to redirect users differently
#use reverse instead of reverse_lazy
class myOwnLogin(HasLoggined ,views.LoginView):
    def get_redirect_url(self):
        if self.request.user.is_superuser:
            return reverse('account:home')
        else:
            return reverse('account:userProfile')


from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})



def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')