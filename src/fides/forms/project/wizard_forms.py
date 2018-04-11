from django import forms

from fides.models.project import (Project, Breakpoint, )


class WizardBasicDetails(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(WizardBasicDetails, self).__init__(*args, **kwargs)

    class Meta:
        model = Project
        fields = ['name', 'codename', 'url', 'description', 'breakpoint', ]
        labels = {
            'name': 'Project Name *',
            'codename': 'Codename *',
            'url': 'Project URL *',
            'description': 'Description *',
            'breakpoint': 'Breakpoints *'
        }        