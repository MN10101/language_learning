from django import forms
from .models import Profile, Answer
from .models import UserFile


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UserFile
        fields = ['file'] 

class TestForm(forms.Form):
    answers = forms.ModelMultipleChoiceField(
        queryset=Answer.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

class ProfileForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, required=True)  # Add email field

    class Meta:
        model = Profile
        fields = [
            'profile_picture', 'first_name', 'last_name', 'email', 'age', 'address',
            'postal_code', 'city', 'country', 'birth_date', 'phone_number', 'nationality', 'bio'
        ]
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        # Populate the email field from the related User model
        self.fields['email'].initial = self.instance.user.email

    def save(self, commit=True):
        # Save the Profile model and update the User model's email field
        profile = super(ProfileForm, self).save(commit=False)
        profile.user.email = self.cleaned_data['email']
        if commit:
            profile.save()
            profile.user.save()  # Save the User model to store the email change
        return profile
