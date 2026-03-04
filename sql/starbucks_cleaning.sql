CREATE OR REPLACE TABLE orders AS 
SELECT 
    customer_id AS Customer_ID,
    order_id AS Order_ID,
    order_date AS Order_Date,
    order_time AS Order_Time,
    day_of_week AS Day_of_Week,
    order_channel AS Order_Channel,
    store_id AS Store_ID,
    store_location_type AS Store_Location_Type,
    region AS Region,
    customer_age_group AS Age_Group,
    customer_gender AS Gender,
    is_rewards_member AS Rewards_Member,
    cart_size AS Cart_Size,
    num_customizations AS Num_Customizations,
    total_spend AS Total_Spend,
    fulfillment_time_min AS Prep_Time_Min,
    drink_category AS Drink_Category,
    has_food_item AS Has_Food,
    order_ahead AS Ordered_Ahead,
    customer_satisfaction AS Customer_Satisfaction
FROM 'data/processed/starbucks_customer_ordering_patterns_cleaned.csv';
COPY (SELECT * FROM orders) TO 'data/processed/starbucks_cleaned_sql.csv' (HEADER, DELIMITER ',');