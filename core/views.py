from django.shortcuts import render,redirect
from requests import Request,post
from rest_framework.views import APIView
from rest_framework.response import Response 
from requests import post,put,get
from rest_framework import status
from datetime import *
import requests

BASE_URL='https://cricapi.com/api/'
apiKey='zWu7HryWSjdwlNwqqxgYbTmYTCy1'
# Create your views here.
class getMatches(APIView):
  def get(self,request):
    
    if 'matches' not in request.session: 
        if not self.request.session.exists(request.session.session_key):
              self.request.session.create()
        
        endpoint='matches/'
        headers={'Content-Type': 'application/json', 'apikey':apiKey }
      

        response = get(BASE_URL + endpoint, {},headers=headers)
        today=date.today()
        
        try:
            response= response.json()
        except:
            return Response({"guess":"error"},status=status.HTTP_200_OK) 
            
        l=[]
        re={}
        today=datetime.today()
            # nextday=datetime.today() + timedelta(days=1)
            # print(type(nextday))
        for i in range(0,80):
                 d={} 
                 d['team-1']=response['matches'][i]['team-1']
                 
                 d['team-2']=response['matches'][i]['team-2']
                 d['unique_id']=response['matches'][i]['unique_id']
                 date_unformat=response['matches'][i]['date']
                 
                 match_day=date_unformat.replace("T00:00:00.000Z", "")
                 date_dt3 = datetime.strptime(match_day, '%Y-%m-%d')
                 
                 if(today.date()  <= date_dt3.date() ):
                 
                    d['date']=match_day
                    l.append(d)
 
        re={"matches":l}
        self.request.session['matches']=re
    
    return Response(self.request.session['matches'],status=status.HTTP_200_OK)
       
      
      

def jst_callback(request,format=None):

            unique_id=request.POST.get('unique')
            print(unique_id)
            return redirect('/score/'+unique_id)

def jst_searchback(request,format=None):

            unique_id=request.GET['team']
            print("tem"+unique_id)
            return redirect('/results/'+unique_id)

class Score_of_match(APIView):
        lookup_url_kwarg = 'code' 
        def get(self,request):
            id= request.GET.get(self.lookup_url_kwarg)
            endpoint='cricketScore/'
           
           
            print(type(id))
            response=requests.get('http://cricapi.com/api/cricketScore?unique_id='+id+'&apikey=zWu7HryWSjdwlNwqqxgYbTmYTCy1')
            
            try:
                response=response.json()
                return Response(response,status=status.HTTP_200_OK)
            except:
                return Response({"guess":"error"},status=status.HTTP_200_OK)
         
         

class homeview(APIView):
      
    def get(self,request):
        
        if not self.request.session.exists(request.session.session_key):
           self.request.session.create()
           
           endpoint='matches/'
           headers={'Content-Type': 'application/json', 'apikey':apiKey }
           response = get(BASE_URL + endpoint, {},headers=headers)
           today=date.today()
           l=[]
           if response !=None:
             response= response.json()
             today=datetime.today()
             for i in range(0,len(response['matches'])):
                 date_unformat=response['matches'][i]['date']
                 match_day=date_unformat.replace("T00:00:00.000Z", "")
                 date_dt3 = datetime.strptime(match_day, '%Y-%m-%d')
                 if(((today.date() - timedelta(days=1)) == date_dt3.date() or today.date() == date_dt3.date()) and (response['matches'][i]['matchStarted']) ):
                                l.append(str(response['matches'][i]['unique_id']))
           
           self.request.session['list_value']=l 
          
     
        l=self.request.session['list_value']
        res={}
        z=[]
        l[0]='1249875'
        for i in range(0,len(l)):
               response=requests.get('http://cricapi.com/api/cricketScore?unique_id='+l[i]+'&apikey=zWu7HryWSjdwlNwqqxgYbTmYTCy1')
               if response != None:
                  response=response.json()
                  
                  if "score"  in response.keys():
                       z.append(response["score"])

        res['det']=z
        print(res)       
           
        
        
              
           
        return Response(res,status=status.HTTP_200_OK) 
         
class get_Searched_Matches(APIView):
  lookup_url_kwarg = 'team'
  def get(self,request):
        team= request.GET.get(self.lookup_url_kwarg)
        print(team)
        if not self.request.session.exists(request.session.session_key):
            self.request.session.create()
        endpoint='matches/'
        headers={'Content-Type': 'application/json', 'apikey':apiKey }
     
        response = get(BASE_URL + endpoint, {},headers=headers)
        today=date.today()
        
        try:
            response= response.json()
        except:
            return Response({"guess":"error"},status=status.HTTP_200_OK) 
            
        l=[]
        re={}
        today=datetime.today()
            # nextday=datetime.today() + timedelta(days=1)
            # print(type(nextday))
        if response !=None:
            for i in range(0,len(response['matches'])):
                 d={} 
                 d['team-1']=response['matches'][i]['team-1']
                  
                 d['team-2']=response['matches'][i]['team-2']
                 d['team-2'].replace(" ", "")
                 d['team-1'].replace(" ", "")
                 print(d['team-2'])
                 if team.lower() in (d['team-1']).lower() or team.lower() == (d['team-2']).lower() :
                    d['unique_id']=response['matches'][i]['unique_id']
                    date_unformat=response['matches'][i]['date']
                 
                    match_day=date_unformat.replace("T00:00:00.000Z", "")
                    date_dt3 = datetime.strptime(match_day, '%Y-%m-%d')
                 
                    
                 
                    d['date']=match_day
                    l.append(d)
            
            
            print("team ",l)
            re={"matches":l}
            

        return Response(re,status=status.HTTP_200_OK)