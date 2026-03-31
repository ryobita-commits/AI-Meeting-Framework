# COUNCIL_MODE

## 概要

`Council Mode` は、複数 AI がそれぞれの立場、性格、口調を持ち、1つの会議として見える形で議論するためのモードです。

## 基本構成

- `moderator`: 進行、論点整理、結論記録
- `critic`: リスク、反対論点、失敗条件
- `advocate`: 前向きな案、実行しやすい進め方
- `analyst`: 事実整理、比較軸、判断順序
- `human`: 制約、意図、最終判断

## 価値

- 人にとって会議として理解しやすい
- 論点が役割ごとに分かれる
- AI の分業を保ちつつ、体験としては一体化できる

## 典型的な流れ

1. moderator が問いを定義する
2. analyst が前提と比較軸を整理する
3. advocate が進める案を出す
4. critic が危険と抜け漏れを出す
5. human が制約と優先順位を補足する
6. moderator が結論と次アクションをまとめる

## 出力

- transcript
- meeting note
- decision memo
- action list
