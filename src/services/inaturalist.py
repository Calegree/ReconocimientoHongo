import requests
import os

def descargar_imagenes():
    especies = {
        "morchella": "Morchella",
        "gyromitra": "Gyromitra"
    }

    base_dir = "images"
    os.makedirs(base_dir, exist_ok=True)

    resultados = {}

    for carpeta, nombre_especie in especies.items():
        save_dir = os.path.join(base_dir, carpeta)
        os.makedirs(save_dir, exist_ok=True)

        url = "https://api.inaturalist.org/v1/observations"
        params = {
            "taxon_name": nombre_especie,
            "per_page": 50,
            "photos": True,
            "order_by": "votes",
            "quality_grade": "research"
        }

        response = requests.get(url, params=params)
        data = response.json()

        count = 0
        for i, obs in enumerate(data.get("results", [])):
            photos = obs.get("photos", [])
            if not photos:
                continue

            photo_url = photos[0]["url"].replace("square", "medium")

            try:
                image_data = requests.get(photo_url).content
                file_path = os.path.join(save_dir, f"{carpeta}_{i+1}.jpg")
                with open(file_path, "wb") as f:
                    f.write(image_data)
                count += 1
            except Exception as e:
                print(f"Error al guardar imagen {carpeta}_{i+1}: {e}")

        resultados[carpeta] = f"{count} imágenes descargadas en {save_dir}"

    return resultados
