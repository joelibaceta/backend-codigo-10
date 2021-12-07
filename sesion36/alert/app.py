from flask import Flask
from flask import request 
from flask.wrappers import Response

from dotenv import load_dotenv

load_dotenv()

import httpx
import os


app = Flask(__name__)

@app.route('/alert', methods = ['POST'])
async def create_alert():

    header = request.headers["authorization"]
    async with httpx.AsyncClient(headers={
        "authorization": header
    }) as client:
        response = await client.get(os.getenv("AUTH_SERVICE"))

    if response.status_code == 200:
        payload = response.json()

        return f"Alerta enviada por {payload['fullname']}"
    else:
        return Response(status=401)