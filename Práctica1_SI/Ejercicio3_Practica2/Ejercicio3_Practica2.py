import requests


def obtener_ultimas_vulnerabilidades(num_vulnerabilidades=10):
    url = "https://cve.circl.lu/api/last/{}".format(num_vulnerabilidades)
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
