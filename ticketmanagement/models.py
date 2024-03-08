from django.db import models
from django.contrib.auth.models import User

class Priority(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Priority"

class Market(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Status"

class ReassignedTeam(models.Model):
    name = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.name

class Backlog(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SLAStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "SLA Status"


class Incident(models.Model):
    incident_id = models.CharField(max_length=100, verbose_name="Incident ID")
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, verbose_name="Priority")
    market = models.ForeignKey(Market, on_delete=models.CASCADE, verbose_name="Market")
    summary = models.TextField(verbose_name="Summary")
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name="Status")
    created_on = models.DateField(verbose_name="Created On")
    resolved_on = models.DateField(null=True, blank=True, verbose_name="Resolved On")
    reassigned_team = models.ForeignKey(ReassignedTeam, on_delete=models.CASCADE, verbose_name="Reassigned Team",blank=True)
    dependency_reason = models.TextField(verbose_name="Dependency Reason",blank=True)
    backlog = models.ForeignKey(Backlog, on_delete=models.CASCADE, verbose_name="Backlog")
    sla_status = models.ForeignKey(SLAStatus, on_delete=models.CASCADE, verbose_name="SLA Status")
    engineer_responsible = models.ForeignKey(User, on_delete=models.CASCADE,max_length=100, verbose_name="Engineer responsible")

    def __str__(self):
        return self.incident_id
