from django.test import TestCase
from django import forms
from django_json_form.form import JsonForm


"""
TODO: Write tests for this fields

Field [+-]
CharField [+-]
IntegerField [+-]
DateField [+-]
TimeField [+-]
DateTimeField [+-]
DurationField [+-]
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


def make_data():
    return {
        'field': {
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


class BaseTestCase(TestCase):
    
    def setUp(self) -> None:
        self.maxDiff = MAX_DIFF
        return super().setUp()


class BaseFieldTestCase(BaseTestCase):
    
    def test_without_args(self):
        class TestForm(JsonForm):
            field = forms.Field()

        form = TestForm()
        result = form.as_dict()
        expect = make_data()
        self.assertDictEqual(expect, result)
   
    def test_with_all_args(self): 
        class TestForm(JsonForm):
            field = forms.Field(
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
            'field': {
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


class CharFieldTestCase(BaseTestCase):
      
    def test_without_args(self):
        class TestForm(JsonForm):
            some_field = forms.CharField()
        expect = make_data()
        
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
    

class IntegerFieldTestCase(BaseTestCase):
    
    def test_without_args(self):
        class IntegerJsonForm(JsonForm):
            some_field = forms.IntegerField()

        expect = make_data()
        
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


class DateFieldTestCase(BaseTestCase):
    
    def test_without_args(self):
        
        class TestForm(JsonForm):
            some_field = forms.DateField()
    
        form = TestForm()
        result = form.as_dict()
        expect = make_data()
        self.assertDictEqual(expect, result)
   
    def test_with_all_args(self):
        
        class TestForm(JsonForm):
            some_field = forms.DateField(
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
                    'name': 'DateInput', 
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


class TimeFieldTestCase(BaseTestCase):
    
    def test_without_args(self):
        
        class TestForm(JsonForm):
            some_field = forms.TimeField()
    
        form = TestForm()
        result = form.as_dict()
        expect = make_data()
        self.assertDictEqual(expect, result)
   
    def test_with_all_args(self):
        
        class TestForm(JsonForm):
            some_field = forms.TimeField(
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
                    'name': 'TimeInput', 
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


class DateTimeFieldTestCase(BaseTestCase):
    
    def test_without_args(self):
        
        class TestForm(JsonForm):
            some_field = forms.DateTimeField()
    
        form = TestForm()
        result = form.as_dict()
        expect = make_data()
        self.assertDictEqual(expect, result)
   
    def test_with_all_args(self):
        
        class TestForm(JsonForm):
            some_field = forms.DateTimeField(
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
                    'name': 'DateTimeInput', 
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


class DurationFieldTestCase(BaseTestCase):
    
    def test_without_args(self):
        
        class TestForm(JsonForm):
            some_field = forms.DurationField()
    
        form = TestForm()
        result = form.as_dict()
        expect = make_data() 
        self.assertDictEqual(expect, result)
   
    def test_with_all_args(self):
        
        class TestForm(JsonForm):
            some_field = forms.DurationField(
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
