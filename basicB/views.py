from django.shortcuts import render
from basicB.datas import *
import random

# Create your views here.
def basicB_template(request):
    return render(request,"basicB.html")


def basicB_form_show(request):
    return render(request,"basicBresult.html")

def basicB_form_show2(request):
    return render(request,"basicBresult2.html")


def basicB_form(request):

    S1=A6()
    S2=A7()
    S3=A8()
    S4=A9()
    S5=A10()
    S11=A16()
    S12=A17()
    S13=A18()
    S14=A19()
    S15=A20()
    groupA=[S1,S2,S3,S4,S5,S11,S12,S13,S14,S15]
    random.shuffle(groupA)

    A1_result=groupA[0]
    A2_result=groupA[1]
    A3_result=groupA[2]
    A4_result=groupA[3]
    A5_result=groupA[4]
    A6_result=groupA[5]
    A7_result=groupA[6]
    A8_result=groupA[7]
    A9_result=groupA[8]
    A10_result=groupA[9]



    payload={
        'A1_result':A1_result,
        'A2_result':A2_result,
        'A3_result':A3_result,
        'A4_result':A4_result,
        'A5_result':A5_result,
        "A6_result":A6_result,
        "A7_result":A7_result,
        "A8_result":A8_result,
        "A9_result":A9_result,
        "A10_result":A10_result,
        }

    return render(request,'basicBresult.html',payload)


def basicB_form2(request):

    S1=A1()
    S2=A2()
    S3=A3()
    S4=A4()
    S5=A5()
    S11=A11()
    S12=A12()
    S13=A13()
    S14=A14()
    S15=A15()
    groupA=[S1,S2,S3,S4,S5,S11,S12,S13,S14,S15]
    random.shuffle(groupA)



    A1_result=groupA[0]
    A2_result=groupA[1]
    A3_result=groupA[2]
    A4_result=groupA[3]
    A5_result=groupA[4]
    A6_result=groupA[5]
    A7_result=groupA[6]
    A8_result=groupA[7]
    A9_result=groupA[8]
    A10_result=groupA[9]



    payload={
        'A1_result':A1_result,
        'A2_result':A2_result,
        'A3_result':A3_result,
        'A4_result':A4_result,
        'A5_result':A5_result,
        "A6_result":A6_result,
        "A7_result":A7_result,
        "A8_result":A8_result,
        "A9_result":A9_result,
        "A10_result":A10_result,
        }

    return render(request,'basicBresult2.html',payload)

# Create your views here.
