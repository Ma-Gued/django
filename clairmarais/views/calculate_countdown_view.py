from django.utils import timezone
from datetime import datetime

def calculate_countdown():
    # Date cible pour le compte à rebours
    target_date = datetime(2024, 11, 1, 18, 0, 0)
    target_date = timezone.make_aware(target_date, timezone.get_current_timezone())
    now = timezone.now()

    # Calculer le temps restant
    time_remaining = target_date - now

    # Extraire les jours, heures, minutes et secondes
    days = time_remaining.days
    hours, remainder = divmod(time_remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return {
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds,
    }