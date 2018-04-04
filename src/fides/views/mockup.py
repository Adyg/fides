from django.http import HttpResponse
from django.shortcuts import render


def mockup_login(request):

    return render(request, 'mockup/login.html', {
    })


def mockup_dashboard(request):

    return render(request, 'mockup/dashboard.html', {
    })


def mockup_add_project(request):

    return render(request, 'mockup/add_project.html', {
    })


def mockup_project_dashboard(request):

    return render(request, 'mockup/project_dashboard.html', {
    })


def mockup_project_dashboard_visual(request):

    return render(request, 'mockup/project_dashboard_visual.html', {
    })


def mockup_visual_consistency_page(request):

    return render(request, 'mockup/visual_consistency_page.html', {
    })            