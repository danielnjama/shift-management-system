from django.contrib import admin
from .models import Incident, Priority, Market, Status, ReassignedTeam, Backlog, SLAStatus
from import_export.admin import ExportActionMixin
class IncidentAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['incident_id', 'priority', 'market', 'summary', 'status', 'created_on', 'resolved_on', 'reassigned_team', 'dependency_reason', 'backlog', 'sla_status', 'engineer_responsible']
    search_fields = ['incident_id', 'summary', 'engineer_responsible__username']
    list_filter = ['priority', 'market', 'status', 'reassigned_team', 'backlog', 'sla_status']
    # list_per_page = 20
    # order =1 

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj is None:  # Only for adding new incidents, not for editing existing ones
            form.base_fields['engineer_responsible'].initial = request.user
        return form



admin.site.register(Incident, IncidentAdmin)
admin.site.register(Priority)
admin.site.register(Market)
admin.site.register(Status)
admin.site.register(ReassignedTeam)
admin.site.register(Backlog)
admin.site.register(SLAStatus)
