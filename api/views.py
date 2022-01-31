import os.path

from django.shortcuts import render
from rest_framework import views,response    #importing views and response from rest_framework
from pathlib import Path

import json    #importing json

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# api/v1/algomax/resources?filename=license.json
class Resources(views.APIView):                     #class based view is created for get and post method
                                                     #which is inherited from APIView
    def get(self,request,*args,**kwargs):            # def function is overwrited
        filename=request.query_params["filename"]   #
        # path="algomax\\static\\"+filename
        # api/static
        path="api/static/"+filename            #getting the path


        try:
            with open(path,"r") as file:         #reading the path to get the json file(license.json)
                file=json.load(file)             #loading the json data(license.json)and storing in file variable
                return response.Response({"data":file})  #sending response when get api is called

        except Exception as e:             #except block works if filename is different
            return response.Response({"error":"file not found"})  #sending response as error if filename is different

    def post(self,request,*args,**kwargs):     #post function is overwrited here
        f=open("out.json","a")                 #creating a file out.json if not created and appending data in json
        json.dump(request.data,f)              #writing the data into out.json
        return response.Response({"data":request.data})   #sending response when post api is called








