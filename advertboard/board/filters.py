from django_filters import FilterSet, ModelChoiceFilter
from django_filters.widgets import *
from .models import Advertisment, Responses,CATEGORY, User

#определяю фукнцию, которая будет в форме выводить выбор статей только авторизованного пользователя
def adv(request):
    if request is None:
        return Advertisment.objects.none()

    print(request.user)
    return Advertisment.objects.filter(user__pk = request.user.pk)


class RespFilter(FilterSet):

    advert = ModelChoiceFilter(
        field_name='advert__head',
        queryset=adv, #добавляю функцию, которая вернет нужный queryset
        label='Название статьи'

    )
