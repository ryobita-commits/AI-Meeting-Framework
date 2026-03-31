# AI-Meeting-Framework

複数 AI と人間が、1つの会議として見える形で議論、整理、判断、記録を行うための framework です。

内部では役割分担して考えつつ、外部には読みやすい会議ログ、要約、報告書として見せることを目的にしています。

## できること

- 複数 AI の役割分担による会議
- 人間参加あり、なしの切り替え
- 会議ログを `transcript`、`summary`、`report` に分けて出力
- `character` モードによるキャラ性のある会話表示
- `teaching` モードによる分かりやすい読解支援
- 会議テーマごとの bootstrap とテンプレート運用

## 中核コンセプト

- framework 名: `AI-Meeting-Framework`
- 中核モード名: `Council Mode`

`Council Mode` は、複数 AI が立場と性格を持って議論し、moderator が結論をまとめる会議モードです。

## 最短の始め方

1. [MEETING_MODES.md](C:\Users\akira_hamasaki\Projects\AI-Meeting-Framework\MEETING_MODES.md) を読む
2. [config/personas.yaml](C:\Users\akira_hamasaki\Projects\AI-Meeting-Framework\config\personas.yaml) で性格設定を見る
3. [config/participants.yaml](C:\Users\akira_hamasaki\Projects\AI-Meeting-Framework\config\participants.yaml) で参加者構成を見る
4. [councils/default-council.yaml](C:\Users\akira_hamasaki\Projects\AI-Meeting-Framework\councils\default-council.yaml) か [councils/yang-council.yaml](C:\Users\akira_hamasaki\Projects\AI-Meeting-Framework\councils\yang-council.yaml) を選ぶ
5. [templates/agenda.md](C:\Users\akira_hamasaki\Projects\AI-Meeting-Framework\templates\agenda.md) から会議を始める

普通のチャットでまず試すなら [CHAT_QUICKSTART.md](C:\Users\akira_hamasaki\Projects\AI-Meeting-Framework\CHAT_QUICKSTART.md) から入るのがおすすめです。

## 会議モード

| モード | 向いている場面 | 最終判断 | 主な出力 |
| --- | --- | --- | --- |
| `AI-Only` | 事前整理、論点洗い出し、比較表作成、たたき台作成 | `moderator` または保留 | transcript、draft decision |
| `Human-in-the-Loop` | 目的確定、優先順位付け、高リスク判断、最終承認 | human | transcript、meeting note、decision memo |
| `Council Mode` | 複数 AI の立場差を見せながら会議を進めたい時 | human または設定次第 | transcript、meeting note、decision memo、action list |
| `Live Council Mode` | リアルタイム風に会話を見せたい時、雑談会議、エンタメ性を重視する時 | human または設定次第 | live transcript、summary、meeting note、decision memo、action list |

## 表示スタイル

- `default`
  - 実務向けで簡潔
- `lively`
  - 少し会議感を強める
- `character`
  - キャラ名と役割を前面に出す
- `teaching`
  - ヤンとユリアンのように、教え諭す会話として見せる

## teaching モード

`teaching` は、記事やエッセイを「分かりやすく、誤読しにくく読む」ためのモードです。

- 基本ガイド: [TEACHING_MODE.md](C:\Users\akira_hamasaki\Projects\AI-Meeting-Framework\TEACHING_MODE.md)
- teaching 入口: [TEACHING_SAMPLES.md](C:\Users\akira_hamasaki\Projects\AI-Meeting-Framework\TEACHING_SAMPLES.md)
- ニュース、解説記事向け: [article-reading-teaching.md](C:\Users\akira_hamasaki\Projects\AI-Meeting-Framework\templates\article-reading-teaching.md)
- インタビュー記事向け: [interview-reading-teaching.md](C:\Users\akira_hamasaki\Projects\AI-Meeting-Framework\templates\interview-reading-teaching.md)
- エッセイ、論説向け: [essay-reading-teaching.md](C:\Users\akira_hamasaki\Projects\AI-Meeting-Framework\templates\essay-reading-teaching.md)

向いている用途:

- ニュース記事
- インタビュー記事
- 論説、批評
- エッセイ
- 読み手が騙されやすい文章の検証

