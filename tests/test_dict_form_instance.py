import datetime

from django.contrib.auth.models import Group, User
from django.test import TestCase

from django_dict_form.form import RenderableDictFormMixin

from .forms import AllFieldTypesForm
from .models import AllFieldTypesModel


class AllFieldTypesDictForm(AllFieldTypesForm, RenderableDictFormMixin):
    pass


EXPECTED_WIDGETS = {
    'char_field': ('TextInput', 'text'),
    'text_field': ('Textarea', None),
    'email_field': ('EmailInput', 'email'),
    'url_field': ('URLInput', 'url'),
    'slug_field': ('TextInput', 'text'),
    'integer_field': ('NumberInput', 'number'),
    'float_field': ('NumberInput', 'number'),
    'decimal_field': ('NumberInput', 'number'),
    'boolean_field': ('CheckboxInput', 'checkbox'),
    'date_field': ('DateInput', 'date'),
    'time_field': ('TimeInput', 'time'),
    'datetime_field': ('DateTimeInput', 'datetime-local'),
    'file_field': ('ClearableFileInput', 'file'),
    'image_field': ('ClearableFileInput', 'file'),
    'json_field': ('Textarea', None),
    'choices_field': ('Select', 'select'),
    'many_to_many': ('SelectMultiple', 'select'),
    'unique_field': ('PasswordInput', 'password'),
    'foreign_key': ('RadioSelect', 'radio'),
}

FIELD_KEYS = {'label', 'label_suffix', 'required', 'disabled', 'help_text', 'initial', 'show_hidden_initial', 'widget'}
WIDGET_KEYS = {'name', 'type', 'is_hidden', 'required', 'choices', 'attrs'}


class AllFieldTypesDictFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_fk = User.objects.create_user(username='fk_user', password='pass')
        cls.user_o2o = User.objects.create_user(username='o2o_user', password='pass')
        cls.group = Group.objects.create(name='test_group')
        cls.instance = AllFieldTypesModel.objects.create(
            char_field='Test Char',
            text_field='Test text content',
            slug_field='test-slug',
            email_field='test@example.com',
            url_field='http://example.com',
            generic_ip='192.168.1.1',
            regex_field='abc123',
            integer_field=42,
            positive_integer=1,
            positive_small_integer=5,
            small_integer=-1,
            big_integer=1_000_000,
            float_field=3.14,
            decimal_field='99.99',
            boolean_field=True,
            date_field=datetime.date(2024, 1, 15),
            time_field=datetime.time(10, 30),
            datetime_field=datetime.datetime(2024, 1, 15, 10, 30),
            duration_field=datetime.timedelta(hours=2),
            file_field='files/sample.txt',
            image_field='images/sample.png',
            json_field={'key': 'value'},
            foreign_key=cls.user_fk,
            one_to_one=cls.user_o2o,
            choices_field='draft',
            nullable_field=None,
            indexed_field='indexed_val',
            unique_field='unique_val',
            validated_integer=50,
            self_relation=None,
        )
        cls.instance.many_to_many.set([cls.group])

    def _form(self):
        return AllFieldTypesDictForm(instance=self.instance)

    def test_as_dict_returns_dict(self):
        result = self._form().as_dict()
        self.assertIsInstance(result, dict)
        self.assertGreater(len(result), 0)

    def test_all_form_fields_present(self):
        form = self._form()
        result = form.as_dict()
        for field_name in form.fields:
            with self.subTest(field=field_name):
                self.assertIn(field_name, result)

    def test_no_extra_keys(self):
        form = self._form()
        result = form.as_dict()
        self.assertEqual(set(result.keys()), set(form.fields.keys()))

    def test_field_structure(self):
        result = self._form().as_dict()
        for field_name, field_data in result.items():
            with self.subTest(field=field_name):
                self.assertEqual(set(field_data.keys()), FIELD_KEYS)

    def test_widget_structure(self):
        result = self._form().as_dict()
        for field_name, field_data in result.items():
            with self.subTest(field=field_name):
                self.assertEqual(set(field_data['widget'].keys()), WIDGET_KEYS)

    def test_widget_names_and_types(self):
        result = self._form().as_dict()
        for field_name, (expected_widget, expected_type) in EXPECTED_WIDGETS.items():
            if field_name not in result:
                continue
            with self.subTest(field=field_name):
                widget = result[field_name]['widget']
                self.assertEqual(widget['name'], expected_widget)
                self.assertEqual(widget['type'], expected_type)

    def test_choices_field_has_choices(self):
        result = self._form().as_dict()
        choices = result['choices_field']['widget']['choices']
        self.assertIsInstance(choices, list)
        self.assertTrue(len(choices) > 0)
        choice_values = [c['value'] for c in choices]
        self.assertIn('draft', choice_values)
        self.assertIn('published', choice_values)
        self.assertIn('archived', choice_values)

    def test_foreign_key_has_choices(self):
        result = self._form().as_dict()
        choices = result['foreign_key']['widget']['choices']
        self.assertIsInstance(choices, list)
        self.assertTrue(len(choices) > 0)

    def test_many_to_many_has_choices(self):
        result = self._form().as_dict()
        choices = result['many_to_many']['widget']['choices']
        self.assertIsInstance(choices, list)
        self.assertTrue(len(choices) > 0)

    def test_required_fields(self):
        result = self._form().as_dict()
        self.assertTrue(result['char_field']['required'])
        self.assertFalse(result['nullable_field']['required'])

    def test_help_text(self):
        result = self._form().as_dict()
        self.assertIsInstance(result['char_field']['help_text'], str)

    def test_boolean_is_not_required(self):
        # CheckboxInput fields are typically not required in ModelForms
        result = self._form().as_dict()
        self.assertFalse(result['boolean_field']['required'])
