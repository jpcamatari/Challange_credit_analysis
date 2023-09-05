from django import forms
from django.contrib import admin
from .models import DynamicForm, DynamicFormField, FormSubmission

class DynamicFormFieldInline(admin.TabularInline):
    model = DynamicForm.form_fields.through

@admin.register(DynamicForm)
class DynamicFormAdmin(admin.ModelAdmin):
    inlines = [DynamicFormFieldInline]

@admin.register(FormSubmission)
class FormSubmissionAdmin(admin.ModelAdmin):
    list_display = ('data', 'response_data')
    list_filter = ('response_data',)
    list_editable = ('response_data',)



admin.site.register(DynamicFormField)

