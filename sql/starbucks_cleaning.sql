/** script name: starbucks_cleaning.sql
    author: Carles Conesa
    date: 04/03/2026
    version: 1.0
    DBMS: PostgreSQL server */


CREATE OR REPLACE TABLE orders AS 
SELECT 
    order_date AS Order_Date,
    order_time[1:5] AS Order_Time,
    customer_id AS Customer_ID,
    order_id AS Order_ID,
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
    total_spend AS Sales_Amount,
    fulfillment_time_min AS Prep_Time_Min,
    drink_category AS Drink_Category,
    has_food_item AS Has_Food,
    order_ahead AS Ordered_Ahead,
    customer_satisfaction AS Customer_Satisfaction,
    1 AS Order_Count
FROM 'data/processed/starbucks_customer_ordering_patterns_cleaned.csv';
COPY (SELECT * FROM orders) TO 'data/processed/starbucks_final_report.csv' (HEADER, DELIMITER ',');