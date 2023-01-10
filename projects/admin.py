from django.contrib import admin

from .models import Project, Review, Tag
# to register the models
admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)