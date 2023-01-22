from django.shortcuts import render, redirect
from .models import Advertisment, Responses, User
from django.views.generic import ListView,CreateView,UpdateView, DeleteView, DetailView, FormView
from django.contrib.auth.models import Group
from .forms import AdsForm, ResponseForm, MailForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .filters import RespFilter

# Create your views here.

class AdsList(ListView):
    model = Advertisment
    ordering = 'time_create'
    template_name = 'index.html'
    context_object_name = 'adv'

    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['form'] = ResponseForm
        return context

class AdsDetail(DetailView):
    model = Advertisment
    template_name = 'adsdetail.html'
    context_object_name = 'ads'


class AdsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('board.add_advertisment')
    model = Advertisment
    template_name = 'adsedit.html'
    form_class = AdsForm

    def form_valid(self, form):

        ads = form.save(commit=False)
        # добавляю текущего автора при создании новости
        ads.user = self.request.user

        return super().form_valid(form)

class AdsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('board.change_advertisment')
    form_class = AdsForm
    model = Advertisment
    template_name = 'adsedit.html'


class AdsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('board.delete_advertisment')
    model = Advertisment
    template_name = 'adsdelete.html'
    success_url = reverse_lazy('board')

class RespDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('board.delete_responses')
    model = Responses
    template_name = 'adsdelete.html'
    success_url = reverse_lazy('board')

class MailingCreate(LoginRequiredMixin, FormView):
    template_name = 'mailing.html'
    form_class = MailForm
    success_url = '/mailing/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mailuser'] = self.request.user.groups.filter(name='mailusers').exists()
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)

#функция записывает в базу отклики на объявления
@login_required
def save_comment(request):
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            Responses.objects.create(user=User.objects.get(pk = request.user.id), text=request.POST['text'], \
            advert=Advertisment.objects.get(pk = request.POST['advid']))
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
