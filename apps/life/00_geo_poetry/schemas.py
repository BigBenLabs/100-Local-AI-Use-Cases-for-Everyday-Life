from pydantic import BaseModel, Field
from typing_extensions import List, TypedDict


# 定义一个线性工作流存储器类型
class PoemState(TypedDict):
    time_info: str
    weather_info: str
    location_info: TypedDict
    culture_info: str
    poem: TypedDict


