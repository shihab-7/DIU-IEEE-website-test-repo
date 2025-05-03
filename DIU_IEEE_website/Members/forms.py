from django import forms
from .models import MemberProfile, Projects
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User



class MemberProfileForm(forms.ModelForm):
    class Meta:
        model = MemberProfile
        fields = ['profile_picture', 'date_of_birth', 'about', 'skills', 'facebook_link', 'linkedin_link', 'github_link', 'member_type', 'member_id', 'club_position']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'about': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'skills': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'facebook_link': forms.URLInput(attrs={'placeholder': 'https://www.facebook.com/yourprofile'}),
            'linkedin_link': forms.URLInput(attrs={'placeholder': 'https://www.linkedin.com/in/yourprofile'}),
            'github_link': forms.URLInput(attrs={'placeholder': 'https://www.github.com/yourprofile'}),
            'member_id': forms.TextInput(attrs={'placeholder': 'Enter your member ID'}),
            'club_position': forms.TextInput(attrs={'placeholder': 'Enter your club position'}),
            'member_type': forms.Select(attrs={'class': 'form-control'}),
        }


class CustomUserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'password' in self.fields:
            del self.fields['password']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['title', 'image', 'link']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Project Title'}),
            'image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
            'link': forms.URLInput(attrs={'placeholder': 'https://www.example.com'}),
        }


class MemberEditForm(forms.ModelForm):
    class Meta:
        model = MemberProfile
        fields = ['profile_picture', 'date_of_birth', 'about', 'skills', 'facebook_link', 'linkedin_link', 'github_link', 'member_type', 'member_id', 'club_position']
    def __init__(self, *args, **kwargs):
        user_instance = kwargs.pop('user_instance', None)
        super().__init__(*args, **kwargs)
        self.user_form = CustomUserEditForm(instance=user_instance) 
        if user_instance:
            self.user_form = CustomUserEditForm(instance=user_instance)
        else:
            self.user_form = CustomUserEditForm()
        self.profile_form = MemberProfileForm(instance=self.instance)