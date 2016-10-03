from django.shortcuts import render
from django.http import HttpResponse

import json

def home(request):
    return render(request,'newsimple.html')


def compute(request):
    if request.method == 'POST':
        
        final = {}
        principal =int(request.POST['p'])
        rate = int(request.POST['r'])
        time = int(request.POST['t'])
        result = (principal * rate * time)/100

        final['principal'] = principal
        final['rate'] = rate
        final['time']=time
        final['result'] = result 
        
       
        return HttpResponse(
            json.dumps(final),
            content_type="application/json")
    else:
        return HttpResponse(
            json.dumps({"nothing to see":"this isn't happening"}),
                        content_type="application/json")
