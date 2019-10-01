from django.contrib import admin

from .models import OtherImages, Project, ProjectDescription

@admin.register(ProjectDescription)
class ProjectDescriptionAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated')
   
    

class OtherProjectImages(admin.TabularInline):
    model = OtherImages
    extra = 1
    verbose_name_plural = 'Other Project Images'


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','date')

    inlines = [OtherProjectImages]
