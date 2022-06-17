from django import forms
class DatePicker(forms.widgets.DateInput):
    template_name = 'employee/widgets/datepicker.html'