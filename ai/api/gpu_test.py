
from fastapi import APIRouter, FastAPI, File, UploadFile
from typing import Union, List, Optional

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from typing import List
from pydantic import BaseModel

import torch
from transformers import PreTrainedTokenizerFast
from transformers import BartForConditionalGeneration
import tensorflow as tf

tokenizer = PreTrainedTokenizerFast.from_pretrained('gogamza/kobart-summarization')
model = BartForConditionalGeneration.from_pretrained('gogamza/kobart-summarization')

router = APIRouter()

class SummaryRequest(BaseModel):    
    text: str
    length_penalty: Optional[float] = 1.0# 길이에 대한 penalty값. 1보다 작은 경우 더 짧은 문장을 생성하도록 유도하며, 1보다 클 경우 길이가 더 긴 문장을 유도
    max_length: Optional[int] = 128     # 요약문의 최대 길이 설정
    min_length: Optional[int] = 32      # 요약문의 최소 길이 설정
    num_beams: Optional[int] = 4        # 문장 생성시 다음 단어를 탐색하는 영역의 개수 
    

@router.post("/summarize", tags=["gpu"])
async def summarize(request: SummaryRequest):
    text = request.text
    raw_input_ids = tokenizer.encode(text)
    input_ids = [tokenizer.bos_token_id] + raw_input_ids + [tokenizer.eos_token_id]
    input_ids = torch.tensor([input_ids])

    summary_text_ids = model.generate(
        input_ids=input_ids,
        bos_token_id=model.config.bos_token_id,
        eos_token_id=model.config.eos_token_id,
        
        length_penalty=request.length_penalty,
        max_length=request.max_length,
        min_length=request.min_length,
        num_beams=request.num_beams,
    )

    res = tokenizer.decode(summary_text_ids[0], skip_special_tokens=True)

    resDict = {'summary': res}
    resJson = jsonable_encoder(resDict)
    return JSONResponse(content=resJson)


@router.get("/check", tags=["gpu"])
async def gpu_check():
    resDict = {'result': tf.config.list_physical_devices()}
    # resDict = {'result':'test'}
    resJson = jsonable_encoder(resDict)
    return JSONResponse(content=resJson)