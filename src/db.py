import json
from abc import ABC, abstractmethod
from typing import Any, Dict, List

from pydantic import BaseModel, Field


class Data(BaseModel):
    name: str = Field(..., alias="名前")
    introduction: str = Field(..., alias="自己紹介")
    hobby: str = Field(..., alias="趣味")
    favorite_food: str = Field(..., alias="好きな食べ物")


class DataBaseInterface(ABC):
    @abstractmethod
    def get(self, path: str) -> List[Data]:
        ...

    def save(self, data: List[Dict[str, Any]], path: str) -> None:
        ...


class DataBase(DataBaseInterface):
    def get(self, path: str) -> List[Data]:
        json_data = json.load(open(path))
        return [Data(**data) for data in json_data]

    def save(self, data: List[Dict[str, Any]], path: str) -> None:
        json.dump(data, open(path, "w"), ensure_ascii=False, indent=4)
