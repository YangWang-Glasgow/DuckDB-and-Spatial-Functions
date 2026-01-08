from pathlib import Path
import pandas as pd

# folder containing parquet files
data_dir = Path(r"C:\Users\yw30f\OneDrive - University of Glasgow\YangJob\Tutor\URBAN5160_2526\Block1\Part2\DuckDB-and-Spatial-Functions\Data7")

# output folder (recommended)
out_dir = data_dir / "filtered"
out_dir.mkdir(exist_ok=True)

# fields to keep (example – edit as needed)
FIELDS = ['id', 'listing_url', 'scrape_id', 'last_scraped', 'name', 'description',
       'neighborhood_overview', 'picture_url', 'host_id', 'host_url',
       'host_name', 'host_since', 'host_location', 'host_about',
       'host_response_time', 'host_response_rate', 'host_acceptance_rate',
       'host_is_superhost', 'host_thumbnail_url', 'host_picture_url',
       'host_neighbourhood', 'host_listings_count',
       'host_total_listings_count', 'host_verifications',
       'host_has_profile_pic', 'host_identity_verified', 'neighbourhood',
       'neighbourhood_cleansed', 'neighbourhood_group_cleansed', 'latitude',
       'longitude', 'property_type', 'room_type', 'accommodates', 'bathrooms',
       'bathrooms_text', 'bedrooms', 'beds', 'amenities', 'price',
       'minimum_nights', 'maximum_nights', 'minimum_minimum_nights',
       'maximum_minimum_nights', 'minimum_maximum_nights',
       'maximum_maximum_nights', 'minimum_nights_avg_ntm',
       'maximum_nights_avg_ntm', 'calendar_updated', 'has_availability',
       'availability_30', 'availability_60', 'availability_90',
       'availability_365', 'calendar_last_scraped', 'number_of_reviews',
       'number_of_reviews_ltm', 'number_of_reviews_l30d', 'first_review',
       'last_review', 'review_scores_rating', 'review_scores_accuracy',
       'review_scores_cleanliness', 'review_scores_checkin',
       'review_scores_communication', 'review_scores_location',
       'review_scores_value', 'instant_bookable',
       'calculated_host_listings_count',
       'calculated_host_listings_count_entire_homes',
       'calculated_host_listings_count_private_rooms',
       'calculated_host_listings_count_shared_rooms', 'reviews_per_month']

for parquet_file in data_dir.glob("*.parquet"):
    print(f"Processing {parquet_file.name}")

    df = pd.read_parquet(parquet_file)

    # keep only columns that actually exist (safe for schema drift)
    keep_cols = [c for c in FIELDS if c in df.columns]
    df_filtered = df[keep_cols]

    # write new parquet file
    out_path = out_dir / parquet_file.name
    df_filtered.to_parquet(out_path, index=False)

print("Done.")