from typing import Union, List, Optional
from pydantic import BaseModel
from uuid import UUID, uuid4
from enum import Enum

from sqlalchemy import Column, Integer, String
from config import Base


class Book(Base):
    __tablename__ = 'book'
    
    id=Column(Integer, primary_key=True)
    title=Column(String)
    description=Column(String)


class Gender(str, Enum):
    male = "male"
    female = "female"
    
class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]

class UserUpdateRequest(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    roles: Optional[List[Role]]

db: List[User] = [
    User(
        id=UUID("73a8c1aa-53b9-4ee9-982d-149795b68a7f"),
        first_name="Kim",
        last_name="TaekGwan",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=UUID("718e738e-8a45-4c6c-9a94-a82719276e90"),
        first_name="Lee",
        last_name="Guan",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]


##########################################
class SummaryRequest(BaseModel):    
    text: str
    length_penalty: Optional[float] = 1.0   # 길이에 대한 penalty값. 1보다 작은 경우 더 짧은 문장을 생성하도록 유도하며, 1보다 클 경우 길이가 더 긴 문장을 유도
    max_length: Optional[int] = 128     # 요약문의 최대 길이 설정
    min_length: Optional[int] = 32      # 요약문의 최소 길이 설정
    num_beams: Optional[int] = 4        # 문장 생성시 다음 단어를 탐색하는 영역의 개수 
