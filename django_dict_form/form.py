from django import forms
from django.forms import Widget
from typing import Iterable


def extract_choices(choices: Iterable[tuple]) -> list[dict]:
    return [{"value": str(key), "name": value} for key, value in choices]


def _widget_as_dict(widget: Widget) -> dict:
    return {
        "name": widget.__class__.__name__,
        "is_hidden": widget.is_hidden,
        "required": widget.is_required,
        "type": getattr(widget, "input_type", None),
        "choices": extract_choices(getattr(widget, "choices", [])),
        "attrs": getattr(widget, "attrs", None),
    }


class RenderableDictFormMixin:
    fields: dict

    def as_dict(self) -> dict[str, dict]:
        return {
            field_name: {
                "label": field.label,
                "label_suffix": field.label_suffix,
                "required": field.required,
                "disabled": field.disabled,
                "help_text": field.help_text,
                "initial": field.initial,
                "show_hidden_initial": field.show_hidden_initial,
                "widget": _widget_as_dict(field.widget),
            }
            for field_name, field in self.fields.items()
        }


class DictForm(forms.Form, RenderableDictFormMixin): ...
