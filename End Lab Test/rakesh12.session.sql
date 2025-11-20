-- MenuItems: Stores food and drink items
CREATE TABLE MenuItems (
    ItemID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    Description TEXT,
    Price DECIMAL(10,2) NOT NULL,
    Category VARCHAR(50)
);

-- Orders: Stores each customer order
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,
    OrderDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    CustomerName VARCHAR(100),
    TableNumber INT
);

-- OrderItems: Stores items within each order
CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY AUTO_INCREMENT,
    OrderID INT,
    ItemID INT,
    Quantity INT NOT NULL,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ItemID) REFERENCES MenuItems(ItemID)
);
-- Insert sample menu items
INSERT INTO MenuItems (Name, Description, Price, Category)
VALUES 
('Margherita Pizza', 'Classic cheese pizza', 299.00, 'Main Course'),
('Veg Burger', 'Grilled veggie patty with lettuce', 149.00, 'Main Course'),
('Lemonade', 'Fresh lemon drink', 59.00, 'Beverage');

-- Insert sample orders
INSERT INTO Orders (CustomerName, TableNumber, OrderDate)
VALUES 
('Amit Sharma', 2, '2025-11-20 10:00:00'),
('Priya Verma', 4, '2025-11-20 11:30:00');

-- Insert sample order items
INSERT INTO OrderItems (OrderID, ItemID, Quantity)
VALUES 
(1, 1, 1),  -- 1 Margherita Pizza
(1, 3, 2),  -- 2 Lemonades
(2, 2, 1);  -- 1 Veg Burger

INSERT INTO MenuItems (Name, Description, Price, Category)
VALUES ('Paneer Tikka', 'Spicy grilled paneer cubes', 199.00, 'Starter');

-- Step 1: Insert into Orders
INSERT INTO Orders (CustomerName, TableNumber)
VALUES ('Ravi Kumar', 5);

-- Step 2: Get the last inserted OrderID
SET @OrderID = LAST_INSERT_ID();

-- Step 3: Insert multiple items into OrderItems
INSERT INTO OrderItems (OrderID, ItemID, Quantity)
VALUES
(@OrderID, 1, 2),  -- 2 Margherita Pizzas
(@OrderID, 3, 1);  -- 1 Lemonade

SELECT SUM(mi.Price * oi.Quantity) AS TotalSalesToday
FROM Orders o
JOIN OrderItems oi ON o.OrderID = oi.OrderID
JOIN MenuItems mi ON oi.ItemID = mi.ItemID
WHERE DATE(o.OrderDate) = CURDATE();