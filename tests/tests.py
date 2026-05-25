from django.test import TestCase
from django import forms
from django_dict_form.form import DictForm
from django.forms import widgets

"""
TODO: Write tests for this fields

Field [+-]
CharField [+-]
IntegerField [+-]
DateField [+-]
TimeField [+-]
DateTimeField [+-]
DurationField [+-]
RegexField [+-]
EmailField [+-]
FileField [-]
ImageField [-]
URLField [+-]
BooleanField [+-]
NullBooleanField [-]
ChoiceField [+-]
MultipleChoiceField [-]
ComboField [-]
MultiValueField [-]
FloatField [+-]
DecimalField [-]
SplitDateTimeField [-]
GenericIPAddressField [-]
FilePathField [-]
JSONField [-]
SlugField [-]
TypedChoiceField [-]
TypedMultipleChoiceField [-]
UUIDField [+-]

"""

MAX_DIFF = None


def make_data(widget: type[widgets.Widget]):
    return {
        'field': {
            'label': None, 
            'label_suffix': None,
            'disabled': False, 
            'help_text': '', 
            'initial': None,
            'widget': {
                'name': widget.__name__, 
                'is_hidden': False, 
                'required': True, 
                'type': '',
                'choices': [],
                'attrs': {}
            }, 
        }
    }


class BaseTestCase(TestCase):
    
    def setUp(self) -> None:
        self.maxDiff = MAX_DIFF
        return super().setUp()


class BaseFieldTestCase(BaseTestCase):
    
    def test_without_args(self):
        class TestForm(DictForm):
            field = forms.Field()

        form = TestForm()
        result = form.as_dict()
        expect = {
            'field': {
                'label': None, 
                'label_suffix': None,
                'disabled': False, 
                'help_text': '', 
                'initial': None,
                'required': True,
                'show_hidden_initial': False,
                'widget': {
                    'name': 'TextInput', 
                    'is_hidden': False, 
                    'required': True, 
                    'type': 'text',
                    'choices': [],
                    'attrs': {}
                }, 
            }
        }
        self.assertDictEqual(expect, result)
   
    def test_with_all_args(self): 
        class TestForm(DictForm):
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
                'disabled': True, 
                'help_text': 'help text',
                'initial': 1,
                'required': False,
                'show_hidden_initial': True,
                'widget': {
                    'name': 'TextInput', 
                    'is_hidden': False, 
                    'required': False, 
                    'type': 'text',
                    'choices': [],
                    'attrs': {}
                }, 
            }
        }
        
        form = TestForm()
        result = form.as_dict()
        self.assertDictEqual(expect, result)


class CharFieldTestCase(BaseTestCase):
      
    def test_without_args(self):
        class TestForm(DictForm):
            field = forms.CharField()
        expect = {
            'field': {
                'label': None,
                'label_suffix': None,
                'disabled': False, 
                'help_text': '',
                'initial': None,
                'required': True,
                'show_hidden_initial': False,
                'widget': {
                    'name': 'TextInput', 
                    'is_hidden': False, 
                    'required': True, 
                    'type': 'text',
                    'choices': [],
                    'attrs': {}
                }, 
            }
        }
        
        form = TestForm()
        result = form.as_dict()
        self.assertDictEqual(expect, result)
   
    def test_with_all_args(self):
        class TestForm(DictForm):
            field = forms.CharField(
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
            'field': {
                'label': 'Some value', 
                'label_suffix': '-',
                'disabled': True, 
                'help_text': 'help text',
                'initial': 1,
                'required': False,
                'show_hidden_initial': True,
                'widget': {
                    'name': 'TextInput', 
                    'is_hidden': False, 
                    'required': False, 
                    'type': 'text',
                    'choices': [],
                    'attrs': {'maxlength': '100', 'minlength': '1'}
                }, 
            }
        }
        
        form = TestForm()
        result = form.as_dict()
        self.assertDictEqual(expect, result)
    

