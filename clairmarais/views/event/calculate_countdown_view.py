from django.utils import timezone
from datetime import datetime
from clairmarais.models import Event

def calculate_countdown(event_date):
    # Date cible pour le compte à rebours (à partir de la date de l'événement)
    target_date = Event.objects.get(id=1).date
    # Vérifier si la date cible est naïve ou consciente du fuseau horaire
    if timezone.is_naive(target_date):
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