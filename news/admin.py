from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
	date_hierarchy = 'created'
	list_display = ["__str__", 'created']
	search_fields = ['title']
	list_filter = ('created',)
	
	class Meta:
		model = Post


admin.site.register(Post, PostAdmin)