# bmi_calculator
This will help us calculate bmi
Step 1 : Download the repo
Step 2 : run script.sh
Step 3 : go to postman import this collection "https://www.getpostman.com/collections/b8a3ffa1a68c25d49e44" and hit the send
Step 4 (Alternative) : run the below python snippet:

------------------------------------------------------------------
import requests

url = "http://127.0.0.1:8000/bmi/"

payload = "{\r\n   \"bmi_data\":  [{\"Gender\": \"Male\", \"HeightCm\": 171, \"WeightKg\": 96 }, \r\n{ \"Gender\": \"Male\", \"HeightCm\": 161, \"WeightKg\": 85 }, \r\n{ \"Gender\": \"Male\", \"HeightCm\": 180, \"WeightKg\": 77 }, \r\n{ \"Gender\": \"Female\", \"HeightCm\": 166, \"WeightKg\": 62}, \r\n{\"Gender\": \"Female\", \"HeightCm\": 150, \"WeightKg\": 70}, \r\n{\"Gender\": \"Female\", \"HeightCm\": 167, \"WeightKg\": 82}] \r\n}\r\n"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "ca41b24a-e05f-7c5d-d735-6b5d9487bbe5"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

----------------------------------------------------------------------------------------------

Note : "bmi_data" should always be a list of dictonary and inside there can be n number of element
