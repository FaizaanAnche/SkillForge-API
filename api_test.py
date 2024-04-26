import requests

url = 'http://localhost:5000/predict'
data = {
    'student_ability': 1,
    'curr_question_diff': 1,
    'ans_status': 0
}

response = requests.post(url, json=data)
print(response.json())
