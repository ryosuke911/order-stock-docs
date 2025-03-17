import csv
import json
import os

def format_components(components):
    """構成要素を箇条書きに整形する"""
    if not components:
        return ''
    items = [item.strip() for item in components.split('、')]
    return '\n'.join(f'- {item}' for item in items)

def format_json_field(field):
    """JSONフィールドを整形する"""
    # 特殊なケースの処理
    if field in ['null', '無し', '']:
        return field
    
    # カンマ区切りのテキストの場合
    if '、' in field and not (field.startswith('[') or field.startswith('{')):
        items = [item.strip() for item in field.split('、')]
        return '\n'.join(f'- {item}' for item in items)

    try:
        # シングルクォートをダブルクォートに変換
        field = field.replace('"', '\\"').replace("'", '"')
        
        # JSONとしてパース
        data = json.loads(field)
        
        # 配列の場合
        if isinstance(data, list):
            # 空の配列
            if not data:
                return '[]'
            
            # シンプルな文字列配列
            if all(isinstance(item, str) for item in data):
                items = [f'- {item}' for item in data]
                return '\n'.join(items)
            
            # テーブル構造を持つ配列
            if all(isinstance(item, dict) and 'table' in item and 'items' in item for item in data):
                result = []
                for item in data:
                    table_name = item['table']
                    items = item['items']
                    result.append(f'- テーブル: `{table_name}`')
                    for field_name in items:
                        result.append(f'  - フィールド: `{field_name}`')
                return '\n'.join(result)
            
            # その他の配列
            return json.dumps(data, ensure_ascii=False, indent=2)
        
        # その他のJSONオブジェクト
        return json.dumps(data, ensure_ascii=False, indent=2)
    
    except json.JSONDecodeError:
        # JSON解析に失敗した場合は元の値を返す
        return field

def format_steps(steps):
    """操作手順を箇条書きに整形する"""
    if not steps:
        return ''
    
    # 数字付きリストの場合
    if any(line.strip().startswith(str(i)+'.') for i in range(1, 10) for line in steps.split('\n')):
        return steps
    
    # それ以外の場合は箇条書きに変換
    return '\n'.join(f'- {step.strip()}' for step in steps.split('\n') if step.strip())

def format_md(row):
    md_content = f"""# {row['画面名']}

## 基本情報
- ID: {row['id']}
- 分類: {row['分類']}
- 概要: {row['概要']}

## 構成要素
{format_components(row['構成要素'])}

## 操作手順
{format_steps(row['操作手順'])}

## アクセス権限
- 利用者: {row['利用者']}
- 権限: {row['権限']}

## 関連ファイル
- ファイル名: `{row['ファイル名']}`

### 入力
{format_json_field(row['入力'])}

### 出力
{format_json_field(row['出力'])}

### 共通コンポーネントファイル
{format_json_field(row['共通コンポーネントファイル'])}
"""
    return md_content

def ensure_directory_exists(directory):
    """ディレクトリが存在しない場合は作成する"""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

def main():
    base_dir = '/Users/ryosuke/Downloads/受託関連/受発注在庫管理システム/3.システム設計/6.画面定義書'
    csv_path = '/Users/ryosuke/Downloads/受託関連/受発注在庫管理システム/画面一覧.csv'
    
    files_created = 0
    files_updated = 0
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # IDからフォルダ名とファイル名を生成
            id_num = row['id'].replace('SCR-', '')
            screen_name = row['画面名']
            folder_name = f'SCR_{id_num}_{screen_name}'
            file_name = f'{id_num}_画面定義書.md'
            
            # フォルダのパスを生成
            folder_path = os.path.join(base_dir, folder_name)
            ensure_directory_exists(folder_path)
            
            # ファイルのパスを生成
            file_path = os.path.join(folder_path, file_name)
            
            # Markdown内容を生成
            md_content = format_md(row)
            
            # ファイルを書き込み
            is_new_file = not os.path.exists(file_path)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(md_content)
            
            if is_new_file:
                files_created += 1
            else:
                files_updated += 1
    
    print(f'処理が完了しました。')
    print(f'新規作成: {files_created}ファイル')
    print(f'更新: {files_updated}ファイル')

if __name__ == '__main__':
    main() 