class IntegerFieldTestCase(BaseTestCase):
    
    def test_without_args(self):
        class IntegerDictForm(DictForm):
            field = forms.IntegerField()

        expect = {
            'field': {
                'label': None, 
                'label_suffix': None,
                'disabled': False, 
                'help_text': '',
                'initial': None,
                'required': True,
                'show_hidden_initial': False,
                'widget': {
                    'name': 'NumberInput', 
                    'is_hidden': False, 
                    'required': True, 
                    'type': 'number',
                    'choices': [],
                    'attrs': {}
                }, 
            }
        }
        
        form = IntegerDictForm()
        result = form.as_dict()
        self.assertDictEqual(expect, result)
   
    def test_with_all_args(self):
        class TestForm(DictForm):
            field = forms.IntegerField(
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
            'field': {
                'label': 'Some value', 
                'label_suffix': '-',
                'disabled': True, 
                'help_text': 'help text',
                'initial': 1,
                'required': False,
                'show_hidden_initial': True,
                'widget': {
                    'name': 'NumberInput', 
                    'is_hidden': False, 
                    'required': False, 
                    'type': 'number',
                    'choices': [],
                    'attrs': {'max': 100, 'min': 1}
                }, 
            }
        }
        
        form = TestForm()
        result = form.as_dict()
        self.assertDictEqual(expect, result)
    
    def test_another_widget(self):
        class TestForm(DictForm):
            field = forms.IntegerField(
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
            'field': {
                'label': 'Some value', 
                'label_suffix': '-',
                'disabled': True, 
                'help_text': 'help text',
                'initial': 1,
                'required': False,
                'show_hidden_initial': True,
                'widget': {
                    'name': 'ChoiceWidget', 
                    'is_hidden': False, 
                    'required': False, 
                    'type': None,
                    'choices': [{'name': '2', 'value': '1'},
                                {'name': '3', 'value': '2'}],
                    'attrs': {'class': 'name'}
                }, 
            }
        }
        
        form = TestForm()
        result = form.as_dict()
        self.assertDictEqual(expect, result)


class DateFieldTestCase(BaseTestCase):
    
    def test_without_args(self):
        
        class TestForm(DictForm):
            field = forms.DateField()
    
        form = TestForm()
        result = form.as_dict()
        expect = {
            'field': {
                'label': None,
                'label_suffix': None,
                'disabled': False, 
                'help_text': '',
                'initial': None,
                'required': True,
                'show_hidden_initial': False,
                'widget': {
                    'name': 'DateInput', 
                    'is_hidden': False, 
                    'required': True, 
                    'type': 'text',
                    'choices': [],
                    'attrs': {}
                }, 
            }
        }
        self.assertDictEqual(expect, result)
   
    def test_with_all_args(self):
        
        class TestForm(DictForm):
            field = forms.DateField(
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
            'field': {
                'label': 'Some value', 
                'label_suffix': '-',
                'disabled': True, 
                'help_text': 'help text',
                'initial': 1,
                'required': False,
                'show_hidden_initial': True,
                'widget': {
                    'name': 'DateInput', 
                    'is_hidden': False, 
                    'required': False, 
                    'type': 'text',
                    'choices': [],
                    'attrs': {}
                }, 
            }
        }
        
        form = TestForm()
        result = form.as_dict()
        self.assertDictEqual(expect, result)


class TimeFieldTestCase(BaseTestCase):
    
    def test_without_args(self):
        
        class TestForm(DictForm):
            field = forms.TimeField()
    
        form = TestForm()
        result = form.as_dict()
        expect = {
            'field': {
                'label': None, 
                'label_suffix': None,
                'disabled': False, 
                'help_text': '',
                'initial': None,
                'required': True,
                'show_hidden_initial': False,
                'widget': {
                    'name': 'TimeInput', 
                    'is_hidden': False, 
                    'required': True, 
                    'type': 'text',
                    'choices': [],
                    'attrs': {}
                }, 
            }
        }
        self.assertDictEqual(expect, result)
   
    def test_with_all_args(self):
        
        class TestForm(DictForm):
            field = forms.TimeField(
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
            'field': {
                'label': 'Some value', 
                'label_suffix': '-',
                'disabled': True, 
                'help_text': 'help text',
                'initial': 1,
                'required': False,
                'show_hidden_initial': True,
                'widget': {
                    'name': 'TimeInput', 
                    'is_hidden': False, 
                    'required': False, 
                    'type': 'text',
                    'choices': [],
                    'attrs': {}
                }, 
            }
        }
        
        form = TestForm()
        result = form.as_dict()
        self.assertDictEqual(expect, result)


