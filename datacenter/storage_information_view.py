from datacenter.models import Visit
from datacenter.models import get_duration, format_duration
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = [
        {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': format_duration(get_duration(visit))
        }
        for visit in Visit.objects.filter(leaved_at=None)
    ]
    context = {'non_closed_visits': non_closed_visits}
    return render(request, 'storage_information.html', context)
