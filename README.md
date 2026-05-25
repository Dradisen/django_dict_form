
# django-dict-form

django_dict_form is a lightweight extension for Django Forms that adds serialization support through `as_dict()` method.

The package allows developers to convert Django form definitions into structured Python dictionaries or JSON objects, making forms easier to integrate with REST APIs, SPA frontends (React/Vue), dynamic UI generators, and low-code systems.

It extends the standard Django form rendering approach (as_p, as_table, as_ul) by providing machine-readable representations of form fields, metadata, validation rules, and configuration.

## When is this convenient?

If forms are used on the frontend, then by writing adapters to components UI/UX, forms can be automatically generated without the frontend developer having to write the forms themselves. Simply editing them on the backend will be enough to make changes.

This saves time by eliminating the need to manually define forms.

## Features

- Serialize Django forms to Python dictionaries
- Useful for dynamic frontend rendering
- Simplifies API-driven form generation
- Lightweight and framework-friendly
- Compatible with standard Django Forms

Suitable for projects where frontend and backend are separated or where forms need to be described programmatically.

## Example

<!-- ## Development plan
 - Write an adapter for popular UX/UX frameworks, such as (Ant.Design, Radix) for components use autogenerate  form with Django -->