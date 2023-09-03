from django.shortcuts import render, HttpResponse
from .models import DynamicForm
from .tasks import process_form, get_form_data



def dynamic_form_view(request, form_id):
    if form_id is None:
        form_id = 1

    dynamic_form = DynamicForm.objects.get(pk=form_id)

    if request.method == 'POST':
        form_data = get_form_data(request, dynamic_form, form_id)

        process_form.delay(form_data)
        return HttpResponse('Analise Enviada com Sucesso')
        
            
            
    else:
        #Renderizar o formulário com base nos campos
        fields = dynamic_form.form_fields.all()
        context = {'dynamic_form': dynamic_form, 'fields': fields}
        return render(request, 'form.html', context)

