from abc import ABC, abstractmethod

import MeCab
import sudachipy


class TokenizerInterface(ABC):
    @abstractmethod
    def tokenize(self, text: str) -> str:
        ...


class MecabTokenizer(TokenizerInterface):
    def __init__(self) -> None:
        self.mecab = MeCab.Tagger()

    def tokenize(self, text: str) -> str:
        return self.mecab.parse(text)


class SudachiTokenizer(TokenizerInterface):
    def __init__(self) -> None:
        self.sudachi = sudachipy.Dictionary().create()

    def tokenize(self, text: str) -> str:
        tokenized = self.sudachi.tokenize(text, mode=sudachipy.Tokenizer.SplitMode.A)
        return " ".join([m.surface() for m in tokenized])
