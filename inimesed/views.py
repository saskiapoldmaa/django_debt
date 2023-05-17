from django.shortcuts import render
from django.http import HttpResponse
import matplotlib.pyplot as plt
from io import StringIO
import numpy as np

def index(request):
    return render(request, 'inimesed/index.html')

def volgnevused(request):
    volad = {}
    with open('inimesed/data.txt', 'r') as f:
        for line in f:
            lender, borrower, amount = line.split(',')
            amount = int(amount)
            if lender in volad:
                volad[lender] += amount
            else:
                volad.update({lender: amount})
            if borrower in volad:
                volad[borrower] -= amount
            else:
                volad.update({borrower: -amount})
    tekst = ""
    for inimene in volad:
        if volad[inimene]>0:
            y = inimene+ " on võlgu "+ str(volad[inimene]) + "€. "
            tekst+=str(y)
        elif volad[inimene]<0:
            pos= -volad[inimene]
            y = inimene+ " peab saama "+ str(pos)+"€. "
            tekst += str(y)
    return render(request, 'inimesed/index.html', {"tekst": tekst})

def about(request):
    return render(request, 'about.html')
