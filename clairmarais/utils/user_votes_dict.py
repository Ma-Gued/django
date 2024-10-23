from clairmarais.models import UserVote

def get_user_votes_dict(vote_options):
    user_votes = UserVote.objects.filter(vote_option__in=vote_options)
    user_votes_dict = {option.id: [] for option in vote_options}
    for vote in user_votes:
        user_votes_dict[vote.vote_option.id].append({
            'user': vote.user.username, 
            'response': vote.response
            })
    return user_votes_dict