from pydantic import BaseModel, Field
from typing_extensions import List, TypedDict


# 定义一个线性工作流存储器类型
class PoemState(TypedDict):
    language: str
    timeInfo: str
    location: TypedDict
    locationInfo: TypedDict
    weather: str
    culture: str
    poemInfo: TypedDict


