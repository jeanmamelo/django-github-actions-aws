from django.http import HttpResponse

def home(request):
   text = """<h1>Amazing page!!!</h1>"""
   return HttpResponse(text)
