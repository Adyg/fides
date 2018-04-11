from django.contrib import admin

from fides.models.project import (Project, Breakpoint, ProjectPage, )

admin.site.register(Project)
admin.site.register(ProjectPage)
admin.site.register(Breakpoint)