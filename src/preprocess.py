from abc import ABC, abstractmethod
from typing import List

import MeCab


class TokenizerInterface(ABC):
    @abstractmethod
    def tokenize(self, text: str) -> List[str]:
        ...


class MecabTokenizer(TokenizerInterface):
    def __init__(self) -> None:
        self.mecab = MeCab.Tagger()

    def tokenize(self, text: str) -> List[str]:
        return self.mecab.parse(text).split()
