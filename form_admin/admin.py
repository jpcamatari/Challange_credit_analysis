from django import forms
from django.contrib import admin
from .models import DynamicForm, DynamicFormField

class DynamicFormFieldInline(admin.TabularInline):
    model = DynamicForm.form_fields.through

@admin.register(DynamicForm)
class DynamicFormAdmin(admin.ModelAdmin):
    inlines = [DynamicFormFieldInline]

admin.site.register(DynamicFormField)

