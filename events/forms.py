from django.forms import ModelForm

from events.models import Submission


class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ['details']
