from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/morchellas")
def get_morchellas(per_page: int = 30):
    url = "https://api.inaturalist.org/v1/observations"
    params = {
        "q": "morchella",
        "per_page": per_page,
        "photos": True,
        "order_by": "votes",
        "quality_grade": "research"
    }
    response = requests.get(url, params=params)
    data = response.json()

    results = []
    for obs in data["results"]:
        if obs["photos"]:
            photo_url = obs["photos"][0]["url"].replace("square", "medium")
            results.append({
                "photo_url": photo_url,
                "species_guess": obs.get("species_guess"),
                "location": obs.get("location"),
                "observed_on": obs.get("observed_on")
            })

    return {"count": len(results), "observations": results}
