# La bonne pratique est de mettre dans un fichier comme lui l'ensemble des class qu'on va utiliser pour notre requete et reponse 
# On peut el faire avec pydantic 

from pydantic import BaseModel, Field


class HousingFeatures(BaseModel):
    MedInc: float = Field(..., description="Revenu médian")
    HouseAge: float = Field(..., description="Âge médian des maisons")
    AveRooms: float = Field(..., description="Nombre moyen de pièces")
    AveBedrms: float = Field(..., description="Nombre moyen de chambres")
    Population: float = Field(..., description="Population du bloc")
    AveOccup: float = Field(..., description="Nombre moyen d'occupants")
    Latitude: float = Field(..., description="Latitude")
    Longitude: float = Field(..., description="Longitude")

class PredictionResponse(BaseModel):
    predicted_house_value: float
    status: str = "success"