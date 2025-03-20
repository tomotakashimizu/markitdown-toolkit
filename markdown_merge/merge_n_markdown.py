"""
HTML & Markdown ツールキット - Markdown マージツール

複数のMarkdownファイルを指定数ごとにまとめて一つのファイルに結合するPythonスクリプト。
カスタム区切り文字、ヘッダー追加、柔軟なファイル選択オプションをサポートしています。
"""

import os
import glob
from pathlib import Path
import argparse
import re
from datetime import datetime


def merge_markdown_files(input_dir, output_dir=None, n=10, file_pattern="*.md", delimiter="___", 
                         include_header=False, prefix="merged", verbose=True):
    """
    指定されたディレクトリ内のMarkdownファイルをn個ずつまとめて新しいファイルを作成する
    
    Args:
        input_dir (str): 入力ディレクトリのパス
        output_dir (str, optional): 出力ディレクトリのパス（デフォルト: 入力ディレクトリと同じ）
        n (int): 一度にまとめるファイル数（デフォルト: 10）
        file_pattern (str): 対象とするファイルのパターン（デフォルト: "*.md"）
        delimiter (str): ファイル間の区切り文字（デフォルト: "___"）
        include_header (bool): 各ファイルの前にファイル名をヘッダーとして含めるかどうか
        prefix (str): 出力ファイル名のプレフィックス（デフォルト: "merged"）
        verbose (bool): 詳細な出力を表示するかどうか
    
    Returns:
        list: 作成されたファイルのパスのリスト
    """
    # 入力ディレクトリが存在するか確認
    input_path = Path(input_dir)
    if not input_path.exists() or not input_path.is_dir():
        if verbose:
            print(f"エラー: 指定されたディレクトリ '{input_dir}' が存在しないか、ディレクトリではありません。")
        return []
    
    # 出力ディレクトリの設定
    if output_dir:
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True, parents=True)
    else:
        output_path = input_path
    
    # Markdownファイルのリストを取得
    markdown_files = sorted(list(input_path.glob(file_pattern)))
    
    if not markdown_files:
        if verbose:
            print(f"エラー: 指定されたディレクトリ '{input_dir}' にパターン '{file_pattern}' に一致するファイルが見つかりません。")
        return []
    
    if verbose:
        print(f"合計 {len(markdown_files)} 個のファイルが見つかりました。")
    
    # ファイルをn個ずつのグループに分ける
    file_groups = [markdown_files[i:i+n] for i in range(0, len(markdown_files), n)]
    
    created_files = []
    
    # 各グループに対して処理を行う
    for i, group in enumerate(file_groups, 1):
        # 出力ファイル名を作成
        timestamp = datetime.now().strftime("%Y%m%d")
        output_file = output_path / f"{prefix}_{timestamp}_{i}.md"
        
        if verbose:
            print(f"グループ {i}: {len(group)} 個のファイルを '{output_file}' にマージします。")
        
        # 出力ファイルを作成
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for j, file_path in enumerate(group, 1):
                # ヘッダーを追加（オプション）
                if include_header:
                    outfile.write(f"# {file_path.stem}\n\n")
                
                # 入力ファイルの内容を読み込む
                with open(file_path, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                
                # 内容を出力ファイルに書き込む
                outfile.write(content)
                
                # 最後のファイル以外は区切り線と改行を追加
                if j < len(group):
                    outfile.write(f"\n\n{delimiter}\n\n")
        
        created_files.append(str(output_file))
        if verbose:
            print(f"ファイル '{output_file}' を作成しました。")
    
    if verbose:
        print(f"合計 {len(file_groups)} 個のマージされたファイルを作成しました。")
    
    return created_files


def main():
    # コマンドライン引数の解析
    parser = argparse.ArgumentParser(description='Markdownファイルをn個ずつまとめる')
    parser.add_argument('input', type=str, help='入力ディレクトリのパス')
    parser.add_argument('-o', '--output', type=str, help='出力ディレクトリのパス（デフォルト: 入力ディレクトリと同じ）')
    parser.add_argument('-n', type=int, default=10, help='一度にまとめるファイル数（デフォルト: 10）')
    parser.add_argument('-p', '--pattern', type=str, default="*.md", help='対象とするファイルのパターン（デフォルト: "*.md"）')
    parser.add_argument('-d', '--delimiter', type=str, default="___", help='ファイル間の区切り文字（デフォルト: "___"）')
    parser.add_argument('--prefix', type=str, default="merged", help='出力ファイル名のプレフィックス（デフォルト: "merged"）')
    parser.add_argument('--header', action='store_true', help='各ファイルの前にファイル名をヘッダーとして含める')
    parser.add_argument('-q', '--quiet', action='store_true', help='詳細な出力を抑制する')
    
    args = parser.parse_args()
    
    # Markdownファイルのマージを実行
    merge_markdown_files(
        input_dir=args.input, 
        output_dir=args.output, 
        n=args.n, 
        file_pattern=args.pattern, 
        delimiter=args.delimiter,
        include_header=args.header,
        prefix=args.prefix,
        verbose=not args.quiet
    )


if __name__ == "__main__":
    main()
