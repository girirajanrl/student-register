from django.contrib import admin
from .models import StudentProject, TeamMember, Payment


admin.site.register(StudentProject)

admin.site.register(TeamMember)

admin.site.register(Payment)