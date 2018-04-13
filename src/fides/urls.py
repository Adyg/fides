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
from fides.views import user as user_views
from fides.views import project as project_views


urlpatterns = [
    path('admin/', admin.site.urls),

    ## MOCKUP
    #path('', mockup_views.mockup_login, name='login'),
    path('project/dashboard', mockup_views.mockup_project_dashboard, name='project-dashboard'),
    path('project/dashboard/visual', mockup_views.mockup_project_dashboard_visual, name='project-dashboard-visual'),
    path('project/dashboard/visual/page/awd234aqafea', mockup_views.mockup_visual_consistency_page, name='project-dashboard-visual-page'),
    ## END MOCKUP

    ## USER
    path('', auth_views.login, {'template_name': 'user/login.html'}),
    path('dashboard/', user_views.dashboard, name='dashboard'),
    path('wizard/project/basic-site-details/', project_views.wizard_project_basic_site_details, name='wizard-project-basic-site-details'),
    path('wizard/project/scrape-site/<str:project_codename>', project_views.wizard_project_scrape_site, name='wizard-project-scrape-site'),
    path('wizard/project/add-pages/<str:project_codename>', project_views.wizard_project_add_pages, name='wizard-project-add-pages'),
    path('wizard/project/visual-assesment/<str:project_codename>', project_views.wizard_project_visual_assesment, name='wizard-project-visual-assesment'),
    path('wizard/project/build-dataset/', project_views.wizard_project_build_dataset, name='wizard-project-build-dataset'),

    path('project/page/delete/', project_views.delete_page, name='delete-page'),
    ## END USER

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
