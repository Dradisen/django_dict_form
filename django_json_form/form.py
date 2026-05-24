import json

from django import forms


class RenderableDictFormMixin:

    def as_dict(self) -> dict[str, dict]:
        attrs = dict()

        for field_name, field_value in self.fields.items():
            choices = getattr(field_value, 'representate_choices', getattr(field_value.widget, 'choices', []))
            attrs[field_name] = dict(
                label=field_value.label,
                label_suffix=field_value.label_suffix,
                widget=dict(
                    name=field_value.widget.__class__.__name__,                    
                    is_hidden=field_value.widget.is_hidden,
                    required=field_value.widget.is_required,
                    type=getattr(field_value.widget, 'input_type', None),
                    choices=choices,
                    attrs=getattr(field_value.widget, 'attrs', None),
                ),
                disabled=field_value.disabled,
                help_text=field_value.help_text,
                initial=field_value.initial
            )
        return attrs


class DictForm(forms.Form, RenderableDictFormMixin): ...
