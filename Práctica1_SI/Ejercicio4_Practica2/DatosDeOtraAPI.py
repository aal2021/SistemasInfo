import requests

def noticasOtraAPI():

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

        # Lista para almacenar los detalles de las noticias recientes
        articles = []

        # Ordenar las noticias por fecha de publicación en orden descendente
        sorted_articles = sorted(data["articles"], key=lambda x: x["publishedAt"], reverse=True)

        # Mostrar los detalles de cada artículo que contiene "ciberseguridad" en el título o la descripción
        for article in sorted_articles:
            title = article["title"]
            description = article["description"]

            # Verificar si la palabra "ciberseguridad" está en el título o la descripción
            if "ciberseguridad" or "Ciberseguridad" in title or "ciberseguridad" or "Ciberseguridad "in description:
                source = article["source"]["name"]
                title = article["title"]
                author = article.get("author", "Autor desconocido")
                description = article["description"]
                published_at = article["publishedAt"]
                url = article["url"]

                # Agregar los detalles del artículo a la lista
                articles.append({
                    "title": title,
                    "source": source,
                    "author": author,
                    "description": description,
                    "published_at": published_at,
                    "url": url
                })

                # Incrementar el contador
                count += 1

                # Verificar si ya se han mostrado 10 artículos
                if count >= 10:
                    return articles

    else:
        print("Error al realizar la solicitud:", response.status_code)
        return []

