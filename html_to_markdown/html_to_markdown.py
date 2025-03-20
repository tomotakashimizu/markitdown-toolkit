"""
HTML & Markdown ツールキット - HTML to Markdown コンバーター

HTMLファイルをMarkdownに変換するPythonスクリプト。
単一ファイルの変換、ディレクトリ内の一括変換、再帰的な処理に対応しています。
"""

import os
import subprocess
import argparse
from pathlib import Path


def convert_html_to_markdown(input_path, output_path, recursive=False):
    """
    HTMLファイルをMarkdownに変換する関数

    Args:
        input_path (Path): 入力ディレクトリまたはファイルのパス
        output_path (Path): 出力ディレクトリまたはファイルのパス
        recursive (bool): サブディレクトリも再帰的に処理するかどうか
    
    Returns:
        tuple: (成功したファイル数, 失敗したファイル数)
    """
    success_count = 0
    failure_count = 0
    
    # 入力がディレクトリの場合
    if input_path.is_dir():
        # 出力ディレクトリが存在しない場合は作成
        output_path.mkdir(exist_ok=True, parents=True)
        
        # HTMLファイルを取得
        if recursive:
            html_files = list(input_path.glob("**/*.html"))
        else:
            html_files = list(input_path.glob("*.html"))
        
        if not html_files:
            print(f"警告: 指定されたディレクトリ '{input_path}' にHTMLファイルが見つかりませんでした。")
            return success_count, failure_count
        
        # 各HTMLファイルをMarkdownに変換
        for html_file in html_files:
            # 入力ディレクトリからの相対パスを保持
            if recursive:
                rel_path = html_file.relative_to(input_path)
                # 相対パスのディレクトリ部分を作成
                rel_dir = output_path / rel_path.parent
                rel_dir.mkdir(exist_ok=True, parents=True)
                output_file = rel_dir / f"{html_file.stem}.md"
            else:
                output_file = output_path / f"{html_file.stem}.md"
            
            # 変換を実行
            result = convert_file(html_file, output_file)
            if result:
                success_count += 1
            else:
                failure_count += 1
    
    # 入力が単一のファイルの場合
    elif input_path.is_file() and input_path.suffix.lower() == '.html':
        # 出力が既存のディレクトリの場合
        if output_path.is_dir() or (not output_path.exists() and output_path.name == ""):
            output_path.mkdir(exist_ok=True, parents=True)
            output_file = output_path / f"{input_path.stem}.md"
        else:
            # 出力パスのディレクトリが存在しない場合は作成
            output_path.parent.mkdir(exist_ok=True, parents=True)
            output_file = output_path
        
        # 変換を実行
        result = convert_file(input_path, output_file)
        if result:
            success_count += 1
        else:
            failure_count += 1
    
    else:
        print(f"エラー: 指定されたパス '{input_path}' はHTMLファイルまたはディレクトリではありません。")
    
    return success_count, failure_count


def convert_file(html_file, output_file):
    """
    単一のHTMLファイルをMarkdownに変換する関数
    
    Args:
        html_file (Path): 入力HTMLファイルのパス
        output_file (Path): 出力Markdownファイルのパス
        
    Returns:
        bool: 変換が成功したかどうか
    """
    # markitdownコマンドを実行
    cmd = ["markitdown", str(html_file), "-o", str(output_file)]
    
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"変換成功: {html_file} -> {output_file}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"変換失敗: {html_file}")
        print(f"エラー: {e}")
        if e.stderr:
            print(f"エラー詳細: {e.stderr}")
        return False
    except FileNotFoundError:
        print("エラー: 'markitdown' コマンドが見つかりません。インストールされているか確認してください。")
        return False


def main():
    """
    メイン関数
    """
    parser = argparse.ArgumentParser(description='HTMLファイルをMarkdownに変換するツール')
    parser.add_argument('input', help='入力ディレクトリまたはHTMLファイル')
    parser.add_argument('-o', '--output', help='出力ディレクトリまたはファイル（デフォルト: 入力ディレクトリ内の "markdown" サブディレクトリ）')
    parser.add_argument('-r', '--recursive', action='store_true', help='サブディレクトリも再帰的に処理する')
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    
    # 出力パスの設定
    if args.output:
        output_path = Path(args.output)
    else:
        # デフォルトの出力パスを設定
        if input_path.is_dir():
            output_path = input_path / "markdown"
        else:
            output_path = input_path.with_suffix('.md')
    
    success_count, failure_count = convert_html_to_markdown(input_path, output_path, args.recursive)
    
    total = success_count + failure_count
    if total > 0:
        print(f"\n処理結果:")
        print(f"- 成功: {success_count} ファイル")
        print(f"- 失敗: {failure_count} ファイル")
        print(f"- 合計: {total} ファイル")
    else:
        print("\n処理対象のファイルがありませんでした。")


if __name__ == "__main__":
    main()
