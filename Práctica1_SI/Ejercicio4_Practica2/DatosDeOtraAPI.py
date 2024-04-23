import requests

# Definir los parámetros de la consulta
url = "https://newsapi.org/v2/everything"
query = "ciberseguridad"
api_key = "6e16ba390f2f4d77b7f1950231a07780"  # Nuestra API Key

# Realizar la consulta a la API
response = requests.get(url, params={"q": query, "apiKey": api_key})

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir la respuesta a formato JSON
    data = response.json()

    # Contador para llevar un seguimiento de los artículos mostrados
    count = 0

    # Mostrar los detalles de cada artículo que contiene "ciberseguridad" en el título o la descripción
    for article in data["articles"]:
        title = article["title"].lower()
        description = article["description"].lower()

        # Verificar si la palabra "ciberseguridad" está en el título o la descripción
        if "ciberseguridad" in title or "ciberseguridad" in description:
            source = article["source"]["name"]
            title = article["title"]
            author = article.get("author", "Autor desconocido")
            description = article["description"]
            published_at = article["publishedAt"]
            url = article["url"]

            # Mostrar los detalles del artículo
            print("Fuente:", source)
            print("Título:", title)
            print("Autor:", author)
            print("Descripción:", description)
            print("Fecha de publicación:", published_at)
            print("URL:", url)
            print("-" * 50)  # Separador entre artículos

            # Incrementar el contador
            count += 1

            # Verificar si ya se han mostrado 10 artículos
            if count >= 10:
                break
else:
    print("Error al realizar la solicitud:", response.status_code)
