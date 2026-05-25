import django
import tempfile

from django.test import TestCase
from django import forms

from django_dict_form.form import DictForm


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


def make_field(field_instance):
    form_class = type('TestForm', (DictForm,), {'field': field_instance})
    return form_class().as_dict()


def field_expect(widget_name, widget_type, widget_attrs=None, widget_choices=None, **field_kwargs):
    field = dict(
        label=None, label_suffix=None, required=True, disabled=False,
        help_text='', initial=None, show_hidden_initial=False,
    )
    field.update(field_kwargs)
    return {
        'field': {
            **field,
            'widget': {
                'name': widget_name,
                'is_hidden': False,
                'required': field['required'],
                'type': widget_type,
                'choices': widget_choices or [],
                'attrs': widget_attrs or {},
            },
        }
    }


class BaseTestCase(TestCase):
    maxDiff = None


class FieldTestCase(BaseTestCase):

    def test_defaults(self):
        result = make_field(forms.Field())
        self.assertDictEqual(field_expect('TextInput', 'text'), result)

    def test_all_args(self):
        result = make_field(forms.Field(
            required=False, label='Some value', label_suffix='-',
            initial=1, help_text='help text', show_hidden_initial=True, disabled=True,
        ))
        expect = field_expect(
            'TextInput', 'text',
            required=False, label='Some value', label_suffix='-',
            initial=1, help_text='help text', show_hidden_initial=True, disabled=True,
        )
        self.assertDictEqual(expect, result)


class CharFieldTestCase(BaseTestCase):

    def test_defaults(self):
        result = make_field(forms.CharField())
        self.assertDictEqual(field_expect('TextInput', 'text'), result)

    def test_all_args(self):
        result = make_field(forms.CharField(
            min_length=1, max_length=100, required=False, label='Some value',
            label_suffix='-', initial=1, help_text='help text',
            show_hidden_initial=True, disabled=True,
        ))
        expect = field_expect(
            'TextInput', 'text',
            widget_attrs={'maxlength': '100', 'minlength': '1'},
            required=False, label='Some value', label_suffix='-',
            initial=1, help_text='help text', show_hidden_initial=True, disabled=True,
        )
        self.assertDictEqual(expect, result)


class IntegerFieldTestCase(BaseTestCase):

    def test_defaults(self):
        result = make_field(forms.IntegerField())
        self.assertDictEqual(field_expect('NumberInput', 'number'), result)

    def test_all_args(self):
        result = make_field(forms.IntegerField(
            max_value=100, min_value=1, required=False, label='Some value',
            label_suffix='-', initial=1, help_text='help text',
            show_hidden_initial=True, disabled=True,
        ))
        expect = field_expect(
            'NumberInput', 'number',
            widget_attrs={'max': 100, 'min': 1},
            required=False, label='Some value', label_suffix='-',
            initial=1, help_text='help text', show_hidden_initial=True, disabled=True,
        )
        self.assertDictEqual(expect, result)

    def test_custom_widget(self):
        result = make_field(forms.IntegerField(
            max_value=100, min_value=1, required=False, label='Some value',
            label_suffix='-', initial=1,
            widget=forms.widgets.ChoiceWidget(choices=[(1, '2'), (2, '3')], attrs={'class': 'name'}),
            help_text='help text', show_hidden_initial=True, disabled=True,
        ))
        expect = field_expect(
            'ChoiceWidget', None,
            widget_attrs={'class': 'name'},
            widget_choices=[{'name': '2', 'value': '1'}, {'name': '3', 'value': '2'}],
            required=False, label='Some value', label_suffix='-',
            initial=1, help_text='help text', show_hidden_initial=True, disabled=True,
        )
        self.assertDictEqual(expect, result)


class DateFieldTestCase(BaseTestCase):

    def test_defaults(self):
        result = make_field(forms.DateField())
        self.assertDictEqual(field_expect('DateInput', 'text'), result)

    def test_all_args(self):
        result = make_field(forms.DateField(
            required=False, label='Some value', label_suffix='-',
            initial=1, help_text='help text', show_hidden_initial=True, disabled=True,
        ))
        expect = field_expect(
            'DateInput', 'text',
            required=False, label='Some value', label_suffix='-',
            initial=1, help_text='help text', show_hidden_initial=True, disabled=True,
        )
        self.assertDictEqual(expect, result)


