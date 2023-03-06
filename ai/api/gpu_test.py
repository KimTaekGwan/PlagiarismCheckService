from keras import backend as K
# from transformers import BertTokenizer, BertModel
# import torch

# tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')
# model = BertModel.from_pretrained('bert-base-multilingual-cased')
# model.to('cuda')  # GPU를 사용하여 모델 로딩

from fastapi import APIRouter
from typing import Union

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

router = APIRouter()



@router.get("/gpu", tags=["gpu"])
async def check():
    resDict = {'result': K.tensorflow_backend._get_available_gpus()}
    # resDict = {'result':'test'}
    resJson = jsonable_encoder(resDict)
    return JSONResponse(content=resJson)