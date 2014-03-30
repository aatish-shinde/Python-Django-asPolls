from django.contrib import admin
from polls.models import Choice

# Register your models here.
from polls.models import Poll

class ChoiceInLine(admin.TabularInline):
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	#use the list_display admin option, which is a tuple of field names to display, as columns, on the change list page for the object:
	list_display = ('question', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question']

	fieldsets = [
		(None, {'fields' : ['question']}),
		('Date Information', {'fields' : ['pub_date'], 'classes':['collapse']}),
	]
	inlines = [ChoiceInLine]

admin.site.register(Poll, PollAdmin)