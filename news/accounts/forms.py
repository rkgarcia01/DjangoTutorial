# accounts/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

# UserCreationForm, provides fields such as
#  - 'username'
#  - 'password1'
#  - 'password2' (confirmation)
#  - Have added a custom 'field' 'age' from your 'CustomUser' model
# So basically when used in 'SignUpView' in 'views.py', it collects user input,
# validates it, and saves the new user to the datbase.

# Meta.fieds, will just diaply the default settings of
#  - 'username'
#  - 'password'
#  - 'age'


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ("age",)
        fields = (
            "username",
            "email",
            "age",
        )


# UserChangeForm, is used to updates existing user detials
#  - Typically in Django admin interface or custo profile editing views.
#  - 'CustomUser' model from 'models.py' might have additional fields like 'age'
#    and this form ensures they're available when updating user data.
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ("username", "email", "age")
