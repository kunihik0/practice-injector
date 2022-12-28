from abc import ABC, abstractmethod

import MeCab


class TokenizerInterface(ABC):
    @abstractmethod
    def tokenize(self, text: str) -> str:
        ...


class MecabTokenizer(TokenizerInterface):
    def __init__(self) -> None:
        self.mecab = MeCab.Tagger()

    def tokenize(self, text: str) -> str:
        return self.mecab.parse(text)
