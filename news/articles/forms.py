# articles/forms.py
from django import forms
from .models import Comment

# Create forms here


# '.ModelForm' is a helper class designed to translate database models into forms
# The comments should now be visible due to this form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment", "author")
