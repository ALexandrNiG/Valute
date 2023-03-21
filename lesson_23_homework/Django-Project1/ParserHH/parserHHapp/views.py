from parserHHapp.management.commands.full_db import Command
import os

from requests import get
from dotenv import load_dotenv
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import ContextMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .forms import ReqForm, UserReqForm, AuthUserReqForm
from .models import Vacancy, Word, Wordskill, Area, Schedule


# # Create your views here.
# def start(request):
#     return render(request, 'parserHHapp/index.html')
#
# def form(request):
#     form1 = ReqForm
#     return render(request, 'parserHHapp/form.html', context={'form': form1})


# def about(request):
#     if request.method == 'POST':
#         form = ReqForm(request.POST)
#         if form.is_valid():
#             vac = form.cleaned_data['vacancy']
#             where = form.cleaned_data['where']
#             pages = form.cleaned_data['pages']
#             print(vac, where, pages, sep='\n')
#             com = Command(vac, pages, where)
#             com.handle()
#             v = Word.objects.get(word=vac)
#             s = Wordskill.objects.filter(id_word_id=v.id).all()
#             vac = Vacancy.objects.filter(word_id=v).all()
#             print(vac, v, s, sep='\n')
#             return render(request, 'parserHHapp/about.html', context={'vac': vac, 'word': v, 'skills': s})
#         else:
#             form1 = ReqForm
#             return render(request, 'parserHHapp/form.html', context={'form': form1})






def start(request):
    return render(request, 'parserHHapp/index.html')


def form(request):
    if not request.user.is_authenticated:
        form1 = UserReqForm()
    else:
        form1 = AuthUserReqForm(initial={'vacancy': request.user.text,
                                         'areas': request.user.areas.all(),
                                         'schedules': request.user.schedules.all()})
    return render(request, 'parserHHapp/form.html', context={'form': form1})


def result(request):
    if request.method == 'POST':
        form = UserReqForm(request.POST)
        if form.is_valid():
            vac = form.cleaned_data['vacancy']
            where = form.cleaned_data['where']
            pages = form.cleaned_data['pages']
            # print(request.POST.getlist('areas'), request.POST.getlist('schedules'))
            areas = [Area.objects.filter(id=it).first() for it in request.POST.getlist('areas')]
            schedules = [Schedule.objects.filter(id=it).first() for it in request.POST.getlist('schedules')]
            # print(areas, schedules, sep='\n')
            com = Command(vac, pages, where, areas, schedules)
            com.handle()
            v = Word.objects.get(word=vac)
            s = Wordskill.objects.filter(id_word_id=v.id).all()
            vac = Vacancy.objects.filter(Q(word_id=v) & Q(area__in=areas) & Q(schedule__in=schedules)).order_by('published').all()
            print(vac, v, s, sep='\n')
            return render(request, 'parserHHapp/about.html', context={'vac': vac, 'word': v, 'skills': s})
        else:
            form1 = UserReqForm()
            return render(request, 'parserHHapp/form.html', context={'form': form1})


class WSList(ListView):
    model = Wordskill
    template_name = 'parserHHapp/ws_list.html'


class AreaList(ListView):
    model = Area
    template_name = 'parserHHapp/area_list.html'

    def get_queryset(self):
        return Area.objects.order_by('name').all()


class AreaDetail(DetailView):
    model = Area
    template_name = 'parserHHapp/area_detail.html'


class AreaPostMixin(ContextMixin):
    def prepare_area(self, url, areas):
        for item in areas:
            # print(item)
            if item['areas'] is not None:
                url[item['name']] = item['id']
                # print(1)
                self.prepare_area(url, item['areas'])
            else:
                url[item['name']] = item['id']

    def parce(self, area):
        # r = {'url': 'https://api.superjob.ru/2.0/vacancies/',
        #      'param': {'town': area,
        #                'period': 1},
        #      'header': {'X-Api-App-Id': os.getenv('key_super'),
        #                 'Authorization': 'Bearer r.000000010000001.example.access_token',
        #                 'Content-Type': 'application/x-www-form-urlencoded'}
        #      }
        self.hh, self.zarpl = dict(), dict()
        for url, d in (('https://api.hh.ru/areas', self.hh), ('https://api.zarplata.ru/areas', self.zarpl)):
            res = get(url).json()
            self.prepare_area(d, res)
        res = get(headers=r['header'], params=r['param']).json()
        return {'name': area, 'ind_hh': self.hh.get(area, 0),
                'ind_zarp': self.zarpl.get(area, 0),
                # 'ind_super': res['objects'][0]['town']['id'] if res['objects'] else 0
        }

    def post(self, request, *args, **kwargs):
        text = request.POST['name']
        print(text)
        new_index = self.parce(text)
        print(new_index)
        Area.objects.create(**new_index)
        return render(request, 'parserHHapp/area_list.html', context={'object_list': Area.objects.order_by('name').all()})


class AreaCreate(LoginRequiredMixin, CreateView, AreaPostMixin):
    model = Area
    fields = ['name']
    success_url = reverse_lazy('ParserHH:area_list')
    template_name = 'parserHHapp/area_create.html'


class AreaUpdateView(UpdateView):
    model = Area
    fields = ['name']
    success_url = reverse_lazy('parserHHapp:area_list')
    template_name = 'parserHHapp/area_create.html'


class AreaDeleteView(DeleteView):
    model = Area
    success_url = reverse_lazy('parserHHapp:area_list')
    template_name = 'parserHHapp/area_delete_confirm.html'

