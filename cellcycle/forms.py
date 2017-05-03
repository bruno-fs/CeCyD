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
        help_text='h')
    cytokinesis = forms.FloatField(
        min_value=0, max_value=100,
        required=True,
        label='Percentage of cells in cytokinesis',
        help_text='%',
    )
    mitosis = forms.FloatField(
        min_value=0, max_value=100,
        required=True,
        label='Percentage of cells in mitosis',
        help_text='%',
    )
    g2edu_time = forms.FloatField(
        min_value=0,
        required=True,
        label='Minimum time to find 2 nuclei Edu-labeled in the same cell',
        help_text='h')
    edu = forms.FloatField(
        min_value=0, max_value=100,
        label='Percentage of positive cells after Edu pulse',
        help_text='%',
    )
    edu_time = forms.FloatField(
        min_value=0,
        required=True,
        label='Edu pulse duration',
        help_text='h',
    )


