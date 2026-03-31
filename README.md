# AI-Meeting-Framework

複数 AI と人間が、1つの会議として見える形で議論、整理、判断、記録を行うための framework です。

## 目的

この framework は、内部では複数 AI が役割分担して考えつつ、外部には 1 本の会議ログとして分かりやすく見せることを目的とします。

## 中核コンセプト

- framework 名: `AI-Meeting-Framework`
- 会議モード名: `Council Mode`

`Council Mode` は、複数 AI が立場と性格を持って議論し、moderator が結論をまとめる会議モードです。

## この framework でできること

- AI メンバーを追加、削除できる
- AI ごとに性格、口調、重視する価値を設定できる
- `AI-Only` と `Human-in-the-Loop` を切り替えられる
- 内部では分業しつつ、外部には 1 つの会議ログとして表示できる
- 会議の結果を `transcript`, `meeting note`, `decision memo`, `action list` として残せる

## 最初に見るファイル

- `README.md`
- `MEETING_MODES.md`
- `COUNCIL_MODE.md`
- `LIVE_COUNCIL_MODE.md`
- `config/personas.yaml`
- `config/participants.yaml`
- `config/transcript-style.yaml`
- `councils/default-council.yaml`
- `councils/live-default-council.yaml`
- `templates/agenda.md`
- `templates/transcript.md`
- `templates/live-transcript.md`
- `templates/character-live-transcript.md`
- `templates/teaching-transcript.md`
- `templates/meeting-note.md`
- `templates/action-list.md`
- `templates/summary.md`
- `templates/live-summary.md`
- `templates/report.md`

## ディレクトリ構成

- `config/`: 会議モード、参加者、ペルソナ、表示ルール
- `councils/`: 会議ごとの標準構成
- `templates/`: agenda、transcript、meeting note、decision memo、action list などのテンプレート
- `samples/`: 会議サンプル
- `sessions/`: 実際の会議で作られる成果物
  - `summaries/`: 人が最初に読む短い要約
  - `reports/`: 会議全体の流れと結論を読む報告書
- `bootstrap/`: 会議を始めるための初期質問と起動テンプレート

## 会議モード

| モード | 向いている場面 | 最終判断 | 主な出力 |
| --- | --- | --- | --- |
| `AI-Only` | 事前整理、論点洗い出し、比較表作成、たたき台作成 | `moderator` または保留 | transcript、option comparison、draft decision |
| `Human-in-the-Loop` | 目的確定、優先順位付け、高リスク判断、最終承認 | human | transcript、meeting note、decision memo |
| `Council Mode` | 複数 AI の立場差を明示し、会議として見せたい時 | human または設定次第 | transcript、meeting note、decision memo、action list |
| `Live Council Mode` | リアルタイム風に会話を見せたい時、雑談会議、エンタメ性を重視する時 | human または設定次第 | live transcript、summary、meeting note、decision memo、action list |

## 既定の参加者

- `moderator`
- `critic`
- `advocate`
- `analyst`
- `human`

必要に応じて以下も追加できます。

- `realist`
- `creative`
- `finance`
- `legal`
- `customer_voice`
- `yang`
- `julian`

## 性格設定の考え方

性格は固定パラメーターだけではなく、日本語や文章でも指定できる前提です。

たとえば次のように定義できます。

- どんな性格か
- どういう口調か
- 何を重視するか
- 何を嫌うか
- 必ずやること
- やってはいけないこと

## キャラクター性のある構成

役割名だけでなく、キャラクター性を持った参加者も追加できます。

- `yang`: 長期視点と歴史観を持つ教え諭す役
- `julian`: 読者の代わりに質問する役

専用構成は [councils/yang-council.yaml](councils/yang-council.yaml) に定義できます。

## transcript の見せ方

表示スタイルは複数持てます。

- `default`: 実務向けで無難
- `lively`: 少し会議感を強める
- `character`: キャラ名と役割を前面に出す
- `teaching`: ヤンとユリアンのように、教え諭す会話として見せる

## 人が最初に読む資料

会議結果は、次の順で読む前提が分かりやすいです。

1. `sessions/summaries/`
2. `sessions/reports/`
3. `sessions/transcripts/` または `sessions/live-transcripts/`

短く把握したい時は `summary`、流れごと理解したい時は `report`、発言を追いたい時は `transcript` を読みます。

## 次にやること

1. `config/personas.yaml` で性格を定義する
2. `config/participants.yaml` で参加者を定義する
3. `councils/default-council.yaml` で標準会議構成を決める
4. `templates/transcript.md` に沿って会議ログを出す
