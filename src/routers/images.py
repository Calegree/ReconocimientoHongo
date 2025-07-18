from fastapi import APIRouter
from src.services.inaturalist import descargar_imagenes

router = APIRouter()

@router.get("/descargar-imagenes")
def descargar():
    return descargar_imagenes()