class TimeFieldTestCase(BaseTestCase):

    def test_defaults(self):
        result = make_field(forms.TimeField())
        self.assertDictEqual(field_expect('TimeInput', 'text'), result)

    def test_all_args(self):
        result = make_field(forms.TimeField(
            required=False, label='Some value', label_suffix='-',
            initial=1, help_text='help text', show_hidden_initial=True, disabled=True,
        ))
        expect = field_expect(
            'TimeInput', 'text',
            required=False, label='Some value', label_suffix='-',
            initial=1, help_text='help text', show_hidden_initial=True, disabled=True,
        )
        self.assertDictEqual(expect, result)


class DateTimeFieldTestCase(BaseTestCase):

    def test_defaults(self):
        result = make_field(forms.DateTimeField())
        self.assertDictEqual(field_expect('DateTimeInput', 'text'), result)

    def test_all_args(self):
        result = make_field(forms.DateTimeField(
            required=False, label='Some value', label_suffix='-',
            initial=1, help_text='help text', show_hidden_initial=True, disabled=True,
        ))
        expect = field_expect(
            'DateTimeInput', 'text',
            required=False, label='Some value', label_suffix='-',
            initial=1, help_text='help text', show_hidden_initial=True, disabled=True,
        )
        self.assertDictEqual(expect, result)


class DurationFieldTestCase(BaseTestCase):

    def test_defaults(self):
        result = make_field(forms.DurationField())
        self.assertDictEqual(field_expect('TextInput', 'text'), result)

    def test_all_args(self):
        result = make_field(forms.DurationField(
            required=False, label='Some value', label_suffix='-',
            initial=1, help_text='help text', show_hidden_initial=True, disabled=True,
        ))
        expect = field_expect(
            'TextInput', 'text',
            required=False, label='Some value', label_suffix='-',
            initial=1, help_text='help text', show_hidden_initial=True, disabled=True,
        )
        self.assertDictEqual(expect, result)


class RegexFieldTestCase(BaseTestCase):

    def test_defaults(self):
        result = make_field(forms.RegexField(regex=r'/dasd[*]+/'))
        self.assertDictEqual(field_expect('TextInput', 'text'), result)


class EmailFieldTestCase(BaseTestCase):

    def test_defaults(self):
        result = make_field(forms.EmailField())
        if django.VERSION >= (4, 0):
            self.assertDictEqual(
                field_expect('EmailInput', 'email', widget_attrs={'maxlength': '320'}),
                result,
            )
        else:
            self.assertDictEqual(
                field_expect('EmailInput', 'email'),
                result,
            )

    def test_all_args(self):
        result = make_field(forms.EmailField(
            max_length=255, required=False, label='Email', label_suffix=':',
            initial='test@example.com', help_text='email help', disabled=True,
        ))
        expect = field_expect(
            'EmailInput', 'email',
            widget_attrs={'maxlength': '255'},
            required=False, label='Email', label_suffix=':',
            initial='test@example.com', help_text='email help', disabled=True,
        )
        self.assertDictEqual(expect, result)


class URLFieldTestCase(BaseTestCase):

    def test_defaults(self):
        result = make_field(forms.URLField())
        self.assertDictEqual(field_expect('URLInput', 'url'), result)

    def test_all_args(self):
        result = make_field(forms.URLField(
            required=False, label='Website', label_suffix='>',
            initial='https://example.com', help_text='url help', disabled=True,
        ))
        expect = field_expect(
            'URLInput', 'url',
            required=False, label='Website', label_suffix='>',
            initial='https://example.com', help_text='url help', disabled=True,
        )
        self.assertDictEqual(expect, result)


