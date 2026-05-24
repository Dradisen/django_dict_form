from django.test import TestCase
from django import forms
from django_json_form.form import JsonForm


"""
TODO: Write tests for this fields

Field [+-]
CharField [+-]
IntegerField [+-]
DateField [-]
TimeField [-]
DateTimeField [-]
DurationField [-]
RegexField [-]
EmailField [-]
FileField [-]
ImageField [-]
URLField [-]
BooleanField [-]
NullBooleanField [-]
ChoiceField [-]
MultipleChoiceField [-]
ComboField [-]
MultiValueField [-]
FloatField [-]
DecimalField [-]
SplitDateTimeField [-]
GenericIPAddressField [-]
FilePathField [-]
JSONField [-]
SlugField [-]
TypedChoiceField [-]
TypedMultipleChoiceField [-]
UUIDField [-]

"""

MAX_DIFF = None



class BaseFieldTestCase(TestCase):
    
    def setUp(self) -> None:
        self.maxDiff = MAX_DIFF
        return super().setUp()
    
    def test_without_args(self):
        
        class TestForm(JsonForm):
            some_field = forms.Field()
    
        form = TestForm()
        result = form.as_dict()
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
        result = form.as_dict()
        self.assertDictEqual(expect, result)


class CharFieldTestCase(TestCase):
      
    def setUp(self) -> None:
        self.maxDiff = MAX_DIFF
        return super().setUp()
    
    def test_without_args(self):
        class TestForm(JsonForm):
            some_field = forms.CharField()

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
        
        form = TestForm()
        result = form.as_dict()
        self.assertDictEqual(expect, result)
   
    def test_with_all_args(self):
        class TestForm(JsonForm):
            some_field = forms.CharField(
                min_length=1,
                max_length=100,
                required=False, 
                label='Some value', 
                label_suffix='-', 
                initial=1,
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
                    'attrs': {'maxlength': '100', 'minlength': '1'}
                }, 
                'disabled': True, 
                'help_text': 'help text',
                'initial': 1,
            }
        }
        
        form = TestForm()
        result = form.as_dict()
        self.assertDictEqual(expect, result)
    

class IntegerFieldTestCase(TestCase):
    
    def setUp(self) -> None:
        self.maxDiff = MAX_DIFF
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
        result = form.as_dict()
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
        result = form.as_dict()
        self.assertDictEqual(expect, result)
    
    def test_another_widget(self):
        class TestForm(JsonForm):
            some_field = forms.IntegerField(
                max_value=100,
                min_value=1,
                required=False, 
                label='Some value', 
                label_suffix='-', 
                initial=1,
                widget=forms.widgets.ChoiceWidget(choices=[(1, '2'), (2, '3')], attrs={'class': 'name'}),
                help_text='help text',
                error_messages=[],
                show_hidden_initial=True,
                # validators=[MinValueValidator(1), MaxValueValidator(100)],
                # localize=
                disabled=True
                # bound_field_class=
            )

        expect = {
            'some_field': {
                'label': 'Some value', 
                'label_suffix': '-',
                'widget': {
                    'name': 'ChoiceWidget', 
                    'is_hidden': False, 
                    'required': False, 
                    'type': None,
                    'choices': [(1, '2'), (2, '3')],
                    'attrs': {'class': 'name'}
                }, 
                'disabled': True, 
                'help_text': 'help text',
                'initial': 1,
            }
        }
        
        form = TestForm()
        result = form.as_dict()
        self.assertDictEqual(expect, result)

