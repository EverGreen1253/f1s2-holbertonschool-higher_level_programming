-- creates table first_table if it does not exist
CREATE TABLE IF NOT EXISTS first_table(
    `id` INT PRIMARY KEY,
    `name` VARCHAR(256) NOT NULL
);