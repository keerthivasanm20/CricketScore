from datetime import datetime, timedelta
from django.conf import settings
from django.contrib import auth
from django.http import HttpResponse

class AutoLogout():
  def __init__(self, get_response):
        self.get_response = get_response

  def __call__(self, request):
        return self.get_response(request)

  def process_exception(self, request, exception): 
        
    try:
      if datetime.now() - request.session['list_value'] > timedelta( 0, settings.AUTO_LOGOUT_DELAY * 60, 0):
        auth.logout(request)
        del request.session['list_value']
      if datetime.now() - request.session['matches'] > timedelta( 0, settings.AUTO_LOGOUT_DELAY * 60, 0):
        auth.logout(request)
        del request.session['matches']
        return HttpResponse("in Sucess")

    except KeyError:
          pass
    request.session['list_value'] = datetime.now()
    request.session['matches'] = datetime.now()
    return HttpResponse("in exception")