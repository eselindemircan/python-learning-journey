SELECT ad_date, campaign_id, sum(spend)as maliyet,sum(impressions)as gosterim ,sum(clicks) as tiklanma,
sum("value") as total_value, sum(spend)::numeric/nullif(sum(clicks),0) as cpc,
(sum(spend)/nullif(sum(impressions),0)*1000) as cpm,
(sum(clicks)::numeric/nullif(sum(impressions),0)*100)as ctr,
(sum("value")-sum(spend))/nullif(sum(spend),0)as romi
FROM public.facebook_ads_basic_daily
group by ad_date, campaign_id;
