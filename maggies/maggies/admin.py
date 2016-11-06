from django.contrib import admin
from .models import PwC, Carer, OtherVisitor, DailyIdentifier, Centre, StaffRole, StaffMember, Activity

admin.site.register(Centre)
admin.site.register(StaffRole)
admin.site.register(StaffMember)
admin.site.register(Activity)
