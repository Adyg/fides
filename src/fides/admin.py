from django.contrib import admin

from fides.models.project import (Project, Breakpoint, ProjectPage, ProjectPagePrevisualAssesment, )

admin.site.register(Project)
admin.site.register(ProjectPage)
admin.site.register(Breakpoint)
admin.site.register(ProjectPagePrevisualAssesment)