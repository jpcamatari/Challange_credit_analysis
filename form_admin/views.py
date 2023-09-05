from django.shortcuts import render
from django.http import JsonResponse
from .models import DynamicForm
from .tasks import process_form



def dynamic_form_view(request, form_id):
    if form_id is None:
        form_id = 1

    dynamic_form = DynamicForm.objects.get(pk=form_id)
    
    if request.method == 'POST':
        form_data = {}

        for field in dynamic_form.form_fields.all():
            field_id = field.label
            form_data[field_id] = request.POST.get(field_id)
            
        process_form.delay(form_data)
        return JsonResponse(form_data)
              
            
    else:
        #Renderizar o formulário com base nos campos
        fields = dynamic_form.form_fields.all()
        context = {'dynamic_form': dynamic_form, 'fields': fields}
        return render(request, 'form.html', context)

