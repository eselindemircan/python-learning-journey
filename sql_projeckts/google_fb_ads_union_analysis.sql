select *
from google_ads_basic_daily 
union all 
select *
from facebook_ads_basic_daily;

SELECT 
    'google_ads' AS media_source,
    *
FROM google_ads_basic_daily

UNION ALL

SELECT 
    'facebook_ads' AS media_source,
    *
FROM facebook_ads_basic_daily;

----hesaplama----------

SELECT
    'google_ads' AS media_source,
    ad_date,
    SUM(spend) AS toplam_maliyet,
    SUM(impressions) AS toplam_gosterim,
    SUM(clicks) AS toplam_tiklama,
    SUM("value") as conversation_value
FROM google_ads_basic_daily
GROUP BY media_source, ad_date  

UNION ALL

SELECT
    'facebook_ads' AS media_source,
    ad_date,
    SUM(spend) AS toplam_maliyet,
    SUM(impressions) AS toplam_gosterim,
    SUM(clicks) AS toplam_tiklama,
    SUM("value") as conversation_value
FROM facebook_ads_basic_daily
GROUP BY media_source, ad_date  
ORDER BY media_source, ad_date;


