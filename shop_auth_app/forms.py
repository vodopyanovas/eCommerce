# # -*- coding: utf-8 -*-
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django import forms
from registration import validators
from registration.forms import RegistrationForm
from shop_auth_app.models import MyUser

__author__ = 'Anton Vodopyanov'


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    email = forms.EmailField(label='Email', max_length=150,)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'password1', 'password2')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def clean_email(self):
        email = self.cleaned_data['email']
        if not validate_email(email):
            raise ValidationError("Enter a valid e-mail address")

        if MyUser.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")

        return email

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        max_length=254,
        # widget=forms.TextInput(attrs={'autofocus': ''}),
    )
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput,
    )

    error_messages = {
        'invalid_login': (
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': ("This account is inactive."),
        'unknown_email': ("There are no such login.")
    }

    # def clean(self):
    #     username = self.cleaned_data.get('username')
    #
    #     if not MyUser.objects.filter(email=username).exists():
    #         raise forms.ValidationError("There are no such email", code='unknown_email')


class CustomRegistrationForm(RegistrationForm):
    class Meta:
        model = MyUser
        fields = (
            'email',
            'password1',
            'password2',
        )

    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.

        """
        if MyUser.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(validators.DUPLICATE_EMAIL, code='Exists')
        return self.cleaned_data['email']
