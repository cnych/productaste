from django import template

from apps.product.models import ProductVote

register = template.Library()


@register.inclusion_tag('tags/vote_button.html', takes_context=True)
def vote_button(context, product):
    user = context['user']
    if user.is_authenticated:
        return {
            'voted': ProductVote.voted(user, product),
            'pid': product.pid,
            'vote_count': product.vote_count
        }
    
    return {'voted': False, 'pid': product.pid, 'vote_count': product.vote_count}
