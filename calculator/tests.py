from django.test import TestCase
from unittest import mock
from calculator.views import CalcuateBMI

class BMItest(TestCase):
    def setUp(self):
        self.input_data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, 
                            { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 }, 
                            { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, 
                            { "Gender": "Female", "HeightCm": 166, "WeightKg": 62}, 
                            {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, 
                            {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}] 

        self.output_data = {
                            "Number of overweights": 1,
                            "bmi data": [
                                {
                                    "Gender": "Male",
                                    "HeightCm": 171,
                                    "WeightKg": 96,
                                    "healthcondtion": "Medium Risk",
                                    "BMI range": "Moderately Obese",
                                    "BMI": "32.83 kg/m^2"
                                },
                                {
                                    "Gender": "Male",
                                    "HeightCm": 161,
                                    "WeightKg": 85,
                                    "healthcondtion": "Medium Risk",
                                    "BMI range": "Moderately Obese",
                                    "BMI": "32.79 kg/m^2"
                                },
                                {
                                    "Gender": "Male",
                                    "HeightCm": 180,
                                    "WeightKg": 77,
                                    "healthcondtion": "Low risk",
                                    "BMI range": "Normal weight",
                                    "BMI": "23.77 kg/m^2"
                                },
                                {
                                    "Gender": "Female",
                                    "HeightCm": 166,
                                    "WeightKg": 62,
                                    "healthcondtion": "Low risk",
                                    "BMI range": "Normal weight",
                                    "BMI": "22.5 kg/m^2"
                                },
                                {
                                    "Gender": "Female",
                                    "HeightCm": 150,
                                    "WeightKg": 70,
                                    "healthcondtion": "Medium Risk",
                                    "BMI range": "Moderately Obese",
                                    "BMI": "31.11 kg/m^2"
                                },
                                {
                                    "Gender": "Female",
                                    "HeightCm": 167,
                                    "WeightKg": 82,
                                    "healthcondtion": "Enhance risk",
                                    "BMI range": "Over weight",
                                    "BMI": "29.4 kg/m^2"
                                }
                            ]
                        }
    
    def test_bmi(self):
        obj = CalcuateBMI().return_bmi(self.input_data)
        self.assertEquals(obj,self.output_data)