class DateTimeFieldTestCase(BaseTestCase):
    
    def test_without_args(self):
        
        class TestForm(DictForm):
            field = forms.DateTimeField()
    
        form = TestForm()
        result = form.as_dict()
        expect = {
            'field': {
                'label': None, 
                'label_suffix': None,
                'disabled': False, 
                'help_text': '',
                'initial': None,
                'required': True,
                'show_hidden_initial': False,
                'widget': {
                    'name': 'DateTimeInput', 
                    'is_hidden': False, 
                    'required': True, 
                    'type': 'text',
                    'choices': [],
                    'attrs': {}
                }, 
            }
        }
        self.assertDictEqual(expect, result)
   
    def test_with_all_args(self):
        
        class TestForm(DictForm):
            field = forms.DateTimeField(
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
            'field': {
                'label': 'Some value', 
                'label_suffix': '-',
                'disabled': True, 
                'help_text': 'help text',
                'initial': 1,
                'required': False,
                'show_hidden_initial': True,
                'widget': {
                    'name': 'DateTimeInput', 
                    'is_hidden': False, 
                    'required': False, 
                    'type': 'text',
                    'choices': [],
                    'attrs': {}
                }, 
            }
        }
        
        form = TestForm()
        result = form.as_dict()
        self.assertDictEqual(expect, result)


class DurationFieldTestCase(BaseTestCase):
    
    def test_without_args(self):
        
        class TestForm(DictForm):
            field = forms.DurationField()
    
        form = TestForm()
        result = form.as_dict()
        expect = {
            'field': {
                'label': None,
                'label_suffix': None,
                'disabled': False, 
                'help_text': '',
                'initial': None,
                'required': True,
                'show_hidden_initial': False,
                'widget': {
                    'name': 'TextInput', 
                    'is_hidden': False, 
                    'required': True, 
                    'type': 'text',
                    'choices': [],
                    'attrs': {}
                }, 
            }
        }
        self.assertDictEqual(expect, result)
   
    def test_with_all_args(self):
        
        class TestForm(DictForm):
            field = forms.DurationField(
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
                'disabled': True, 
                'help_text': 'help text',
                'initial': 1,
                'required': False,
                'show_hidden_initial': True,
                'widget': {
                    'name': 'TextInput', 
                    'is_hidden': False, 
                    'required': False, 
                    'type': 'text',
                    'choices': [],
                    'attrs': {}
                }, 
            }
        }
        
        form = TestForm()
        result = form.as_dict()
        self.assertDictEqual(expect, result)


class RegexFieldTestCase(BaseTestCase):
    
    def test_without_args(self):
        
        class TestForm(DictForm):
            field = forms.RegexField(regex=r'/dasd[*]+/')
    
        form = TestForm()
        result = form.as_dict()
        expect = {
            'field': {
                'label': None,
                'label_suffix': None,
                'disabled': False, 
                'help_text': '',
                'initial': None,
                'required': True,
                'show_hidden_initial': False,
                'widget': {
                    'name': 'TextInput', 
                    'is_hidden': False, 
                    'required': True, 
                    'type': 'text',
                    'choices': [],
                    'attrs': {}
                }, 
            }
        }
        self.assertDictEqual(expect, result)
  
      
