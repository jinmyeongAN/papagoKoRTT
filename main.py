from fastapi import FastAPI
from pydantic import BaseModel

from utils.PapagoKoRTT import PapagoKoRTT

class Sentence(BaseModel):
    setence: str

app = FastAPI()


@app.post("/papago/")
async def round_trip_trans(input_sentence: Sentence):
    sentence_dict = input_sentence.dict()
    if input_sentence.setence:
        papagoKoRTT = PapagoKoRTT(input_sentence.setence)
        output = papagoKoRTT.roundTripTranslation()
        sentence_dict.update({"sentence": output})
    return sentence_dict
