from django import forms


class BootstrapForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BootstrapForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

        # if self.errors:
        #     for f_name in self.fields:
        #         if f_name in self.errors:
        #             classes = self.fields[f_name].widget.attrs.get('class', '')
        #             classes += ' has-error'
        #             self.fields[f_name].widget.attrs['class'] = classes


class InputData(BootstrapForm):
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


