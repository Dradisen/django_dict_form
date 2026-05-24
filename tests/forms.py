from django import forms

from .models import AllFieldTypesModel

class AllFieldTypesForm(forms.ModelForm):
    
    class Meta:
        model = AllFieldTypesModel
        fields = '__all__'

        widgets = {
            # Text Inputs
            'char_field': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст'
            }),

            'text_field': forms.Textarea(attrs={
                'rows': 5,
                'class': 'form-control'
            }),

            'email_field': forms.EmailInput(attrs={
                'class': 'form-control'
            }),

            'url_field': forms.URLInput(attrs={
                'class': 'form-control'
            }),

            'slug_field': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            # Number Inputs
            'integer_field': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'float_field': forms.NumberInput(attrs={
                'step': '0.01'
            }),

            'decimal_field': forms.NumberInput(attrs={
                'step': '0.01'
            }),

            # Checkbox
            'boolean_field': forms.CheckboxInput(),

            # Date / Time
            'date_field': forms.DateInput(attrs={
                'type': 'date'
            }),

            'time_field': forms.TimeInput(attrs={
                'type': 'time'
            }),

            'datetime_field': forms.DateTimeInput(attrs={
                'type': 'datetime-local'
            }),

            # File Inputs
            'file_field': forms.ClearableFileInput(),
            'image_field': forms.ClearableFileInput(),

            # JSON
            'json_field': forms.Textarea(attrs={
                'rows': 6,
                'class': 'form-control'
            }),

            # Select
            'choices_field': forms.Select(attrs={
                'class': 'form-select'
            }),

            # Multiple Select
            'many_to_many': forms.SelectMultiple(attrs={
                'class': 'form-select'
            }),

            # Hidden
            'uuid_field': forms.HiddenInput(),

            # Password example
            'unique_field': forms.PasswordInput(render_value=True),

            # Radio buttons
            'foreign_key': forms.RadioSelect(),
        }
        