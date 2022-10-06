from django.contrib import admin

from events.models import Event, Submission

admin.site.register(Event)
admin.site.register(Submission)