class BooleanFieldTestCase(BaseTestCase):

    def test_defaults(self):
        result = make_field(forms.BooleanField())
        self.assertDictEqual(field_expect('CheckboxInput', 'checkbox'), result)

    def test_all_args(self):
        result = make_field(forms.BooleanField(
            required=False, label='Accept', label_suffix='?',
            initial=True, help_text='checkbox help', disabled=True,
        ))
        expect = field_expect(
            'CheckboxInput', 'checkbox',
            required=False, label='Accept', label_suffix='?',
            initial=True, help_text='checkbox help', disabled=True,
        )
        self.assertDictEqual(expect, result)


class ChoiceFieldTestCase(BaseTestCase):

    CHOICES = ((1, 'One'), (2, 'Two'))
    SERIALIZED_CHOICES = [{'name': 'One', 'value': '1'}, {'name': 'Two', 'value': '2'}]

    def test_defaults(self):
        result = make_field(forms.ChoiceField(choices=self.CHOICES))
        self.assertDictEqual(
            field_expect('Select', 'select', widget_choices=self.SERIALIZED_CHOICES),
            result,
        )

    def test_all_args(self):
        result = make_field(forms.ChoiceField(
            choices=self.CHOICES, required=False, label='Select value',
            label_suffix=':', initial=1, help_text='choice help', disabled=True,
        ))
        expect = field_expect(
            'Select', 'select',
            widget_choices=self.SERIALIZED_CHOICES,
            required=False, label='Select value', label_suffix=':',
            initial=1, help_text='choice help', disabled=True,
        )
        self.assertDictEqual(expect, result)


class FloatFieldTestCase(BaseTestCase):

    def test_defaults(self):
        result = make_field(forms.FloatField())
        self.assertDictEqual(
            field_expect('NumberInput', 'number', widget_attrs={'step': 'any'}),
            result,
        )

    def test_all_args(self):
        result = make_field(forms.FloatField(
            min_value=1.5, max_value=99.9, required=False, label='Float',
            label_suffix=':', initial=10.5, help_text='float help', disabled=True,
        ))
        expect = field_expect(
            'NumberInput', 'number',
            widget_attrs={'min': 1.5, 'max': 99.9, 'step': 'any'},
            required=False, label='Float', label_suffix=':',
            initial=10.5, help_text='float help', disabled=True,
        )
        self.assertDictEqual(expect, result)


class UUIDFieldTestCase(BaseTestCase):

    def test_defaults(self):
        result = make_field(forms.UUIDField())
        self.assertDictEqual(field_expect('TextInput', 'text'), result)

    def test_all_args(self):
        result = make_field(forms.UUIDField(
            required=False, label='UUID', label_suffix=':',
            initial='123e4567-e89b-12d3-a456-426614174000',
            help_text='uuid help', disabled=True, show_hidden_initial=True,
        ))
        expect = field_expect(
            'TextInput', 'text',
            required=False, label='UUID', label_suffix=':',
            initial='123e4567-e89b-12d3-a456-426614174000',
            help_text='uuid help', disabled=True, show_hidden_initial=True,
        )
        self.assertDictEqual(expect, result)


class FileFieldTestCase(BaseTestCase):

    def test_defaults(self):
        result = make_field(forms.FileField())
        self.assertDictEqual(field_expect('ClearableFileInput', 'file'), result)

    def test_all_args(self):
        result = make_field(forms.FileField(
            required=False, label='File', label_suffix=':',
            help_text='file help', disabled=True,
        ))
        expect = field_expect(
            'ClearableFileInput', 'file',
            required=False, label='File', label_suffix=':',
            help_text='file help', disabled=True,
        )
        self.assertDictEqual(expect, result)


class ImageFieldTestCase(BaseTestCase):

    def test_defaults(self):
        result = make_field(forms.ImageField())
        self.assertDictEqual(field_expect('ClearableFileInput', 'file', widget_attrs={'accept': 'image/*'}), result)

    def test_all_args(self):
        result = make_field(forms.ImageField(
            required=False, label='Image', label_suffix=':',
            help_text='image help', disabled=True,
        ))
        expect = field_expect(
            'ClearableFileInput', 'file',
            required=False, label='Image', label_suffix=':',
            help_text='image help', disabled=True,
            widget_attrs={'accept': 'image/*'}
        )
        self.assertDictEqual(expect, result)


