from django.db import models

class DynamicFormField(models.Model):
    label = models.CharField(max_length=20)
    field_type = models.CharField(max_length=20, choices=[('text', 'Text'), ('number', 'Number'), ('date', 'Date')])

    def __str__(self):
        return self.label

class DynamicForm(models.Model):
    title = models.CharField(max_length=20)
    form_fields = models.ManyToManyField(DynamicFormField, blank=True)

    def __str__(self):
        return self.title
    
class FormSubmission(models.Model):
    data = models.JSONField()
    response_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.data
