#!/usr/bin/env python
from math import *
dt = input('Please enter doubling time: ')
c = input('Please enter percentage of cells in cytokinesis (ex: 0.357): ')
while c < 0 or c > 1 :
    c = input ('Please enter a number between 0 and 1 for the percentage of cells in cytokinesis: ')
m = input('Please enter percentage of cells in mitosis (ex: 0.370): ')
while m < 0 or m > 1 :
    m = input ('Please enter a number between 0 and 1 for the percentage of cells in mitosis: ')

g2edu = input('Please enter EdU pulse for G2 phase (in hours): ')
l = input('Please enter percentage of EdU positve cells: ')
while l < 0 or l > 1 :
    l = input ('Please enter a number between 0 and 1 for the percentage of EdU positive cells: ')
edu = input('Please enter time of EdU pulse for positive cell counting (in hours): ')

# dt = 7.25
# c = 0.0357
# m = 0.037
# g2edu = 1
# l = 0.3979
# edu = 1

# Calculos de a
a = log(0.5)/(-dt)
# print 'a: ' + str(a)

# calculo de Xc
y = 1-c
Xg1_m = log(1-y/2)/(-a)
Xc = dt-Xg1_m
Xc_ccu = Xc/dt
# print 'y: ' + str(y)
# print 'Xg1_m: ' + str(Xg1_m)
# print Xc

# calculo de Xm
y2 = 1-(c+m)
Xg1_g2 = log(1-y2/2)/(-a)
Xm = dt-Xg1_g2-Xc
Xm_ccu = Xm/dt
# print 'y2: ' + str(y2)
# print 'Xg1_g2: ' + str(Xg1_g2)
# print 'Xm: ' + str(Xm)

#calculo de G2
Xg2 = g2edu-Xm
Xg2_ccu = Xg2/dt
# print 'Xg2: ' + str(Xg2)

# calculo de S
z = Xg2+Xm+Xc
Xs=(1/a)*log(l+exp(a*z))-(z+edu)
Xs_ccu = Xs/dt
# print 'Xs: ' + str(Xs)

# calculo de G1
Xg1 = dt-(Xc+Xm+Xg2+Xs)
Xg1_ccu = Xg1/dt
# print 'Xg1: ' + str(round(Xg1,3)) + ' h or ' + str(round(Xg1_ccu,3)) + ' ccu'

Xfase = Xc + Xm + Xg2 + Xs + Xg1
Xfase_ccu = Xfase/dt

if Xfase < dt:
    Xg1 = Xg1 + (dt-Xfase)
elif Xfase > dt:
    Xg1 = Xg1 - (Xfase-dt)    

print 'a:   ' + str(a)
print 'Xc:  ' + str(round(Xc,3)) + ' h or ' + str(round(Xc_ccu,3)) + ' ccu'
print 'Xm:  ' + str(round(Xm,3)) + ' h or ' + str(round(Xm_ccu,3)) + ' ccu'
print 'Xg2: ' + str(round(Xg2,3)) + ' h or ' + str(round(Xg2_ccu,3)) + ' ccu'
print 'Xs : ' + str(round(Xs,3)) + ' h or ' + str(round(Xs_ccu,3)) + ' ccu'
print 'Xg1: ' + str(round(Xg1,3)) + ' h or ' + str(round(Xg1_ccu,3)) + ' ccu'