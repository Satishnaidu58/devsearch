from django.forms import ModelForm
from django import forms
from .models import Project, Review

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tags']
        # can mopdify css class with widgets
        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
        }
        
    def __init__(self, *args, **kwargs):
        # overiding the parent class constructure, inheriting
        super(ProjectForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']
        labels = {
            'value':'place your vote',
            'body':'Add a comment with your vote'
        }
                
    def __init__(self, *args, **kwargs):
        # overiding the parent class constructure, inheriting
        super(ReviewForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})