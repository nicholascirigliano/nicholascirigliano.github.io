from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from playersblog.models import Profile


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'fb_url', 'instagram_url', 'tiktok_url', 'amazon_url', 'etsy_url')

        widgets = {

                'bio': forms.Textarea(attrs={'class': 'form-control'}),
                #'profile_pic': forms.TextInput(attrs={'class': 'form-control'}),
                'fb_url': forms.TextInput(attrs={'class': 'form-control'}),
                'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
                'tiktok_url': forms.TextInput(attrs={'class': 'form-control'}),
                'amazon_url': forms.TextInput(attrs={'class': 'form-control'}),
                'etsy_url': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs = {'Placeholder': 'Email', 'class': 'form-control'}))
    #first_name = forms.CharField(max_length=100, widget = forms.TextInput(attrs={'class': 'form-control'}))
    #last_name = forms.CharField(max_length=100, widget = forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields  = ('email', 'username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['Placeholder'] = 'Username'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['Placeholder'] = 'Password'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['Placeholder'] = 'Confirm Password'

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs = {'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget = forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget = forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget = forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(max_length=100, widget = forms.TextInput(attrs={'class': 'form-control'}))
    is_superuser = forms.CharField(max_length=100, widget = forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_staff = forms.CharField(max_length=100, widget = forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_active = forms.CharField(max_length=100, widget = forms.CheckboxInput(attrs={'class': 'form-check'}))
    date_joined = forms.CharField(max_length=100, widget = forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields  = ('first_name', 'last_name', 'email', 'username', 'date_joined', 'last_login', 'is_superuser', 'is_staff', 'is_active')


 
class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget = forms.PasswordInput(attrs = {'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=100, widget = forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=100, widget = forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields  = ('old_password', 'new_password1', 'new_password2')
