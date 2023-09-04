from celery import shared_task
import redis
import json
from .models import DynamicForm


def get_form_data(request, dynamic_form, form_id):
    form_data = {}
    if form_id is None:
        form_id = 1
    dynamic_form = DynamicForm.objects.get(pk=form_id)
    for field in dynamic_form.form_fields.all():
        field_id = field.label
        form_data[field_id] = request.POST.get(field_id)

    return form_data


@shared_task
def process_form(form_data):
    
    form_data = get_form_data()
    return form_data

    #r = redis.StrictRedis(host='localhost', port=6379, db=0)
    #r.lpush('fila_request', json.dumps(form_data))
