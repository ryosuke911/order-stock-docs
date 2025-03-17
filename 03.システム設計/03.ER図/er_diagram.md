```mermaid
erDiagram
    products {
        TEXT product_code PK
        TEXT product_name
        TEXT inventory_location
        INT inventory_upper_limit
        INT inventory_lower_limit
    }
    inventory {
        UUID id PK
        TEXT product_code FK
        INT quantity
        TEXT warehouse
        TIMESTAMP updated_at
    }
    orders {
        UUID order_id PK
        TEXT product_code FK
        INT order_quantity
        TEXT supplier
        DATE delivery_date
        TIMESTAMP order_date
        TEXT order_status
        TEXT order_supplier
    }
    inbounds {
        UUID id PK
        TEXT product_code FK
        INT inbound_quantity
        TIMESTAMP inbound_date
        TEXT warehouse
    }
    outbounds {
        UUID id PK
        TEXT product_code FK
        INT outbound_quantity
        TIMESTAMP outbound_date
        TEXT warehouse
    }
    users {
        UUID user_id PK
        TEXT username
        TEXT password
        TEXT role
    }
    alerts {
        UUID alert_id PK
        TEXT product_code FK
        TEXT alert_type
        INT threshold
        TEXT message
        TIMESTAMP created_at
    }
    suppliers {
        UUID supplier_id PK
        TEXT supplier_name
        TEXT contact_info
        TEXT address
    }
    inventory_movements {
        UUID movement_id PK
        TEXT product_code FK
        INT quantity
        TEXT source_warehouse
        TEXT destination_warehouse
        TIMESTAMP movement_date
    }
    products ||--o{ inventory : "has"
    products ||--o{ orders : "is ordered"
    products ||--o{ inbounds : "is received"
    products ||--o{ outbounds : "is shipped"
    products ||--o{ alerts : "generates"
    products ||--o{ inventory_movements : "is moved"