from celery import shared_task

from django.shortcuts import render, HttpResponse
from .models import DynamicForm

@shared_task
def dynamic_form_view(request, form_id):
    if form_id is None:
        form_id = 1

    dynamic_form = DynamicForm.objects.get(pk=form_id)

    if request.method == 'POST':
        form_data = {}

        for field in dynamic_form.form_fields.all():
            field_label = field.label
            form_data[field_label] = request.POST.get(field_label)
            return HttpResponse('Analise Enviada com Sucesso')
        print(form_data)
            
            
    else:
        # Renderizar o formulário com base nos campos associados
        fields = dynamic_form.form_fields.all()
        context = {'dynamic_form': dynamic_form, 'fields': fields}
        return render(request, 'form.html', context)