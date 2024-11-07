from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    if isinstance(dictionary, dict):
        return dictionary.get(key)
    return None


@register.simple_tag
def has_voted(user_votes, user, response):
    for vote in user_votes:
        if vote['user'] == user and vote['response'] == response:
            return True
    return False