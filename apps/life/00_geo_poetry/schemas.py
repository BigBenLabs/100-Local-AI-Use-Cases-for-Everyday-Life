from pydantic import BaseModel, Field
from typing_extensions import List, TypedDict
from prompts import poem_prompts


# 定义一个线性工作流存储器类型
class State(TypedDict):
    language: str
    timeInfo: str
    location: TypedDict
    locationInfo: TypedDict
    weather: str
    humanity: str
    poemInfo: TypedDict


