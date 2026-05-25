# django-dict-form

[![PyPI](https://img.shields.io/pypi/v/django-dict-form.svg?label=PyPI)](https://pypi.org/project/django-deploy-probes/)
[![Django Packages](https://img.shields.io/badge/Django%20Packages-django--dict--form-0c4b33.svg)](https://djangopackages.org/packages/p/django_dict_form/)
[![Python](https://img.shields.io/badge/python-%3E%3D3.11-3776AB.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-%3E%3D3.2-0C4B33.svg)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
<!-- [![uv](https://img.shields.io/badge/package%20manager-uv-5C3EE8.svg)](https://docs.astral.sh/uv/) -->

Lightweight Django Forms extension. Adds `as_dict()` — serializes form definitions to Python dicts / JSON, making forms easier to integrate with REST APIs, SPA frontends (React/Vue), dynamic UI generators, and low-code systems.

Extends standard Django form rendering (`as_p`, `as_table`, `as_ul`) with machine-readable field metadata, validation rules, and widget configuration.

## When is this convenient?

Write adapters to UI/UX components once — forms auto-generate on frontend. Backend edits propagate automatically. No manual frontend form duplication.

## Features

- Serialize Django forms to Python dictionaries
- Useful for dynamic frontend rendering
- Simplifies API-driven form generation
- Lightweight and framework-friendly
- Compatible with standard Django Forms

## Install

```bash
pip install django-dict-form
```

## Quick Start

```python
from django_dict_form import DictForm
from django import forms

class ContactForm(DictForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

form = ContactForm()
data = form.as_dict()
```

Output:

```json
{
  "name": {
    "label": null,
    "required": true,
    "disabled": false,
    "help_text": "",
    "initial": null,
    "show_hidden_initial": false,
    "label_suffix": null,
    "widget": {
      "name": "TextInput",
      "type": "text",
      "is_hidden": false,
      "required": true,
      "choices": [],
      "attrs": {"maxlength": "100"}
    }
  }
}
```

## Mixin Usage

Use `RenderableDictFormMixin` to add `as_dict()` to any existing form class:

```python
from django_dict_form.form import RenderableDictFormMixin
from django import forms

class MyForm(forms.Form, RenderableDictFormMixin):
    field = forms.CharField()
```

## `as_dict()` Output Schema

Each field produces:

| Key | Type | Description |
|-----|------|-------------|
| `label` | `str \| null` | Field label |
| `label_suffix` | `str \| null` | Label suffix |
| `required` | `bool` | Whether field is required |
| `disabled` | `bool` | Whether field is disabled |
| `help_text` | `str` | Help text |
| `initial` | `any` | Default value |
| `show_hidden_initial` | `bool` | Show hidden initial widget |
| `widget` | `dict` | Widget metadata (see below) |

Widget dict:

| Key | Type | Description |
|-----|------|-------------|
| `name` | `str` | Widget class name (e.g. `TextInput`) |
| `type` | `str \| null` | HTML input type (e.g. `text`, `email`, `number`) |
| `is_hidden` | `bool` | Whether widget is hidden |
| `required` | `bool` | Widget-level required |
| `choices` | `list[{value, name}]` | Options for select widgets |
| `attrs` | `dict` | HTML attributes (e.g. `maxlength`, `min`, `max`) |

## Supported Fields

| Field | Widget | Notes |
|-------|--------|-------|
| `CharField` | `TextInput` | `maxlength`, `minlength` in attrs |
| `IntegerField` | `NumberInput` | `min`, `max` in attrs |
| `FloatField` | `NumberInput` | `step: any` in attrs |
| `EmailField` | `EmailInput` | `maxlength: 320` default |
| `URLField` | `URLInput` | |
| `BooleanField` | `CheckboxInput` | |
| `ChoiceField` | `Select` | choices serialized |
| `DateField` | `DateInput` | |
| `TimeField` | `TimeInput` | |
| `DateTimeField` | `DateTimeInput` | |
| `DurationField` | `TextInput` | |
| `RegexField` | `TextInput` | |
| `UUIDField` | `TextInput` | |

Custom widgets supported — pass any widget instance, choices and attrs extracted automatically.

## Requirements

- Python >= 3.11.15
- Django >= 3.2

## License

MIT — [Gleb Uvarov](https://github.com/Dradisen)
