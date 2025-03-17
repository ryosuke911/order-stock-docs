# バックエンド処理一覧

| ID | 分類 | 処理名 | 概要 | 操作手順 | ファイル名 | 関連する画面名 | HTTPメソッド | ルートパス |
|---|---|---|---|---|---|---|---|---|
| bac-001 | 在庫情報管理 | 商品マスタ登録 | 商品コード、商品名、在庫拠点、在庫上限・下限などの基本情報を登録する。 | APIに商品コード、商品名、在庫拠点、在庫上限、在庫下限をPOSTする。 | product-master-register.ts | SCR-001 | POST | /api/products |
| bac-002 | 在庫情報管理 | 商品マスタ更新 | 登録済みの商品マスタ情報を更新する。 | APIに商品コードと更新項目（商品名、在庫拠点、在庫上限、在庫下限など）をPUTする。 | product-master-update.ts | SCR-003 | PUT | /api/products/{product_code} |
| bac-003 | 在庫情報管理 | 在庫数変動履歴検索 | 在庫数の変動履歴を検索する。 | APIに検索条件（期間、商品コード、担当者など)をGETで送信する。 | inventory-history-search.ts | SCR-005 | GET | /api/inventory-movements |
| bac-004 | 在庫情報管理 | 商品情報検索 | 商品コード、商品名などで商品情報を検索する。 | APIに検索キーワードをGETで送信する。 | product-search.ts | SCR-007 | GET | /api/products/search |
| bac-005 | 在庫情報管理 | 倉庫別在庫情報取得 | 倉庫別の在庫情報を取得する。 | APIに倉庫名を指定してGETする。 | warehouse-inventory.ts | SCR-010 | GET | /api/inventory/warehouse/{warehouse} |
| bac-006 | 入出庫管理 | 入庫登録 | 倉庫への商品の入庫を登録する。 | APIに入庫情報をPOSTする。 | inbound-register.ts | SCR-012 | POST | /api/inbounds |
| bac-007 | 入出庫管理 | 出庫登録 | 倉庫からの商品の出庫を登録する。 | APIに出庫情報をPOSTする。 | outbound-register.ts | SCR-013 | POST | /api/outbounds |
| bac-008 | 発注管理 | 発注データ登録 | 発注先、発注数量、納期などの発注データを登録する。 | APIに発注データをPOSTする。 | order-register.ts | SCR-011 | POST | /api/orders |
| bac-009 | 在庫移動管理 | 在庫移動登録 | 倉庫間の在庫移動を登録する。 | APIに在庫移動データをPOSTする。 | inventory-movement-registration.ts | SCR-028 | POST | /api/inventory-movements |
| bac-010 | 在庫調整管理 | 在庫調整登録 | 棚卸しなどによる在庫調整を登録する。 | APIに在庫調整データをPOSTする。 | inventory-adjustment-registration.ts | SCR-031 | POST | /api/inventory-adjustments |
| bac-011 | アラート機能 | アラート通知設定 | アラートの通知先（メール、チャットツールなど）を設定する。 | APIにアラートの種類と通知先をPOSTする。 | alert-notification-settings.ts | SCR-040 | POST | /api/alerts/settings |
| bac-012 | アラート機能 | 在庫アラート設定 | 在庫に関するアラートの種類と条件を設定する。 | APIにアラートの種類と条件をPOSTする。 | inventory-alert-settings.ts | SCR-042 | POST | /api/inventory/alerts/settings |
| bac-013 | アクセス権限管理 | ユーザー登録 | システム利用者のユーザーアカウントを登録する。 | APIにユーザーID、パスワード、権限をPOSTする。 | register-user.ts | SCR-046 | POST | /api/users |
| bac-014 | アクセス権限管理 | ユーザー権限設定 | ユーザーのメニューやデータの閲覧・編集権限を設定する。 | APIにユーザーIDと権限をPUTする。 | set-user-permissions.ts | SCR-047 | PUT | /api/users/{user_id}/permissions |
| bac-015 | アクセス権限管理 | 操作ログ検索 | 操作ログを検索する。 | APIに検索条件（ユーザーID、期間、操作の種類など)をGETで送信する。 | search-operation-logs.ts | SCR-048 | GET | /api/operation-logs |
| bac-016 | 発注管理 | 発注データ更新 | 登録済みの発注データを更新する。 | APIに発注IDと更新内容をPUTする。 | [orderId]-edit.ts | SCR-052 | PUT | /api/orders/{orderId} |
| bac-017 | 発注管理 | 発注データ取得 | 発注データを取得する。 | APIに発注IDをGETする。 | [orderId]-detail.ts | SCR-058 | GET | /api/orders/{orderId} |
| bac-018 | 発注管理 | 発注承認 | 発注を承認する。 | APIに発注IDと承認ステータスをPUTする。 | order-approval.ts | SCR-060 | PUT | /api/orders/{orderId}/approve |
| bac-019 | 発注管理 | 発注却下 | 発注を却下する。 | APIに発注IDと却下理由をPUTする。 | order-rejection.ts | SCR-061 | PUT | /api/orders/{orderId}/reject |
| bac-020 | 発注管理 | サプライヤー登録 | サプライヤー情報を登録する。 | APIにサプライヤー名、連絡先、住所をPOSTする。 | supplier-registration.ts | SCR-062 | POST | /api/suppliers |
| bac-021 | 発注管理 | サプライヤー検索 | サプライヤー情報を検索する。 | APIにサプライヤー名をGETで送信する。 | supplier-search.ts | SCR-064 | GET | /api/suppliers/search |
| bac-022 | 発注管理 | サプライヤー詳細取得 | サプライヤー詳細情報を取得する。 | APIにサプライヤーIDを指定してGETする。 | [supplierId]-detail.ts | SCR-066 | GET | /api/suppliers/{supplierId} |
| bac-023 | 操作ログ記録 | 操作ログ記録 | ユーザーの操作ログを記録する。 | APIに操作ログをPOSTする。 | N/A | N/A | POST | /api/operation-logs |
