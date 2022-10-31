from fastapi import FastAPI
from pydantic import BaseModel


class Sentence(BaseModel):
    setence: str

app = FastAPI()


@app.post("/papago/")
async def round_trip_trans(input_sentence: Sentence):
    sentence_dict = input_sentence.dict()
    if input_sentence.setence:
        output = papago_KoRTT(input_sentence.setence)
        sentence_dict.update({"sentence": output})
    return sentence_dict
