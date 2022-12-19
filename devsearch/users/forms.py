from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Skill, Message

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name':'Name',
        }
    
    # over  write the super method, iterate over the fields and add "input class"
    def __init__(self, *args, **kwargs):
        # overiding the parent class constructure, vai looping thorough each value and updating it
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            
            
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["name", "username", "location", "email", "short_intro", "bio", "profile_image", 
                  "social_github", "social_linkedin", "social_leetcode", "personal_website", 
                  ]
    # over  write the super method, iterate over the fields and add "input class"
    def __init__(self, *args, **kwargs):
        # overiding the parent class constructure, vai looping thorough each value and updating it
        super(ProfileForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            # updating the class attribute for inputs box styling
            field.widget.attrs.update({'class': 'input'})


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"
        exclude = ["owner"]
        
    # over  write the super method, iterate over the fields and add "input class"
    def __init__(self, *args, **kwargs):
        # overiding the parent class constructure, vai looping thorough each value and updating it
        super(SkillForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            # updating the class attribute for inputs box styling
            field.widget.attrs.update({'class': 'input'})
            
            
class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'body']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})