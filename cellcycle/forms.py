from django import forms


class InputData(forms.Form):
    doubling_time = forms.FloatField(
        min_value=0,  # mudar p > 0
        required=True,
        help_text='(in hours)')
    cytokinesis = forms.FloatField(
        min_value=0, max_value=1,
        required=True,
        label='Percentage of cells in cytokinesis')
    mitosis = forms.FloatField(
        min_value=0, max_value=1,
        required=True,
        label='Percentage of cells in mitosis')
    g2edu = forms.FloatField(
        min_value=0,
        required=True,
        label='EdU pulse for G2 phase (in hours)',
        help_text='(in hours)')
    edu = forms.FloatField(
        min_value=0, max_value=1,
        label='Percentage of EdU positive cells')
    edu_time = forms.FloatField(
        min_value=0,
        required=True,
        label='EdU pulse for positive cell counting',
        help_text='(in hours)',
    )


