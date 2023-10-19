from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauth.models import User


class UserRegistrationForm(UserCreationForm):


    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}), required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}), required=True)

    class Meta:
        model = User
        # Register sayfasında kullanıcıdan email, password1 ve password2 bilgilerini alıyoruz.
        fields = ['username', 'email']


    # template_name = 'base/register.html'
    # form_class = UserCreationForm
    # redirect_authenticated_user = True # Eğer kullanıcı giriş yapmışsa register sayfasına gitmesini engelliyoruz.
    # success_url = reverse_lazy('tasks')
    #
    # def form_valid(self, form):
    #     user = form.save() # formdan gelen bilgileri kaydediyoruz.
    #     if user is not None:
    #         login(self.request, user) # login fonksiyonu ile kullanıcıyı otomatik olarak giriş yapıyoruz.
    #     return super(RegisterPage, self).form_valid(form)
    #
    # def get(self, *args, **kwargs):
    #     if self.request.user.is_authenticated: # Eğer kullanıcı giriş yapmışsa register sayfasına gitmesini engelliyoruz.
    #         return redirect('tasks')
    #     return super(RegisterPage, self).get(*args, **kwargs)