CREATE TABLE IF NOT EXISTS deli_products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type ENUM('animal source', 'vegetable', 'drinks', 'cleaning products') NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT NOT NULL
);

CREATE TABLE IF NOT EXISTS cart (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    quantity INT NOT NULL
);

INSERT IGNORE INTO deli_products (name, type, price, stock_quantity) VALUES
    ('Cheddar Cheese', 'animal source', 5.99, 50),
    ('Lettuce', 'vegetable', 1.49, 100),
    ('Orange Juice', 'drinks', 2.99, 75),
    ('Dish Soap', 'cleaning products', 3.49, 30),
    ('Salami', 'animal source', 7.99, 40),
    ('Tomato', 'vegetable', 0.99, 120),
    ('Soda', 'drinks', 1.49, 90),
    ('Paper Towels', 'cleaning products', 2.99, 50),
    ('Ham', 'animal source', 6.49, 35),
    ('Cucumber', 'vegetable', 0.79, 80),
    ('Water', 'drinks', 0.99, 100),
    ('All-Purpose Cleaner', 'cleaning products', 4.99, 25),
    ('Turkey', 'animal source', 8.99, 30),
    ('Carrot', 'vegetable', 0.69, 110),
    ('Milk', 'drinks', 2.49, 60),
    ('Dishwasher Detergent', 'cleaning products', 5.49, 20),
    ('Swiss Cheese', 'animal source', 6.99, 45),
    ('Spinach', 'vegetable', 1.29, 70),
    ('Tea', 'drinks', 1.99, 85),
    ('Glass Cleaner', 'cleaning products', 3.99, 40);

