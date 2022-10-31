from fastapi import FastAPI
from pydantic import BaseModel

from utils.PapagoKoRTT import PapagoKoRTT

def round_trip_trans(input_sentence):
    if input_sentence:
        papagoKoRTT = PapagoKoRTT(input_sentence)
        output = papagoKoRTT.roundTripTranslation()
    return output

print(round_trip_trans('안뇽?'))