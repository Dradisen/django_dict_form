from collections import defaultdict

from django import forms


class JsonFormMixin:
    
    def as_json(self: type[forms.Form]) -> dict[str, dict]:
        attrs = defaultdict(dict)

        for field_name, field_value in self.fields.items():
            choices = getattr(field_value, 'representate_choices', getattr(field_value.widget, 'choices', []))
            attrs[field_name] = dict(
                input=dict(
                    label=field_value.label,
                    label_suffix=field_value.label_suffix,
                    name=field_name,
                    step_size=getattr(field_value, 'step_size', None),
                    widget=dict(
                        name=field_value.widget.__class__,                    
                        is_hidden=field_value.widget.is_hidden,
                        required=field_value.widget.is_required,
                        type=getattr(field_value.widget, 'input_type', None),
                        # value=self.format_value(value),
                        # attrs=self.build_attrs(self.attrs, attrs),
                        attrs=getattr(field_value.widget, 'attrs', None),
                    ),
                    disabled=field_value.disabled,
                    help_text=field_value.help_text,
                    max_length=getattr(field_value, 'max_length', None),
                    min_length=getattr(field_value, 'min_length', None),
                ),
                data=dict(
                    initial=field_value.initial,
                    choices=choices,
                )
            )
        return attrs


class JsonForm(forms.Form, JsonFormMixin): ...
