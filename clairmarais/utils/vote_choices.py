def get_vote_choices(poll):
    if poll.form_type == 'emoji':
        return ['👎', '🤐', '👍']
    elif poll.form_type == 'yes_no':
        return ['👎', '👍']
    else:
        return []