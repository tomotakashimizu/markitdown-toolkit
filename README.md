# markitdown-toolkit

[markitdown](https://github.com/microsoft/markitdown)を活用した Markdown 変換・処理ユーティリティツール集です。

## 概要

このリポジトリには、ドキュメント処理に役立つ複数の Python 製ユーティリティが含まれています。markitdown を利用した HTML→Markdown 変換や、Markdown ファイルの結合など、様々なシナリオで活用できるツールを提供しています。

## リポジトリ構成

このツールキットは以下のモジュールで構成されています：

- [**HTML to Markdown コンバーター**](./html_to_markdown/README.md) - HTML ファイルを Markdown に変換するツール
- [**Markdown マージツール**](./markdown_merge/README.md) - 複数の Markdown ファイルを結合するツール

## 必要条件

- Python 3.6 以上
- HTML→Markdown 変換には[markitdown](https://github.com/microsoft/markitdown)が必要（詳細は各ツールの README を参照）

## クイックスタート

以下の手順でこのリポジトリを使い始めることができます：

### 1. リポジトリのクローン

```bash
git clone https://github.com/tomotakashimizu/markitdown-toolkit.git
cd markitdown-toolkit
```

### 2. 依存パッケージのインストール（HTML→Markdown 変換を行う場合）

```bash
pip install 'markitdown[all]~=0.1.0a1'
```

### 3. 使用例

**HTML を Markdown に変換：**

```bash
python html_to_markdown/html_to_markdown.py example.html
```

**複数の Markdown ファイルを結合：**

```bash
python markdown_merge/merge_n_markdown.py markdown_dir/
```

各ツールの詳細な使い方については、それぞれのディレクトリ内の README をご参照ください：

- [HTML to Markdown コンバーター](./html_to_markdown/README.md)
- [Markdown マージツール](./markdown_merge/README.md)

## ライセンス情報

このツールキットは MIT ライセンスで公開されています。ただし、HTML→Markdown 変換の機能では、Microsoft が開発している[markitdown](https://github.com/microsoft/markitdown)ライブラリを使用しています。

markitdown は MIT ライセンスで公開されており、帰属表示（attribution）が必要です。詳細は[markitdown のリポジトリ](https://github.com/microsoft/markitdown)を参照してください。

### markitdown ライセンスについて

markitdown は MIT ライセンスで公開されています。これは比較的寛容なライセンスで、以下の条件を満たす限り、商用利用を含む様々な用途に利用できます：

- 著作権表示とライセンス表示を含める
- 同じライセンスの下で再配布する必要はない

当ツールキットは markitdown のラッパーとして機能する部分を含みますが、markitdown そのものを再配布するものではありません。
