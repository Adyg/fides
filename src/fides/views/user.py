from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from fides.models.project import (Project, )

@login_required
def dashboard(request):
    projects = Project.objects.all()

    return render(request, 'user/dashboard.html', {
        'projects': projects,
    })
