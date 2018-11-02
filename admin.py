from django.contrib import admin
from .models import Images,Themes

# Register your models here.
admin.site.register(Images)

#@admin.register(Background)

'''
class FlatPageAdmin(admin.ModelAdmin):
	
	fields = ('background_name')

	def __str__(self):
		return "Background"
	
	fields = ('page',)

admin.site.register(BackgroundSelection, FlatPageAdmin)
'''