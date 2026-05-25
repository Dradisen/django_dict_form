from django.forms import Widget

from dataclasses import dataclass

@dataclass
class MetaFieldJson:
    widget: Widget
    required: bool
    disabled: bool
    help_text: str
    max_length: int|None
    min_length: int|None
    choices: list[dict]
    label: str
    type: str
    name: str
    attrs: dict