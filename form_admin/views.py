from django.shortcuts import render
from .models import DynamicForm

def dynamic_form_view(request, form_id):
    dynamic_form = DynamicForm.objects.get(pk=form_id)

    if request.method == 'POST':
        form_data = {}

        for field in dynamic_form.form_fields.all():
            field_name = field.field_name
            form_data[field_name] = request.POST.get(field_name)
            
    else:
        # Renderizar o formulário com base nos campos associados
        fields = dynamic_form.form_fields.all()
        context = {'dynamic_form': dynamic_form, 'fields': fields}
        return render(request, 'form.html', context)

