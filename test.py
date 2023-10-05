import json, requests


headers = {'Content-Type': 'application/json'}
scoring_uri ="http://127.0.0.1:8080/infer"


test_data = json.dumps({'prefix': 'pragma solidity', 'max_token': 20})
print('sending the request', '...')
#response = infer(test_data)
response = requests.post(scoring_uri, data=test_data, headers=headers)
print(response)
print('#' * 100)
data = json.loads(response.json())
print(data)