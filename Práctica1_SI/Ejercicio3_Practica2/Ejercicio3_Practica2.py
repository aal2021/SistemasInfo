import requests


def obtener_ultimas_vulnerabilidades(num_vulnerabilidades=10):
    url = "https://cve.circl.lu/api/last/{}".format(num_vulnerabilidades)
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        for i, vulnerabilidad in enumerate(data):
            print("Vulnerabilidad #{}".format(i + 1))
            print("CVE-ID:", vulnerabilidad["id"])
            # print("Descripción:", vulnerabilidad["summary"])
            # print("Referencia:", vulnerabilidad["references"])
            # print("Publicado:", vulnerabilidad["Published"])
            print()
    else:
        print("Error al obtener las vulnerabilidades:", response.status_code)


obtener_ultimas_vulnerabilidades()
