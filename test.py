import parser
import unittest


class ParserTest(unittest.TestCase):
    def test_answer_sample1_1(self):
        with open('./cases/sample1.md') as f:
            text = f.read()

        tokenized = parser.parse(text)
        query = ['大見出し', '中見出し', '小見出し1']
        answer = parser.answer(tokenized, query)

        self.assertEqual(
            answer,
            ['本文1'],
        )

    def test_answer_sample1_2(self):
        with open('./cases/sample1.md') as f:
            text = f.read()

        tokenized = parser.parse(text)
        query = ['大見出し', '中見出し', '小見出し2']
        answer = parser.answer(tokenized, query)

        self.assertEqual(
            answer,
            ['本文2'],
        )

    def test_answer_sample1_3_empty(self):
        with open('./cases/sample1.md') as f:
            text = f.read()

        tokenized = parser.parse(text)
        query = ['大見出し', '中見出し', '小見出し3']
        answer = parser.answer(tokenized, query)

        self.assertEqual(
            answer,
            [],
        )

    def test_answer_sample1_4_no_query(self):
        with open('./cases/sample1.md') as f:
            text = f.read()

        tokenized = parser.parse(text)
        query = []

        self.assertRaises(
            Exception, parser.answer, tokenized, query
        )

    def test_answer_sample2_1(self):
        with open('./cases/sample2.md') as f:
            text = f.read()

        tokenized = parser.parse(text)
        query = ['大見出し', '中見出し2']
        answer = parser.answer(tokenized, query)

        self.assertEqual(
            answer,
            ['本文3'],
        )

    def test_answer_sample2_2(self):
        with open('./cases/sample2.md') as f:
            text = f.read()

        tokenized = parser.parse(text)
        query = ['大見出し', '中見出し1', '小見出し2']
        answer = parser.answer(tokenized, query)

        self.assertEqual(
            answer,
            ['本文2', '複数行もOK'],
        )

    def test_answer_sample3_1(self):
        with open('./cases/sample3.md') as f:
            text = f.read()

        tokenized = parser.parse(text)
        query = ['aab']
        answer = parser.answer(tokenized, query)

        self.assertEqual(
            answer,
            ['b'],
        )

    def test_answer_sample3_2(self):
        with open('./cases/sample3.md') as f:
            text = f.read()

        tokenized = parser.parse(text)
        query = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff']
        answer = parser.answer(tokenized, query)

        self.assertEqual(
            answer,
            ['hoge'],
        )

    def test_answer_sample3_3(self):
        with open('./cases/sample3.md') as f:
            text = f.read()

        tokenized = parser.parse(text)
        query = ['1', '2', '3', '4', '5', '6', 'not header!!!!']
        answer = parser.answer(tokenized, query)

        self.assertEqual(
            answer,
            [],
        )

    def test_answer_sample3_4(self):
        with open('./cases/sample3.md') as f:
            text = f.read()

        tokenized = parser.parse(text)
        query = ['1', '2', '3', '4', '5', '6']
        answer = parser.answer(tokenized, query)

        self.assertEqual(
            answer,
            ['####### not header!!!!', 'hoge'],
        )

    def test_answer_portfolio_1(self):
        with open('./cases/portfolio_example.md') as f:
            text = f.read()

        tokenized = parser.parse(text)
        query = ['ポートフォリオ', '研究内容', '論文']
        answer = parser.answer(tokenized, query)

        self.assertEqual(
            [
                '- レシピ文章の日本語-英語機械翻訳',
                '    - 毎日楽太郎，九々波土',
                '    - 料理情報学会論文集 123 2017年5月',
            ],
            answer,
        )

    def test_answer_portfolio_2(self):
        with open('./cases/portfolio_example.md') as f:
            text = f.read()

        tokenized = parser.parse(text)
        query = ['ポートフォリオ', '研究内容']
        answer = parser.answer(tokenized, query)

        self.assertEqual(
            [
                '- 自然言語処理（レシピの解析や検索、分類、推薦、翻訳）',
                '- 画像認識（料理写真の分類やクロッピング）',
            ],
            answer,
        )

    def test_answer_portfolio_3(self):
        with open('./cases/portfolio_example.md') as f:
            text = f.read()

        tokenized = parser.parse(text)
        query = ['ポートフォリオ', '公開中のサービス、アプリケーション、ライブラリ']
        answer = parser.answer(tokenized, query)

        self.assertEqual(
            [
                '- クックパッド',
                '    - https://cookpad.com',
                '    - 開発メンバーとして、閲覧したレシピの記録機能を担当',
                '- みんなのお弁当',
                '    - https://itunes.apple.com/app/id977965019',
                '    - UIデザインを除くプログラミング全般（サーバーサイド、アプリケーション）を担当',
            ],
            answer,
        )


if __name__ == '__main__':
    unittest.main()
