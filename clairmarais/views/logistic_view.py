from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from clairmarais.models import Poll, VoteOption, UserVote
from django.contrib.auth.models import User

@login_required
def logistic(request, poll_id):
    print("KIKOU")
    poll = get_object_or_404(Poll, id=poll_id)
    vote_options = VoteOption.objects.filter(poll=poll, category='logistic')
    user = request.user

    if request.method == 'POST':
        vote_option_id = request.POST.get('vote_option_id')
        vote_option = get_object_or_404(VoteOption, id=vote_option_id)
        UserVote.objects.create(user=user, vote_option=vote_option, response="Je ramène")

    print("-----------------------")
    print(user)
    print(vote_options)
    print(poll)
    return render(request, 'poll_votes/logistic.html', {'poll': poll, 'vote_options': vote_options})