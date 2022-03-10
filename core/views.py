from django.http import HttpResponse

def home(request):
   text = """<h1>Hello world!!!</h1>"""
   return HttpResponse(text)
