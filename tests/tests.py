from django.test import TestCase
from django import forms

from django_json_form.form import JsonForm


class BaseFieldTestCase(TestCase):
    
    def setUp(self) -> None:
        self.maxDiff = None
        return super().setUp()
    
    def test_without_args(self):
        
        class TestForm(JsonForm):
            some_field = forms.Field()
    
        form = TestForm()
        result = form.as_json()
        expect = {
            'some_field': {
                'label': None, 
                'label_suffix': None,
                'widget': {
                    'name': 'TextInput', 
                    'is_hidden': False, 
                    'required': True, 
                    'type': 'text',
                    'choices': [],
                    'attrs': {}
                }, 
                'disabled': False, 
                'help_text': '', 
                'initial': None,
            }
        }  
        self.assertDictEqual(expect, result)
   
    def test_with_all_args(self):
        
        class TestForm(JsonForm):
            some_field = forms.Field(
                required=False, 
                label='Some value', 
                label_suffix='-', 
                initial=1,
                # widget=forms.widgets.ChoiceWidget,
                help_text='help text',
                error_messages=[],
                show_hidden_initial=True,
                disabled=True,
            )

        expect = {
            'some_field': {
                'label': 'Some value', 
                'label_suffix': '-',
                'widget': {
                    'name': 'TextInput', 
                    'is_hidden': False, 
                    'required': False, 
                    'type': 'text',
                    'choices': [],
                    'attrs': {}
                }, 
                'disabled': True, 
                'help_text': 'help text',
                'initial': 1,
            }
        }
        
        form = TestForm()
        result = form.as_json()
        self.assertDictEqual(expect, result)


class IntegerFieldTestCase(TestCase):
    
    def setUp(self) -> None:
        self.maxDiff = None
        return super().setUp()
    
    def test_without_args(self):
        class IntegerJsonForm(JsonForm):
            some_field = forms.IntegerField()

        expect = {
            'some_field': {
                'label': None, 
                'label_suffix': None,
                'widget': {
                    'name': 'NumberInput', 
                    'is_hidden': False, 
                    'required': True, 
                    'type': 'number',
                    'choices': [],
                    'attrs': {}
                }, 
                'disabled': False, 
                'help_text': '', 
                'initial': None,
            }
        }
        
        form = IntegerJsonForm()
        result = form.as_json()
        self.assertDictEqual(expect, result)
   
    def test_with_all_args(self):
        class TestForm(JsonForm):
            some_field = forms.IntegerField(
                max_value=100,
                min_value=1,
                required=False, 
                label='Some value', 
                label_suffix='-', 
                initial=1,
                # widget=forms.widgets.ChoiceWidget,
                help_text='help text',
                error_messages=[],
                show_hidden_initial=True,
                # validators=[MinValueValidator(1), MaxValueValidator(100)],
                # localize=
                disabled=True,
                # bound_field_class=
            )

        expect = {
            'some_field': {
                'label': 'Some value', 
                'label_suffix': '-',
                'widget': {
                    'name': 'NumberInput', 
                    'is_hidden': False, 
                    'required': False, 
                    'type': 'number',
                    'choices': [],
                    'attrs': {'max': 100, 'min': 1}
                }, 
                'disabled': True, 
                'help_text': 'help text',
                'initial': 1,
            }
        }
        
        form = TestForm()
        result = form.as_json()
        self.assertDictEqual(expect, result)
        