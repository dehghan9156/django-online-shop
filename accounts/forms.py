# from django import forms
# from django.contrib.auth import get_user_model
# from django.core.exceptions import ValidationError

# User = get_user_model()

# class UserRegisterForm(forms.ModelForm):
#     confirm_password = forms.CharField()
#     class Meta:
#         models = User
#         fields = ["name","family","address","description","email","password","confirm_password"]

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")
#         if password and confirm_password and password != confirm_password:
#             raise ValidationError("Passwords do not match.")
#         return cleaned_data