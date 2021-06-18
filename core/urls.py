from django.conf.urls import url
from django.urls import path, include
from .views import *
urlpatterns = [
	
	path('matches/', getMatches.as_view()),
	path('getscore/',Score_of_match.as_view()),
	path('redirect/',jst_callback),
	path('results/',homeview.as_view()),
	path('searchresults/',get_Searched_Matches.as_view()),
	path('searchredirect/',jst_searchback),
	
	
]