-- Create a table for coffee drinks
CREATE OR REPLACE TABLE videos-408723.sample_data.coffee_table (
    drink_name STRING,     -- coffee drink available at Starbucks
    coffee_type STRING,    -- Type of coffee (e.g., espresso, latte, cappuccino)
    strength INT64,        -- Strength level (scale of 1 to 10, 10 being the strongest)
    sweetness INT64,       -- Sweetness level (scale of 1 to 10, 10 being the sweetest)
    customer_rating FLOAT64 -- Customer rating (scale of 1 to 10, 10 being the highest)
);

-- Insert sample data
INSERT INTO videos-408723.sample_data.coffee_table (drink_name, coffee_type, strength, sweetness, customer_rating)
VALUES
    ('Strong Espresso', 'Espresso', 9, 2, 8),
    ('Sweet Latte', 'Latte', 5, 8, 9),
    ('Perfect Cappuccino', 'Cappuccino', 7, 5, 8.8),
    ('Intense Latte', 'Latte', 10, 1, 8.7),
    ('Caramel Cappuccino', 'Cappuccino', 6, 9, 6.4),
    ('Classic Latte', 'Latte', 4, 4, 8.0),
    ('Mocha Madness', 'Mocha', 8, 7, 9.6),
    ('Mocha Light', 'Mocha', 8, 4, 7.7);
