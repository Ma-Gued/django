from clairmarais.models import VoteOption

def delete_option(request, user, poll):
    option_id = request.POST.get('delete_option')
    VoteOption.objects.filter(id=option_id, user=user).delete()
    should_redirect = True