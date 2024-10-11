from django.shortcuts import render, redirect, get_object_or_404
from items.models import Poll, Vote, Meal, Intendance, Game


def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    meal_proposals = Meal.objects.all()
    return render(request, 'poll_votes.html', {'poll': poll, 'meal_proposals': meal_proposals})

def poll_votes(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    votes = Vote.objects.filter(poll=poll)

    if request.method == 'POST':
        for vote in votes:
            response = request.POST.get(f'response_{vote.id}')
            if response:
                vote.response = response
                vote.save()
        return redirect('poll_success')

    return render(request, 'poll_votes.html', {'poll': poll, 'votes': votes})
