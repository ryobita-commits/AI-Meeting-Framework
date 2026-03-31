# Encoding Rules

## 基本方針

このリポジトリのテキストファイルは、原則として次の形式に統一する。

- 文字コード: `UTF-8`
- BOM: `なし`
- 改行コード: `LF`

## 対象

このルールは少なくとも次に適用する。

- `*.md`
- `*.yaml`, `*.yml`
- `*.json`
- `*.toml`
- `*.txt`
- `*.py`
- `*.ps1`

## なぜ必要か

Windows の PowerShell やエディタの設定によっては、ファイル自体が壊れていなくても文字化けして見えることがある。  
また、保存時に `CP932` や `UTF-8 with BOM`、`CRLF` が混ざると、Git 差分やツール処理で問題が出やすい。

このリポジトリでは、次の 3 段で防ぐ。

1. `.editorconfig`
   - 保存時の既定を UTF-8 / LF に寄せる
2. `.gitattributes`
   - Git 上の改行を正規化する
3. `scripts/check_utf8.py`
   - テキストファイルが UTF-8 で読めるか確認する

## 書き込みルール

ファイルを追加、編集するときは次を守る。

1. 新規テキストファイルは UTF-8 で保存する
2. BOM は付けない
3. 改行は LF にする
4. 既存ファイルが UTF-8 の場合、別エンコーディングで上書きしない
5. Windows で文字化けして見えても、まずファイル内容と表示環境を分けて考える

## 文字化けに見えるときの切り分け

### 1. ファイルが壊れているか確認する

Python で UTF-8 として読めるなら、まずファイル自体は壊れていない可能性が高い。

```powershell
@'
from pathlib import Path
print(Path("README.md").read_text(encoding="utf-8")[:200])
'@ | python -
```

### 2. PowerShell の表示が原因か確認する

PowerShell のコードページや出力エンコーディングによって、日本語が崩れて見えることがある。  
ファイルが UTF-8 で読めるなら、表示側の問題である可能性が高い。

## 確認コマンド

リポジトリ全体の UTF-8 確認:

```powershell
python scripts/check_utf8.py
```

特定フォルダだけ確認:

```powershell
python scripts/check_utf8.py samples templates
```

## 補足

- Markdown の内容が PowerShell 上で文字化けして見えても、GitHub や UTF-8 対応エディタでは正常に見えることがある
- 文字化けの見た目だけで再保存すると、本当に壊すことがある
- 怪しいときは、再保存より先に UTF-8 読み取り確認を行う

