from django.shortcuts import render
from django.http import *
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_bmi(request):
    if request.method == "POST":
        body = json.loads(request.body)
        data = body.get("bmi_data")
        print(data)
        final_respose = CalcuateBMI().return_bmi(data)
        return JsonResponse(final_respose, safe=False)
    return JsonResponse({"error": "invalid data"})

class CalcuateBMI:
    def __init__(self):
        pass

    def return_bmi(self,data):
        final_List = []
        number_of_overweight = 0
        for i in data:
            print("i", i)
            bmi = self.calcualate_bmi(i["WeightKg"],i["HeightCm"])
            condition = self.find_range(bmi)
            # bmi = "{} kg/m^2".format(bmi)
            i.update({"healthcondtion":condition[0], "BMI range":condition[1] , "BMI" : "{} kg/m^2".format(bmi)})
            final_List.append(i)
            if condition[2]:
                number_of_overweight += 1
        output_data = {"Number of overweights": number_of_overweight , "bmi data" : final_List}
        return output_data
        


    def find_range(self,bmi):
        for i in CONST.keys():
            falls_in_range = self.falls_in_range(CONST[i]["range"],bmi)
#             print (i)
            if falls_in_range:
                if i == "Over weight":
                    print (i)
                    return CONST[i]['healthrisk'] , i, True
                else:
                    return CONST[i]['healthrisk'] , i, False


    def falls_in_range(self,range_bmi,value):
        if len(range_bmi) == 2:
            return  min(range_bmi[0], range_bmi[1]) < value < max(range_bmi[0], range_bmi[1])
        else:
            if value > range[0]:
                return True
            else:
                return False
        
    def conver_into_meters(self, cm_data):
        return cm_data/100

    def calcualate_bmi(self,weight , height):
        m_height = self.conver_into_meters(height)
        bmi = weight/m_height**2
        return round(bmi,2)
    

CONST = {
    "Underweight" : {"range":[0, 18.4] , "healthrisk":"malnutririon risk"},
    "Normal weight" : {"range":[18.5,24.9] , "healthrisk":"Low risk"},
    "Over weight" : {"range":[25, 29.9] , "healthrisk":"Enhance risk"},
    "Moderately Obese" : {"range":[30,34.9] , "healthrisk":"Medium Risk"},
    "Severly Obese" : {"range":[35,39.9] , "healthrisk":"Heigh Risk"},
    "Very severly obese" : {"range":[40] , "healthrisk":"Very High risk"}

}