class EmailFieldTestCase(BaseTestCase):

    def test_without_args(self):

        class TestForm(DictForm):
            field = forms.EmailField()

        form = TestForm()
        result = form.as_dict()

        expect = {
            'field': {
                'label': None,
                'label_suffix': None,
                'disabled': False, 
                'help_text': '',
                'initial': None,
                'required': True,
                'show_hidden_initial': False,
                'widget': {
                    'name': 'EmailInput', 
                    'is_hidden': False, 
                    'required': True, 
                    'type': 'email',
                    'choices': [],
                    'attrs': {'maxlength': '320'}
                }, 
            }
        }
        self.assertDictEqual(expect, result)

    def test_with_all_args(self):

        class TestForm(DictForm):
            field = forms.EmailField(
                max_length=255,
                required=False,
                label='Email',
                label_suffix=':',
                initial='test@example.com',
                help_text='email help',
                disabled=True,
            )

        expect = {
            'field': {
                'label': 'Email',
                'label_suffix': ':',
                'required': False,
                'show_hidden_initial': False,
                'disabled': True,
                'help_text': 'email help',
                'initial': 'test@example.com',
                'widget': {
                    'name': 'EmailInput',
                    'is_hidden': False,
                    'required': False,
                    'type': 'email',
                    'choices': [],
                    'attrs': {'maxlength': '255'}
                },
            }
        }

        form = TestForm()
        result = form.as_dict()

        self.assertDictEqual(expect, result)


class URLFieldTestCase(BaseTestCase):

    def test_without_args(self):

        class TestForm(DictForm):
            field = forms.URLField()

        form = TestForm()
        result = form.as_dict()

        expect = {
            'field': {
                'label': None, 
                'label_suffix': None,
                'disabled': False, 
                'help_text': '',
                'initial': None,
                'required': True,
                'show_hidden_initial': False,
                'widget': {
                    'name': 'URLInput', 
                    'is_hidden': False, 
                    'required': True, 
                    'type': 'url',
                    'choices': [],
                    'attrs': {}
                }, 
            }
        }
        self.assertDictEqual(expect, result)

    def test_with_all_args(self):

        class TestForm(DictForm):
            field = forms.URLField(
                required=False,
                label='Website',
                label_suffix='>',
                initial='https://example.com',
                help_text='url help',
                disabled=True,
            )

        expect = {
            'field': {
                'label': 'Website',
                'label_suffix': '>',
                'disabled': True,
                'help_text': 'url help',
                'initial': 'https://example.com',
                'required': False,
                'show_hidden_initial': False,
                'widget': {
                    'name': 'URLInput',
                    'is_hidden': False,
                    'required': False,
                    'type': 'url',
                    'choices': [],
                    'attrs': {}
                },
            }
        }

        form = TestForm()
        result = form.as_dict()

        self.assertDictEqual(expect, result)


class BooleanFieldTestCase(BaseTestCase):

    def test_without_args(self):

        class TestForm(DictForm):
            field = forms.BooleanField()

        form = TestForm()
        result = form.as_dict()

        expect = {
            'field': {
                'label': None,
                'label_suffix': None,
                'disabled': False,
                'help_text': '',
                'initial': None,
                'required': True,
                'show_hidden_initial': False,
                'widget': {
                    'name': 'CheckboxInput',
                    'is_hidden': False,
                    'required': True,
                    'type': 'checkbox',
                    'choices': [],
                    'attrs': {}
                },
            }
        }

        self.assertDictEqual(expect, result)

    def test_with_all_args(self):

        class TestForm(DictForm):
            field = forms.BooleanField(
                required=False,
                label='Accept',
                label_suffix='?',
                initial=True,
                help_text='checkbox help',
                disabled=True,
            )

        expect = {
            'field': {
                'label': 'Accept',
                'label_suffix': '?',
                'disabled': True,
                'help_text': 'checkbox help',
                'initial': True,
                'required': False,
                'show_hidden_initial': False,
                'widget': {
                    'name': 'CheckboxInput',
                    'is_hidden': False,
                    'required': False,
                    'type': 'checkbox',
                    'choices': [],
                    'attrs': {}
                },
            }
        }

        form = TestForm()
        result = form.as_dict()

        self.assertDictEqual(expect, result)


