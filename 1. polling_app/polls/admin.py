from django.contrib import admin
from .models import Question, Choice

# Configuring the name of admin panel
admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to the Pollster Admin Area"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields' : ['question_text']}),
                ('Date Information', {'fields' : ['pub_date'], 'classes' : ['collapse']}),]

    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)