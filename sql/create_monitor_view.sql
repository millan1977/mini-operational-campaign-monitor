CREATE OR REPLACE VIEW public.line_item_snapshots_monitor AS
SELECT
    snapshot_id,
    line_item_id,
    snapshot_date,
    advertiser_id,
    advertiser_name,
    line_item_start_date,
    contracted_impressions,
    order_name,
    order_id,
    line_item_name,
    line_item_end_date,
    lifetime_impressions,
    trafficker_name,
    trafficker_id,
    status,
    total_days,
    elapsed_days,
    delivery_ratio,
    time_ratio,
    osi,
    CASE
        WHEN osi IS NULL THEN 'No observable'::text
        WHEN osi >= 0.95 THEN 'Bueno'::text
        WHEN osi >= 0.80 THEN 'Observable'::text
        ELSE 'Critico'::text
    END AS osi_kpi
FROM line_item_snapshots lis;