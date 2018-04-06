from django.contrib import admin

from fides.models.project import (Project, Breakpoint, )

admin.site.register(Project)
admin.site.register(Breakpoint)