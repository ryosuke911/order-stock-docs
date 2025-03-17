# テーブル定義書

## 商品テーブル (products)
| 項目名 | データ形式 | 制約 | 初期値 | 外部キー | 概要 |
|--------|------------|------|---------|-----------|------|
| product_code | TEXT | PRIMARY KEY | | | 商品コード |
| product_name | TEXT | NOT NULL | | | 商品名 |
| inventory_location | TEXT | | | | 在庫拠点 |
| inventory_upper_limit | INT | | 0 | | 在庫上限 |
| inventory_lower_limit | INT | | 0 | | 在庫下限 |

## 在庫テーブル (inventory)
| 項目名 | データ形式 | 制約 | 初期値 | 外部キー | 概要 |
|--------|------------|------|---------|-----------|------|
| id | UUID | PRIMARY KEY DEFAULT gen_random_uuid() | | | ID |
| product_code | TEXT | NOT NULL | | products.product_code | 商品コード |
| quantity | INT | NOT NULL | 0 | | 在庫数 |
| warehouse | TEXT | | | | 倉庫 |
| updated_at | TIMESTAMP | NOT NULL | NOW() | | 更新日時 |

## 発注テーブル (orders)
| 項目名 | データ形式 | 制約 | 初期値 | 外部キー | 概要 |
|--------|------------|------|---------|-----------|------|
| order_id | UUID | PRIMARY KEY DEFAULT gen_random_uuid() | | | 発注ID |
| product_code | TEXT | NOT NULL | | products.product_code | 商品コード |
| order_quantity | INT | NOT NULL | 0 | | 発注数量 |
| supplier | TEXT | | | | 発注先 |
| delivery_date | DATE | | | | 納期 |
| order_date | TIMESTAMP | NOT NULL | NOW() | | 発注日 |
| order_status | TEXT | | 発注済 | | 発注ステータス |
| supplier | TEXT | | | | 発注担当者 |

## 入庫テーブル (inbounds)
| 項目名 | データ形式 | 制約 | 初期値 | 外部キー | 概要 |
|--------|------------|------|---------|-----------|------|
| id | UUID | PRIMARY KEY DEFAULT gen_random_uuid() | | | 入庫ID |
| product_code | TEXT | NOT NULL | | products.product_code | 商品コード |
| inbound_quantity | INT | NOT NULL | 0 | | 入庫数量 |
| inbound_date | TIMESTAMP | NOT NULL | NOW() | | 入庫日 |
| warehouse | TEXT | | | | 倉庫 |

## 出庫テーブル (outbounds)
| 項目名 | データ形式 | 制約 | 初期値 | 外部キー | 概要 |
|--------|------------|------|---------|-----------|------|
| id | UUID | PRIMARY KEY DEFAULT gen_random_uuid() | | | 出庫ID |
| product_code | TEXT | NOT NULL | | products.product_code | 商品コード |
| outbound_quantity | INT | NOT NULL | 0 | | 出庫数量 |
| outbound_date | TIMESTAMP | NOT NULL | NOW() | | 出庫日 |
| warehouse | TEXT | | | | 倉庫 |

## 在庫移動テーブル (inventory_movements)
| 項目名 | データ形式 | 制約 | 初期値 | 外部キー | 概要 |
|--------|------------|------|---------|-----------|------|
| movement_id | UUID | PRIMARY KEY DEFAULT gen_random_uuid() | | | 移動ID |
| product_code | TEXT | NOT NULL | | products.product_code | 商品コード |
| quantity | INT | NOT NULL | 0 | | 移動数量 |
| source_warehouse | TEXT | | | | 移動元倉庫 |
| destination_warehouse | TEXT | | | | 移動先倉庫 |
| movement_date | TIMESTAMP | NOT NULL | NOW() | | 移動日 |

## サプライヤーテーブル (suppliers)
| 項目名 | データ形式 | 制約 | 初期値 | 外部キー | 概要 |
|--------|------------|------|---------|-----------|------|
| supplier_id | UUID | PRIMARY KEY DEFAULT gen_random_uuid() | | | サプライヤーID |
| supplier_name | TEXT | NOT NULL | | | サプライヤー名 |
| contact_info | TEXT | | | | 連絡先 |
| address | TEXT | | | | 住所 |

## ユーザーテーブル (users)
| 項目名 | データ形式 | 制約 | 初期値 | 外部キー | 概要 |
|--------|------------|------|---------|-----------|------|
| user_id | UUID | PRIMARY KEY DEFAULT gen_random_uuid() | | | ユーザーID |
| username | TEXT | NOT NULL | | | ユーザー名 |
| password | TEXT | NOT NULL | | | パスワード |
| role | TEXT | | 在庫管理担当者 | | ロール |

## アラートテーブル (alerts)
| 項目名 | データ形式 | 制約 | 初期値 | 外部キー | 概要 |
|--------|------------|------|---------|-----------|------|
| alert_id | UUID | PRIMARY KEY DEFAULT gen_random_uuid() | | | アラートID |
| product_code | TEXT | | | products.product_code | 商品コード |
| alert_type | TEXT | NOT NULL | | | アラート種類 |
| threshold | INT | | 0 | | 閾値 |
| message | TEXT | | | | メッセージ |
| created_at | TIMESTAMP | NOT NULL | NOW() | | 作成日時 |
