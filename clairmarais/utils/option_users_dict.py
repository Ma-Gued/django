from clairmarais.models import UserVote

def get_option_users_dict(vote_options):
    option_users_dict = {}
    for option in vote_options:
        user_votes_for_option = UserVote.objects.filter(vote_option=option)
        option_users_dict[option.id] = {
            'oui': [vote.user.username for vote in user_votes_for_option if vote.response == 'oui'],
            'non': [vote.user.username for vote in user_votes_for_option if vote.response == 'non']
        }