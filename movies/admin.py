from django.contrib import admin
from .models import *

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email')

	search_fields = ('first_name', 'last_name')

class MovieAdmin(admin.ModelAdmin):
	list_display = ('title',  'release_date', 'language' )
	list_filter = ('release_date',)
	ordering = ('title', 'release_date', 'language', 'genre')
	search_fields = ('title', )
	filter_horizontal = ('genre', )
#	raw_id_fields = ('genre',)


admin.site.register(Genre)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Tag)
admin.site.register(Movie_Has_Tag)
admin.site.register(Crew)
admin.site.register(User)
admin.site.register(Review)
