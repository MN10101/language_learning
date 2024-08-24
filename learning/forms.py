from django import forms
from .models import Profile, Answer

class TestForm(forms.Form):
    answers = forms.ModelMultipleChoiceField(
        queryset=Answer.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'profile_picture', 'first_name', 'last_name', 'age', 'address',
            'postal_code', 'city', 'country', 'birth_date',
            'phone_number', 'nationality', 'bio'
        ]
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }
