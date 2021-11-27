from django.shortcuts import render
from django.http import HttpResponse    

# Create your views here.
def say_hello(request):
    return render(request, 'hello.html', {'name':'DHANUSH'})
    #return HttpResponse('Hello Dhanush')
    
    
from django.http import JsonResponse
from django.shortcuts import render

def index(request):
    comments=[
        {'name':'Dhanush',
         'email':'dhanushkv2000@gmail.com'        
         },
         {
          'name':'Vachan',
          'email':'vachan@gmail.com'
         }
    ]

    #context={'comments':comments}

    #return render(request,'hello.html',context)
    
    return JsonResponse({'comments':comments})