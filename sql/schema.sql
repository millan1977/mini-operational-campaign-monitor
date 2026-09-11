CREATE TABLE IF NOT EXISTS public.line_item_snapshots (
    snapshot_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    line_item_id BIGINT NOT NULL,
    snapshot_date DATE NOT NULL,

    advertiser_id BIGINT,
    advertiser_name VARCHAR(255),

    line_item_start_date TIMESTAMP,
    contracted_impressions BIGINT,

    order_name VARCHAR(255),
    order_id BIGINT,

    line_item_name VARCHAR(255),
    line_item_end_date TIMESTAMP,

    lifetime_impressions BIGINT,

    trafficker_name VARCHAR(255),
    trafficker_id BIGINT,

    status VARCHAR(255),

    total_days INTEGER,
    elapsed_days INTEGER,

    delivery_ratio NUMERIC,
    time_ratio NUMERIC,
    osi NUMERIC,

    UNIQUE (line_item_id, snapshot_date)
);