class MultipleChoiceFieldTestCase(BaseTestCase):

    CHOICES = ((1, 'One'), (2, 'Two'))
    SERIALIZED_CHOICES = [{'name': 'One', 'value': '1'}, {'name': 'Two', 'value': '2'}]

    def test_defaults(self):
        result = make_field(forms.MultipleChoiceField(choices=self.CHOICES))
        self.assertDictEqual(
            field_expect('SelectMultiple', 'select', widget_choices=self.SERIALIZED_CHOICES),
            result,
        )

    def test_all_args(self):
        result = make_field(forms.MultipleChoiceField(
            choices=self.CHOICES, required=False, label='Pick many',
            label_suffix=':', help_text='multi help', disabled=True,
        ))
        expect = field_expect(
            'SelectMultiple', 'select',
            widget_choices=self.SERIALIZED_CHOICES,
            required=False, label='Pick many', label_suffix=':',
            help_text='multi help', disabled=True,
        )
        self.assertDictEqual(expect, result)


class ComboFieldTestCase(BaseTestCase):

    def test_defaults(self):
        result = make_field(forms.ComboField(fields=[forms.CharField(), forms.EmailField()]))
        self.assertDictEqual(field_expect('TextInput', 'text'), result)


class _SimpleMultiField(forms.MultiValueField):
    def compress(self, data_list):
        return ' '.join(data_list) if data_list else ''


class MultiValueFieldTestCase(BaseTestCase):

    def test_defaults(self):
        fields = (forms.CharField(), forms.CharField())
        widget = forms.MultiWidget(widgets=[f.widget for f in fields])
        result = make_field(_SimpleMultiField(fields=fields, widget=widget))
        self.assertDictEqual(field_expect('MultiWidget', None), result)


class DecimalFieldTestCase(BaseTestCase):

    def test_defaults(self):
        result = make_field(forms.DecimalField())
        self.assertDictEqual(
            field_expect('NumberInput', 'number', widget_attrs={'step': 'any'}),
            result,
        )

    def test_with_decimal_places(self):
        result = make_field(forms.DecimalField(max_digits=10, decimal_places=2))
        self.assertDictEqual(
            field_expect('NumberInput', 'number', widget_attrs={'step': '0.01'}),
            result,
        )

    def test_all_args(self):
        result = make_field(forms.DecimalField(
            max_digits=10, decimal_places=2, max_value=100, min_value=1,
            required=False, label='Decimal', label_suffix=':',
            initial='10.50', help_text='decimal help', disabled=True,
        ))
        expect = field_expect(
            'NumberInput', 'number',
            widget_attrs={'step': '0.01', 'max': 100, 'min': 1},
            required=False, label='Decimal', label_suffix=':',
            initial='10.50', help_text='decimal help', disabled=True,
        )
        self.assertDictEqual(expect, result)


class SplitDateTimeFieldTestCase(BaseTestCase):

    def test_defaults(self):
        result = make_field(forms.SplitDateTimeField())
        self.assertDictEqual(field_expect('SplitDateTimeWidget', None), result)

    def test_all_args(self):
        result = make_field(forms.SplitDateTimeField(
            required=False, label='Date+Time', label_suffix=':',
            help_text='split help', disabled=True,
        ))
        expect = field_expect(
            'SplitDateTimeWidget', None,
            required=False, label='Date+Time', label_suffix=':',
            help_text='split help', disabled=True,
        )
        self.assertDictEqual(expect, result)



