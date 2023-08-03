from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from board.models import Advertisment, Responses, User
from django.core.paginator import Paginator
from board.filters import RespFilter

# Create your views here.


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mailuser'] = self.request.user.groups.filter(name='mailusers').exists()
        return context


class AdsView(LoginRequiredMixin, TemplateView):
    template_name = 'userads.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['responses'] = Responses.objects.filter(advert__user = self.request.user.id).order_by('-time_create')
        ads = Advertisment.objects.filter(user=self.request.user.id).order_by('-time_create')
        paginator = Paginator(ads, 5)

        page_number = self.request.GET.get('page')
        context['page_obj'] = paginator.get_page(page_number)

        return context


class RespView(LoginRequiredMixin, ListView):
    model = Responses
    template_name = 'userresp.html'
    ordering = '-time_create'
    context_object_name = 'resp'

    paginate_by = 1

    def get_queryset(self):
        #чтобы показывать только отклики на статьи пользователя нужен другой запрос
        queryset = Responses.objects.filter(advert__user = User.objects.get(pk=self.request.user.id))
        self.filterset = RespFilter(self.request.GET, queryset, request=self.request)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


def accept_response(request):
    resp = Responses.objects.get(pk = request.POST['respid'])
    resp.acceptresponse = True
    resp.save(update_fields=["acceptresponse"])
    return redirect('userresp')
