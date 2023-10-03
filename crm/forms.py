from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Customer


class RegisterForm(UserCreationForm):

    email = forms.EmailField(
        label="E-Mail address", widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'E-Mail address'}), \
            max_length=254, help_text="Required. Add a valid email address."
    )

    first_name = forms.CharField(
        label="First name", widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'First Name'}), \
            max_length=50, help_text="Required. Add your first name."
    )

    last_name = forms.CharField(
        label="Last name", widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Last Name'}), \
            max_length=50, help_text="Required. Add your last name."
    )


    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Username', \
                'help_text': '<span class="form-text text-muted">Required. Add a unique username.</span>'
            }
        )

        self.fields["password1"].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Password'}
        )

        self.fields["password2"].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Confirm Password', \
                'help_text': '<span class="form-text text-muted">Enter the same password as above, for verification.</span>'
            }
        )


class AddCustomerForm(forms.ModelForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    )
    email = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-Mail address'})
    )

    class Meta:
        model = Customer
        fields = ('username', 'first_name', 'last_name', 'email')
