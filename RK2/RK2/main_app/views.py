from django.shortcuts import render
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from datetime import datetime


def index(request):
    return render(request, 'index.html')


def report(request):
    PCs = PC.objects.all()
    params = {'PCs': PCs, 'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    return render(request, 'report.html', params)


def PC_list(request):
    PCs = PC.objects.all().values()
    params = {'entity': 'PC', 'objects': PCs}
    return render(request, 'list.html', params)


def processor_list(request):
    processors = Processor.objects.all().values()
    params = {'entity': 'Processor', 'objects': processors}
    return render(request, 'list.html', params)


class ProcessorCreate(CreateView):
    model = Processor
    fields = ['name', 'memory_cash', 'frequency']
    success_url = '/processor'
    template_name = 'processor_form.html'


class ProcessorUpdate(UpdateView):
    model = Processor
    fields = ['name', 'memory_cash', 'frequency']
    pk_url_kwarg = 'id'
    success_url = '/processor'
    template_name = 'processor_form.html'


class ProcessorDelete(DeleteView):
    model = Processor
    pk_url_kwarg = 'id'
    success_url = '/processor'
    template_name = 'processor_delete_form.html'


class PCCreate(CreateView):
    model = PC
    fields = ['name', 'price', 'processor_id']
    success_url = '/PC'
    template_name = 'PC_form.html'

    def get_context_data(self, **kwargs):
        context = super(PCCreate, self).get_context_data(**kwargs)
        context['form'].fields['processor_id'] = forms.ModelChoiceField(queryset=Processor.objects.all(),
                                                                    empty_label=None, label='Microprocessor')
        return context


class PCUpdate(UpdateView):
    model = PC
    fields = ['name', 'price', 'processor_id']
    pk_url_kwarg = 'id'
    success_url = '/PC'
    template_name = 'PC_form.html'

    def get_context_data(self, **kwargs):
        context = super(PCUpdate, self).get_context_data(**kwargs)
        context['form'].fields['processor_id'] = forms.ModelChoiceField(queryset=Processor.objects.all(),
                                                                   empty_label=None, label='Микропроцессор')
        return context


class PCDelete(DeleteView):
    model = PC
    pk_url_kwarg = 'id'
    success_url = '/PC'
    template_name = 'PC_delete_form.html'