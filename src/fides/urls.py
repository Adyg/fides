"""fides URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from fides.views import mockup as mockup_views

urlpatterns = [
    path('admin/', admin.site.urls),

    ## MOCKUP
    #path('', mockup_views.mockup_login, name='login'),
    path('dashboard/', mockup_views.mockup_dashboard, name='dashboard'),
    path('add/project/', mockup_views.mockup_add_project, name='add-project'),
    path('project/dashboard', mockup_views.mockup_project_dashboard, name='project-dashboard'),
    path('project/dashboard/visual', mockup_views.mockup_project_dashboard_visual, name='project-dashboard-visual'),
    path('project/dashboard/visual/page/awd234aqafea', mockup_views.mockup_visual_consistency_page, name='project-dashboard-visual-page'),
    ## END MOCKUP

    ## USER
    path('', auth_views.login, {'template_name': 'user/login.html'}),
    ## END USER

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
