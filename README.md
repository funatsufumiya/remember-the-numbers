# 数字の語呂合わせを自動生成するスクリプト

## kana2nums

ひらがなを数字に変換するスクリプト。nodejsを使用。

```bash
$ scripts/kana2nums -h
# Usage: kana2nums [hiragana]

$ scripts/kana2nums むさし
# 634

$ scripts/kana2nums しこく
# 459

$ scripts/kana2nums にしみなみ
# 24373

$ scripts/kana2nums ががが
# [エラー] 1文字目(が)が翻訳できませんでした。

```
