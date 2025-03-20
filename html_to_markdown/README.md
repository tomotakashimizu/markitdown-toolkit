# HTML to Markdown コンバーター

HTML ファイルを Markdown ファイルに変換するシンプルで使いやすい Python ツールです。

## 機能

- 単一の HTML ファイルを Markdown に変換
- ディレクトリ内のすべての HTML ファイルを一括変換
- サブディレクトリ内の HTML ファイルも再帰的に処理可能
- 変換の成功・失敗の詳細レポート提供

## 必要条件

- Python 3.6 以上
- [markitdown](https://github.com/microsoft/markitdown) コマンドラインツール

## インストール

### markitdown のインストール

このスクリプトは外部ツールとして `markitdown` を使用します。以下のいずれかの方法でインストールしてください。

```bash
# pipを使用してインストール（推奨）
pip install 'markitdown[all]~=0.1.0a1'

# または個別の機能だけをインストール
pip install markitdown[html]
```

詳細は [markitdown の公式ドキュメント](https://github.com/microsoft/markitdown) を参照してください。

### スクリプトの実行権限を設定（Unix/Linux/Mac 環境）

```bash
chmod +x html_to_markdown.py
```

## 使い方

### 基本的な使用方法

```bash
python html_to_markdown.py <入力パス> [オプション]
```

または実行権限を設定した場合：

```bash
./html_to_markdown.py <入力パス> [オプション]
```

### コマンドラインオプション

| オプション        | 説明                                                   |
| ----------------- | ------------------------------------------------------ |
| `<入力パス>`      | 変換する HTML ファイルまたはディレクトリのパス（必須） |
| `-o, --output`    | 出力するファイルまたはディレクトリのパス（省略可）     |
| `-r, --recursive` | サブディレクトリも再帰的に処理する                     |
| `-h, --help`      | ヘルプメッセージを表示する                             |

### 使用例

#### 単一のファイルを変換

```bash
python html_to_markdown.py example.html
```

指定した出力先に変換：

```bash
python html_to_markdown.py example.html -o converted/example.md
```

#### ディレクトリ内のすべての HTML ファイルを変換

```bash
python html_to_markdown.py html_dir/
```

指定した出力ディレクトリに変換：

```bash
python html_to_markdown.py html_dir/ -o markdown_dir/
```

#### サブディレクトリも含めて再帰的に変換

```bash
python html_to_markdown.py html_dir/ -r
```

## 出力

デフォルトでは以下のような出力となります：

- 単一ファイルの場合：入力ファイルと同じ場所に拡張子を `.md` に変更したファイル
- ディレクトリの場合：入力ディレクトリの中に `markdown` というサブディレクトリを作成

## 注意事項

- `markitdown` コマンドがインストールされていない場合はエラーメッセージが表示されます
- サブディレクトリの階層構造は出力先でも保持されます（`-r` オプション使用時）
