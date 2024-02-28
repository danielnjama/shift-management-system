# views.py
from django.shortcuts import render
from .models import Shift, UserInfo
from django.db.models import Count,Q
# views.py
from django.http import HttpResponse
import openpyxl
from django.contrib.auth.decorators import login_required

@login_required(login_url='/admin')
def shift_list(request):
    team_filter = request.GET.get('team')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    shifts = Shift.objects.filter(
        team_member__isnull=False  # Ensure team_member is not null
    )

    if team_filter:
        # Filter by team using ForeignKey relationship to UserInfo
        shifts = shifts.filter(team_member__userinfo__team=team_filter)
    
    if start_date and end_date:
        shifts = shifts.filter(date__range=[start_date, end_date])

    shift_counts = []  # Initialize with an empty list

    # Check if there are any filtered shifts before calculating shift_counts
    if shifts.exists():
        shift_counts = shifts.values('team_member__username', 'team_member__userinfo__employeeID').annotate(
            morning_count=Count('pk', filter=Q(shift_type='Morning')),
            night_count=Count('pk', filter=Q(shift_type='Night'))
        )

    teams = UserInfo.objects.values_list('team', flat=True).distinct()  # Retrieve distinct teams from UserInfo model
    context = {
        'teams': teams,
        'shift_counts': shift_counts
    }

    return render(request, 'index.html', context)



@login_required(login_url='/admin')
def shift_listsss(request):
    team_filter = request.GET.get('team')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    shifts = Shift.objects.filter(
        team_member__isnull=False  # Ensure team_member is not null
    )

    if team_filter:
        # Filter by team using ForeignKey relationship to UserInfo
        shifts = shifts.filter(team_member__userinfo__team=team_filter)
    
    if start_date and end_date:
        shifts = shifts.filter(date__range=[start_date, end_date])

    # Aggregate shift counts per user including employeeID
    # shift_counts = Shift.objects.filter(
    #     team_member__isnull=False  # Ensure team_member is not null
    # ).values('team_member__username', 'team_member__userinfo__employeeID').annotate(
    #     morning_count=Count('pk', filter=Q(shift_type='Morning')),
    #     night_count=Count('pk', filter=Q(shift_type='Night'))
    # )
        shift_counts = shifts.values('team_member__username', 'team_member__userinfo__employeeID').annotate(
        morning_count=Count('pk', filter=Q(shift_type='Morning')),
        night_count=Count('pk', filter=Q(shift_type='Night'))
    )

    teams = UserInfo.objects.values_list('team', flat=True).distinct()  # Retrieve distinct teams from UserInfo model
    context = {
        'shifts': shifts,
        'teams': teams,
        'shift_counts': shift_counts
    }


    return render(request, 'index.html', context)

def download_shift_summary_excel(request):
    shift_counts = Shift.objects.filter(
        team_member__isnull=False
    ).values('team_member__username').annotate(
        morning_count=Count('pk', filter=Q(shift_type='Morning')),
        night_count=Count('pk', filter=Q(shift_type='Night'))
    )

    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.title = "Shift Summary"
    worksheet.append(['Name', 'Morning Shifts', 'Night Shifts'])

    for count in shift_counts:
        worksheet.append([
            count['team_member__username'],
            count['morning_count'],
            count['night_count']
        ])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=shift_summary.xlsx'
    workbook.save(response)
    return response