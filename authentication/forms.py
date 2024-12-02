from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from authentication.models import UserProfile
from django.core.exceptions import ValidationError

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email", required=True)
    full_name = forms.CharField(label="Name", required=True)


    class Meta:
        model = User
        fields = ("username", "full_name", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email address must be unique. This email is already in use.")
        return email

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]  # Set email from cleaned data
        if commit:
            user.save()  # Save user first to create a User instance

            # Create UserProfile associated with the User
            UserProfile.objects.create(
                user=user,
                full_name=self.cleaned_data["full_name"]
            )
        return user