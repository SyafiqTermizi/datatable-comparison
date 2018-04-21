from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView

from .models import Human


class HumanListViewHtmlTable(ListView):
    model = Human
    template_name = 'humans/html_table.html'


class HumanListViewHtmlTablePagination(ListView):
    model = Human
    template_name = 'humans/html_table_pagination.html'
    paginate_by = 15


class HumanListViewJqueryTable(ListView):
    model = Human
    template_name = 'humans/jquery_table.html'


class HumanListViewJqueryTableAjax(TemplateView):
    template_name = 'humans/jquery_table_ajax.html'


class HumanDetailView(DetailView):
    model = Human
    pk_url_kwarg = 'pk'

