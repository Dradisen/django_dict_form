from django import forms


def extract_choices(choices) -> list[dict]:
    extracted_choices = list()
    for key, value in list(choices):
        extracted_choices.append(dict(value=str(key), name=value))
    return extracted_choices


class RenderableDictFormMixin:

    def as_dict(self) -> dict[str, dict]:
        attrs = dict()

        for field_name, field_value in self.fields.items():
            choices = extract_choices(getattr(field_value.widget, 'choices', []))
            attrs[field_name] = dict(
                label=field_value.label,
                label_suffix=field_value.label_suffix,
                required=field_value.required,
                disabled=field_value.disabled,
                help_text=field_value.help_text,
                initial=field_value.initial,
                show_hidden_initial=field_value.show_hidden_initial,
                widget=dict(
                    name=field_value.widget.__class__.__name__,                    
                    is_hidden=field_value.widget.is_hidden,
                    required=field_value.widget.is_required,
                    type=getattr(field_value.widget, 'input_type', None),
                    choices=choices,
                    attrs=getattr(field_value.widget, 'attrs', None),
                )
            )
        return attrs


class DictForm(forms.Form, RenderableDictFormMixin): ...