class ChoiceFieldTestCase(BaseTestCase):

    CHOICES = (
        (1, 'One'),
        (2, 'Two'),
    )

    def test_without_args(self):

        class TestForm(DictForm):
            field = forms.ChoiceField(choices=self.CHOICES)

        form = TestForm()
        result = form.as_dict()

        expect = {
            'field': {
                'label': None,
                'label_suffix': None,
                'disabled': False,
                'help_text': '',
                'initial': None,
                'required': True,
                'show_hidden_initial': False,
                'widget': {
                    'name': 'Select',
                    'is_hidden': False,
                    'required': True,
                    'type': 'select',
                    'choices': [{'name': 'One', 'value': '1'},
                                {'name': 'Two', 'value': '2'}],
                    'attrs': {}
                },
            }
        }

        self.assertDictEqual(expect, result)

    def test_with_all_args(self):

        class TestForm(DictForm):
            field = forms.ChoiceField(
                choices=self.CHOICES,
                required=False,
                label='Select value',
                label_suffix=':',
                initial=1,
                help_text='choice help',
                disabled=True,
            )

        expect = {
            'field': {
                'label': 'Select value',
                'label_suffix': ':',
                'disabled': True,
                'help_text': 'choice help',
                'initial': 1,
                'required': False,
                'show_hidden_initial': False,
                'widget': {
                    'name': 'Select',
                    'is_hidden': False,
                    'required': False,
                    'type': 'select',
                    'choices': [{'name': 'One', 'value': '1'},
                                {'name': 'Two', 'value': '2'}],
                    'attrs': {}
                },
            }
        }

        form = TestForm()
        result = form.as_dict()

        self.assertDictEqual(expect, result)


class FloatFieldTestCase(BaseTestCase):

    def test_without_args(self):

        class TestForm(DictForm):
            field = forms.FloatField()

        form = TestForm()
        result = form.as_dict()

        expect = {
            'field': {
                'label': None,
                'label_suffix': None,
                'disabled': False, 
                'help_text': '',
                'initial': None,
                'required': True,
                'show_hidden_initial': False,
                'widget': {
                    'name': 'NumberInput', 
                    'is_hidden': False, 
                    'required': True, 
                    'type': 'number',
                    'choices': [],
                    'attrs': {'step': 'any'}
                }, 
            }
        }
        self.assertDictEqual(expect, result)

    def test_with_all_args(self):

        class TestForm(DictForm):
            field = forms.FloatField(
                min_value=1.5,
                max_value=99.9,
                required=False,
                label='Float',
                label_suffix=':',
                initial=10.5,
                help_text='float help',
                disabled=True,
            )

        expect = {
            'field': {
                'label': 'Float',
                'label_suffix': ':',
                'disabled': True,
                'help_text': 'float help',
                'initial': 10.5,
                'required': False,
                'show_hidden_initial': False,
                'widget': {
                    'name': 'NumberInput',
                    'is_hidden': False,
                    'required': False,
                    'type': 'number',
                    'choices': [],
                    'attrs': {
                        'min': 1.5,
                        'max': 99.9,
                        'step': 'any',
                    }
                },
            }
        }

        form = TestForm()
        result = form.as_dict()

        self.assertDictEqual(expect, result)


class UUIDFieldTestCase(BaseTestCase):

    def test_without_args(self):

        class TestForm(DictForm):
            field = forms.UUIDField()

        form = TestForm()
        result = form.as_dict()

        expect = {
            'field': {
                'label': None, 
                'label_suffix': None,
                'disabled': False, 
                'help_text': '',
                'initial': None,
                'required': True,
                'show_hidden_initial': False,
                'widget': {
                    'name': 'TextInput', 
                    'is_hidden': False, 
                    'required': True, 
                    'type': 'text',
                    'choices': [],
                    'attrs': {}
                }, 
            }
        }
        self.assertDictEqual(expect, result)

    def test_with_all_args(self):

        class TestForm(DictForm):
            field = forms.UUIDField(
                required=False,
                label='UUID',
                label_suffix=':',
                initial='123e4567-e89b-12d3-a456-426614174000',
                help_text='uuid help',
                disabled=True,
                show_hidden_initial=True
            )

        expect = {
            'field': {
                'label': 'UUID',
                'label_suffix': ':',
                'required': False,
                'disabled': True,
                'help_text': 'uuid help',
                'initial': '123e4567-e89b-12d3-a456-426614174000',
                'show_hidden_initial': True,
                'widget': {
                    'name': 'TextInput',
                    'is_hidden': False,
                    'required': False,
                    'type': 'text',
                    'choices': [],
                    'attrs': {}
                },
            }
        }

        form = TestForm()
        result = form.as_dict()

        self.assertDictEqual(expect, result)