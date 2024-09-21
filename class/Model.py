import requests
import json

class Model:
    def __init__(self, urlBase):
        self.urlBase = urlBase

    def getDadosApi(self, endpoint):
        url = self.urlBase + endpoint
        return requests.get(url)

    def setDadosApi(self, endpoint, data):
        url = self.urlBase + endpoint
        headers = {
            'Content-Type': 'application/vnd.api+json',
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 201:
            return True
        else:
            return False


    def getNovoId(self, endpoint):
        url = self.urlBase + endpoint
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            qtd = len(data)
            return qtd+1
        else:
            print(f"Erro ao consultar o servidor: {response.status_code}")

        # response = requests.get(url)

        # if response.status_code == 200:
        #     data = response.json()
        #     print(data[0]['title'])
        # else:
        #     print(f"Erro ao consultar o servidor: {response.status_code}")