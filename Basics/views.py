from django.shortcuts import render

# Create your views here.
def calculator(request):
    result=""
    if request.method =='POST':
        a=int(request.POST.get('txt_number1'))
        b=int(request.POST.get('txt_number2'))
        btn=request.POST.get('btnsubmit')
        if btn =='+':
            result=a+b
        elif btn=='-':
            result=a-b
        elif btn=='*':
            result=a*b
        elif btn=='/':
            result=a/b
        return render(request,'Basics/Calculator.html',{'result':result})
    else:
        return render(request,'Basics/Calculator.html')


def largesmall(request):
    if request.method=='POST':
        a=int(request.POST.get('txtnum1'))
        b=int(request.POST.get('txtnum2'))
        c=int(request.POST.get('txtnum3'))
    
        if a > b and a > c:
            largest = a
        elif b > c:
                largest = b
        else:
                largest = c

        if a < b and a < c:
                smallest = a
        elif b < c:
                smallest = b
        else:
            smallest = c


    
        return render(request,'Basics/smallestlargest.html',{'largest':largest,'smallest':smallest})
    else:
        return render(request,'Basics/smallestlargest.html')