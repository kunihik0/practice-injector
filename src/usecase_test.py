from unittest import IsolatedAsyncioTestCase
from unittest.mock import Mock

from src.db import Data, DataBaseInterface
from src.di import injector
from src.preprocess import TokenizerInterface
from src.usecase import UseCase


class TestUsecase(IsolatedAsyncioTestCase):
    async def test_preprocess(self) -> None:
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

        actural = usecase.preprocess("a")

        expected = (
            "こんにちは\t感動詞,*,*,*,*,*,こんにちは,コンニチハ,コンニチワ\n。\t"
            "記号,句点,*,*,*,*,。,。,。\n私\t名詞,代名詞,一般,*,*,*,私,ワタシ,ワタシ\nは\t"
            "助詞,係助詞,*,*,*,*,は,ハ,ワ\n、\t記号,読点,*,*,*,*,、,、,、\n東京\t名詞,固有名詞,"
            "地域,一般,*,*,東京,トウキョウ,トーキョー\n都\t名詞,接尾,地域,*,*,*,都,ト,ト\n出身\t"
            "名詞,一般,*,*,*,*,出身,シュッシン,シュッシン\nの\t助詞,連体化,*,*,*,*,の,ノ,ノ\nテスト\t"
            "名詞,サ変接続,*,*,*,*,テスト,テスト,テスト\nです\t助動詞,*,*,*,特殊・デス,基本形,です,デス,デス\n。\t"
            "記号,句点,*,*,*,*,。,。,。\nEOS\n"
        )

        self.assertEqual(actural[0]["自己紹介"], expected)