Gemini などの一般的なチャットで使うときは [CHAT_QUICKSTART.md](C:\Users\akira_hamasaki\Projects\AI-Meeting-Framework\CHAT_QUICKSTART.md) を使うと、そのまま始めやすいです。

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

## キャラクター性のある構成

役割名だけでなく、キャラクター性を持った参加者も追加できます。

- `yang`
  - 長期視点と歴史観を持つ教え諭す役
- `julian`
  - 読者の代わりに質問する役

専用構成は [councils/yang-council.yaml](C:\Users\akira_hamasaki\Projects\AI-Meeting-Framework\councils\yang-council.yaml) にあります。

## 人が最初に読む資料

会議結果は、次の順で読むのが分かりやすいです。

1. `sessions/summaries/`
2. `sessions/reports/`
3. `sessions/transcripts/` または `sessions/live-transcripts/`

短く把握したい時は `summary`、流れごと理解したい時は `report`、発言を追いたい時は `transcript` を読みます。

## 主要ファイル

- [MEETING_MODES.md](C:\Users\akira_hamasaki\Projects\AI-Meeting-Framework\MEETING_MODES.md)
- [COUNCIL_MODE.md](C:\Users\akira_hamasaki\Projects\AI-Meeting-Framework\COUNCIL_MODE.md)
- [LIVE_COUNCIL_MODE.md](C:\Users\akira_hamasaki\Projects\AI-Meeting-Framework\LIVE_COUNCIL_MODE.md)
- [config/personas.yaml](C:\Users\akira_hamasaki\Projects\AI-Meeting-Framework\config\personas.yaml)
- [config/participants.yaml](C:\Users\akira_hamasaki\Projects\AI-Meeting-Framework\config\participants.yaml)
- [config/transcript-style.yaml](C:\Users\akira_hamasaki\Projects\AI-Meeting-Framework\config\transcript-style.yaml)
- [templates/agenda.md](C:\Users\akira_hamasaki\Projects\AI-Meeting-Framework\templates\agenda.md)
- [templates/transcript.md](C:\Users\akira_hamasaki\Projects\AI-Meeting-Framework\templates\transcript.md)
- [templates/character-live-transcript.md](C:\Users\akira_hamasaki\Projects\AI-Meeting-Framework\templates\character-live-transcript.md)
- [templates/teaching-transcript.md](C:\Users\akira_hamasaki\Projects\AI-Meeting-Framework\templates\teaching-transcript.md)
- [templates/summary.md](C:\Users\akira_hamasaki\Projects\AI-Meeting-Framework\templates\summary.md)
- [templates/report.md](C:\Users\akira_hamasaki\Projects\AI-Meeting-Framework\templates\report.md)
- [samples/README.md](C:\Users\akira_hamasaki\Projects\AI-Meeting-Framework\samples\README.md)
- [CHANGELOG.md](C:\Users\akira_hamasaki\Projects\AI-Meeting-Framework\CHANGELOG.md)
- [CHAT_QUICKSTART.md](C:\Users\akira_hamasaki\Projects\AI-Meeting-Framework\CHAT_QUICKSTART.md)

## ディレクトリ構成

- `bootstrap/`
  - 会議を始めるための初期質問と起動テンプレート
- `config/`
  - 会議モード、参加者、ペルソナ、表示ルール
- `councils/`
  - 会議ごとの標準構成
- `templates/`
  - agenda、transcript、meeting note、decision memo、action list などのテンプレート
- `samples/`
  - 会議サンプル
- `sessions/`
  - 実際の会議で作られる成果物
- `scripts/`
  - 補助スクリプト

## 文字コードと保存ルール

テキストファイルは原則として次で統一します。

- 文字コード: UTF-8
- BOM: なし
- 改行: LF

詳細は [ENCODING_RULES.md](C:\Users\akira_hamasaki\Projects\AI-Meeting-Framework\ENCODING_RULES.md) を参照してください。  
UTF-8 確認は [scripts/check_utf8.py](C:\Users\akira_hamasaki\Projects\AI-Meeting-Framework\scripts\check_utf8.py) で行えます。

## リポジトリ運用

- GitHub テンプレートまたは複製元として使えます
- 初期安定版は `v1.0.0`
- 今後の変更は改善提案ベースで小さく積み上げます
