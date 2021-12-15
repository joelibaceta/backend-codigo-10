import json
import requests

def lambda_handler(event, context):

    headers = event["headers"]
    authorizacion = headers["Authorization"]
    
    response = requests.get("http://198.199.84.117/validate", headers={
        "Authorization": authorizacion
    })
    
    payload = json.loads(response.text)

    if response.status_code == 200:
        return {
            'statusCode': 200,
            'body': f"Alerta enviada por {payload['fullname']}"
        }
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
