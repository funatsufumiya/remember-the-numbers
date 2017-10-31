# 数字の語呂合わせを自動生成する人工知能

## 方針

- ひらがなを数字に変換するスクリプト(`kana2nums`)を使い、辞書の見出しを数字に変換しておくことで、これを教師データとする。
- 辞書に無いデータは、平仮名N-gramを使うといいかもしれない

## kana2nums

ひらがなを数字に変換するスクリプト。nodejsを使用。

```bash
$ scripts/kana2nums -h
Usage: kana2nums [hiragana]

$ scripts/kana2nums むさし
634

$ scripts/kana2nums しこく
459

$ scripts/kana2nums にしみなみ
24373

```