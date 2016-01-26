from django import forms

import models


class JourneyForm(forms.ModelForm):
    class Meta:
        model = models.journey
        fields = ('traveller_name', 'traveller_email', 'traveller_phone',
                  'start_time', 'end_time')
