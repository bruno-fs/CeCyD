from __future__ import division

from django.shortcuts import render

from cellcycle.forms import InputData
from cellcycle.cell_cycle import calculate


def home(request):

    if request.method == 'POST':
        form = InputData(request.POST)

        if form.is_valid():
            dt = form.cleaned_data['doubling_time']
            c = form.cleaned_data['cytokinesis']/100
            m = form.cleaned_data['mitosis']/100
            g2edu = form.cleaned_data["g2edu_time"]
            l = form.cleaned_data['edu']/100
            edu = form.cleaned_data['edu_time']

            a, Xc, Xc_ccu, Xm, Xm_ccu, Xg2, Xg2_ccu, Xs, Xs_ccu, Xg1, Xg1_ccu = calculate(dt, c, m, g2edu, l, edu)

            results = dict(a=a, Xc=round(Xc, 3), Xc_ccu=round(Xc_ccu, 3),
                           Xm=round(Xm, 3), Xm_ccu=round(Xm_ccu, 3), Xg2=round(Xg2, 3), Xg2_ccu=round(Xg2_ccu, 3),
                           Xs=round(Xs, 3), Xs_ccu=round(Xs_ccu, 3), Xg1=round(Xg1, 3), Xg1_ccu=round(Xg1_ccu, 3))

            return render(request, 'results.html', results)

    else:
        form = InputData()

    return render(request, 'input_data.html', {'form': form})
