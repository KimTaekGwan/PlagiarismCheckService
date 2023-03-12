from fastapi import APIRouter
# from pydantic import BaseModel
# from conn.db_connection import engineconn
# from conn.db_class import Test

router = APIRouter()
# engine = engineconn()
# session = engine.sessionmaker()

@router.get("/",tags=["XAI"])
async def firstss_get():
    return {'result':'test'}

# class Item(BaseModel):
#     name : str
#     number : int

# @router.post("/post", tags=["post"])
# async def first_post(item:Item):
#     addMemo = Test(name=item.name, number=item.number)
#     session.add(addMemo)
#     session.commit()
#     return item