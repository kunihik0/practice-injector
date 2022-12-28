from abc import ABC, abstractmethod

from injector import inject

from src.db import DataBaseInterface
from src.preprocess import TokenizerInterface


class UseCaseInterface(ABC):
    @abstractmethod
    def execute(self, data_path: str, save_path: str) -> None:
        ...


class UseCase(object):
    @inject
    def __init__(self, tokenizer: TokenizerInterface, db: DataBaseInterface):
        self.tokenizer = tokenizer
        self.db = db

    def execute(self, data_path: str, save_path: str) -> None:
        data_list = self.db.get(data_path)

        save_data = []
        for data in data_list:
            save_data.append(
                {
                    "名前": data.name,
                    "自己紹介": self.tokenizer.tokenize(data.introduction),
                    "趣味": self.tokenizer.tokenize(data.hobby),
                    "好きな食べ物": self.tokenizer.tokenize(data.favorite_food),
                }
            )
        self.db.save(save_data, save_path)