class GenericIPAddressFieldTestCase(BaseTestCase):

    def test_defaults(self):
        result = make_field(forms.GenericIPAddressField())
        if django.VERSION >= (4, 0):
            self.assertDictEqual(field_expect('TextInput', 'text', widget_attrs={'maxlength': '39'}), result)
        else:
            self.assertDictEqual(field_expect('TextInput', 'text'), result)

    def test_all_args(self):
        result = make_field(forms.GenericIPAddressField(
            required=False, label='IP', label_suffix=':',
            help_text='ip help', disabled=True,
        ))
        
        if django.VERSION >= (4, 0):
            expect = field_expect(
                'TextInput', 'text',
                required=False, label='IP', label_suffix=':',
                help_text='ip help', disabled=True,
                widget_attrs={'maxlength': '39'}
            )
        else:
            expect = field_expect(
                'TextInput', 'text',
                required=False, label='IP', label_suffix=':',
                help_text='ip help', disabled=True,
            )
        self.assertDictEqual(expect, result)


class FilePathFieldTestCase(BaseTestCase):

    def test_defaults(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = make_field(forms.FilePathField(path=tmp))
            self.assertDictEqual(field_expect('Select', 'select'), result)


class JSONFieldTestCase(BaseTestCase):

    def test_defaults(self):
        result = make_field(forms.JSONField())
        self.assertDictEqual(
            field_expect('Textarea', None, widget_attrs={'cols': '40', 'rows': '10'}),
            result,
        )

    def test_all_args(self):
        result = make_field(forms.JSONField(
            required=False, label='JSON', label_suffix=':',
            help_text='json help', disabled=True,
        ))
        expect = field_expect(
            'Textarea', None,
            widget_attrs={'cols': '40', 'rows': '10'},
            required=False, label='JSON', label_suffix=':',
            help_text='json help', disabled=True,
        )
        self.assertDictEqual(expect, result)


class SlugFieldTestCase(BaseTestCase):

    def test_defaults(self):
        result = make_field(forms.SlugField())
        self.assertDictEqual(field_expect('TextInput', 'text'), result)

    def test_all_args(self):
        result = make_field(forms.SlugField(
            required=False, label='Slug', label_suffix=':',
            help_text='slug help', disabled=True,
        ))
        expect = field_expect(
            'TextInput', 'text',
            required=False, label='Slug', label_suffix=':',
            help_text='slug help', disabled=True,
        )
        self.assertDictEqual(expect, result)


class TypedChoiceFieldTestCase(BaseTestCase):

    CHOICES = ((1, 'One'), (2, 'Two'))
    SERIALIZED_CHOICES = [{'name': 'One', 'value': '1'}, {'name': 'Two', 'value': '2'}]

    def test_defaults(self):
        result = make_field(forms.TypedChoiceField(choices=self.CHOICES))
        self.assertDictEqual(
            field_expect('Select', 'select', widget_choices=self.SERIALIZED_CHOICES),
            result,
        )

    def test_all_args(self):
        result = make_field(forms.TypedChoiceField(
            choices=self.CHOICES, coerce=int, required=False,
            label='Typed', label_suffix=':', help_text='typed help', disabled=True,
        ))
        expect = field_expect(
            'Select', 'select',
            widget_choices=self.SERIALIZED_CHOICES,
            required=False, label='Typed', label_suffix=':',
            help_text='typed help', disabled=True,
        )
        self.assertDictEqual(expect, result)


class TypedMultipleChoiceFieldTestCase(BaseTestCase):

    CHOICES = ((1, 'One'), (2, 'Two'))
    SERIALIZED_CHOICES = [{'name': 'One', 'value': '1'}, {'name': 'Two', 'value': '2'}]

    def test_defaults(self):
        result = make_field(forms.TypedMultipleChoiceField(choices=self.CHOICES))
        self.assertDictEqual(
            field_expect('SelectMultiple', 'select', widget_choices=self.SERIALIZED_CHOICES),
            result,
        )

    def test_all_args(self):
        result = make_field(forms.TypedMultipleChoiceField(
            choices=self.CHOICES, coerce=int, required=False,
            label='Typed Multi', label_suffix=':', help_text='typed multi help', disabled=True,
        ))
        expect = field_expect(
            'SelectMultiple', 'select',
            widget_choices=self.SERIALIZED_CHOICES,
            required=False, label='Typed Multi', label_suffix=':',
            help_text='typed multi help', disabled=True,
        )
        self.assertDictEqual(expect, result)
