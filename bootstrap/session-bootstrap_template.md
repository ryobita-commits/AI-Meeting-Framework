# session bootstrap template

## 目的

初期回答を、実際に会議を始めるための最初の live ファイルへ変換する。

## 入力

- `bootstrap/meeting-type-router.md`
- `bootstrap/questions/<type>.md`
- `bootstrap/initial-answers.md`
- `templates/agenda.md`
- `templates/transcript.md`
- `templates/meeting-note.md`
- `templates/decision-memo.md`
- `templates/action-list.md`

## 出力

- `sessions/agendas/<date>-<topic>.md`
- `sessions/transcripts/<date>-<topic>.md`
- `sessions/notes/<date>-<topic>.md`
- `sessions/decisions/<date>-<topic>.md`
- `sessions/actions/<date>-<topic>.md`

## 変換ルール

- テーマは短く分かりやすくする
- 判断したい問いを1文で固定する
- 人間が参加する場合は、その役割を agenda に明記する
- `AI-Only` か `Human-in-the-Loop` かを最初に決める
- 高リスク論点がある場合は `Human-in-the-Loop` を優先する

## 最低限抜き出す項目

- 会議種別
- テーマ
- 判断したい問い
- 制約
- 扱わないこと
- 欲しい成果物
- 会議モード
