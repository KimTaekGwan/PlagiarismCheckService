
from fastapi import APIRouter, FastAPI, File, UploadFile

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from models import SummaryRequest


import torch
from transformers import PreTrainedTokenizerFast
from transformers import BartForConditionalGeneration
import tensorflow as tf

tokenizer = PreTrainedTokenizerFast.from_pretrained('gogamza/kobart-summarization')
model = BartForConditionalGeneration.from_pretrained('gogamza/kobart-summarization')

router = APIRouter()
    

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