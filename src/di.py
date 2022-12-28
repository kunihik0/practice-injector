from injector import Binder, Injector

from src.db import DataBase, DataBaseInterface
from src.tokenizer import MecabTokenizer, TokenizerInterface
from src.usecase import UseCase, UseCaseInterface


def configure(binder: Binder) -> None:
    binder.bind(DataBaseInterface, to=DataBase)  # type: ignore
    binder.bind(TokenizerInterface, to=MecabTokenizer)  # type: ignore
    binder.bind(UseCaseInterface, to=UseCase)  # type: ignore


injector = Injector([configure])

__all__ = ["injector"]
