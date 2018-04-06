from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from fides.models.project import (Project, )


@login_required
def create_project(request):

    return render(request, 'project/create_project.html', {

    })