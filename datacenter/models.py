from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )


def get_duration(visit):
    if visit.leaved_at is None:
        duration = localtime() - localtime(visit.entered_at)
    else:
        duration = visit.leaved_at - visit.entered_at
    return int(duration.total_seconds())


def format_duration(duration):
    seconds = duration
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f'{hours:02}:{minutes:02}'


def is_visit_long(visit, minutes=60):
    dutarion_minutes = (get_duration(visit) % 3600) // 60
    return dutarion_minutes > minutes
    