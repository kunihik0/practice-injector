from unittest import TestCase
from unittest.mock import Mock

from src.db import Data, DataBaseInterface
from src.di import injector
from src.tokenizer import TokenizerInterface
from src.usecase import UseCase


class TestUsecase(TestCase):
    def test_preprocess(self) -> None:
        db = Mock(spec=DataBaseInterface)
        db.get.return_value = [
            Data(
                **{
                    "名前": "テスト",
                    "自己紹介": "こんにちは。私は、東京都出身のテストです。",
                    "趣味": "私はtestに入ることが好きです。",
                    "好きな食べ物": "私はテストが好きです。",
                }
            )
        ]

        tokenizer = injector.get(TokenizerInterface)  # type: ignore

        usecase = UseCase(tokenizer, db)  # type: ignore

        actual = usecase.preprocess("path/to/data")
        expected = [
            {
                "名前": "テスト",
                "自己紹介": "こんにちは 。 私 は 、 東京 都 出身 の テスト です 。 \n",
                "趣味": "私 は test に 入る こと が 好き です 。 \n",
                "好きな食べ物": "私 は テスト が 好き です 。 \n",
            }
        ]

        self.assertEqual(actual, expected)
