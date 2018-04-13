from django import forms

from fides.models.project import (Project, ProjectPagePrevisualAssesment, )


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


class ProjectPagePrevisualAssesmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectPagePrevisualAssesmentForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ProjectPagePrevisualAssesment
        fields = ['url_pattern', 'js_code', 'test_original', ]
        labels = {
            'url_pattern': 'URL Pattern *',
            'js_code': 'JS Code *',
            'test_original': 'Test both the original page and the page after the JS code is executed'
        }