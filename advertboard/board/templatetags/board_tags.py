from django import template
from board.models import Advertisment, Responses


register = template.Library()

#для пагинации с фильтрацией
@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
   d = context['request'].GET.copy()
   for k, v in kwargs.items():
       d[k] = v
   return d.urlencode()


#этот при выводе статей на главной странице получает id объявления и текущего авторизованного пользователя
#если пользователь уже писал комментарий к этому объявлению, то объект фильтрации будет не пустой и выведется True
#если же пользователь ещё не писал комментарий, то выведется False (далее это отображается соответствующими кнопками)
@register.simple_tag()
def user_comments_exist(user_id = None, ads_id = None):
    r = Responses.objects.filter(user__pk = user_id, advert__pk = ads_id)
    if r:
        return True
    else:
        return False
