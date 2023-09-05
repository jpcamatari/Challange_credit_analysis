from celery import shared_task
import redis
import json
import requests
from django.http import HttpResponse
import requests
from .models import FormSubmission


@shared_task
def process_form(form_data):
    r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
    r.lpush('fila_request', json.dumps(form_data))

    if len(form_data) >= 2:
        name = next(iter(form_data.values()))
        document = next(iter(form_data.values(), list(form_data.values())[1]))
        
        api = 'https://loan-processor.digitalsys.com.br/swagger/index.html#/Loan/post_loan_/loan/'

        data = {
        'name': name,
        'document': document,
        }
        response = requests.post(api, data=data)

        form_submission = FormSubmission.objects.create(
        data=form_data,
        response_data=response.json() if response.status_code == 200 else {},)
        form_submission.save()


        




    else:
        return HttpResponse('Erro: Falta de argumentos')

    
