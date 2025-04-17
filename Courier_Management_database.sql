create database courier_management_db;
use courier_management_db;

CREATE TABLE Customer (
    UserID INT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Password VARCHAR(255) NOT NULL,
    ContactNumber VARCHAR(20) NULL,
    Address TEXT NULL
);

-- Courier Table
CREATE TABLE Courier (
    CourierID INT PRIMARY KEY,
    UserID INT NOT NULL,  -- Foreign Key to Customer
    ServiceID INT NOT NULL,  -- Foreign Key to CourierServices
    SenderName VARCHAR(255) NOT NULL,
    SenderAddress TEXT NOT NULL,
    ReceiverName VARCHAR(255) NOT NULL,
    ReceiverAddress TEXT NOT NULL,
    Weight DECIMAL(5, 2) NOT NULL,
    Status VARCHAR(50) NOT NULL,
    TrackingNumber VARCHAR(20) UNIQUE NOT NULL,
    DispatchDate DATETIME NOT NULL,  
    DeliveryDate DATE,
    FOREIGN KEY (UserID) REFERENCES Customer(UserID),
    FOREIGN KEY (ServiceID) REFERENCES CourierServices(ServiceID)
);
-- CourierServices Table
CREATE TABLE CourierServices (
    ServiceID INT PRIMARY KEY,
    ServiceName VARCHAR(100) NOT NULL,
    Cost DECIMAL(8, 2) NOT NULL
);

-- Employee Table
CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    ContactNumber VARCHAR(20) NULL,
    Role VARCHAR(50) NOT NULL,
    Salary DECIMAL(10, 2) NOT NULL,
	ServiceId Int,
	FOREIGN KEY (ServiceId) REFERENCES CourierServices(ServiceID),
);

-- Location Table
CREATE TABLE Location (
    LocationID INT PRIMARY KEY,
    LocationName VARCHAR(100) NOT NULL,
    Address TEXT NOT NULL
);
-- Payment Table
CREATE TABLE Payment (
    PaymentID INT PRIMARY KEY,
    CourierID INT NOT NULL,
    LocationID INT NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    PaymentDate DATE NOT NULL,
    FOREIGN KEY (CourierID) REFERENCES Courier(CourierID),
    FOREIGN KEY (LocationID) REFERENCES Location(LocationID)
);

-- Inserting into Customer Table
INSERT INTO Customer (UserID, Name, Email, Password, ContactNumber, Address) VALUES
(101, 'John Doe', 'john.doe@email.com', 'password123', '1234567890', '123 Elm St'),
(102, 'Jane Smith', 'jane.smith@email.com', 'password456', '0987654321', '456 Oak St'),
(103, 'Alice Johnson', 'alice.johnson@email.com', 'password789', '1122334455', '789 Pine St'),
(104, 'Bob Brown', 'bob.brown@email.com', 'password012', '6677889900', '101 Maple St'),
(105, 'Charlie Davis', 'charlie.davis@email.com', 'password345', '2233445566', '202 Birch St');

-- Inserting into CourierServices Table
INSERT INTO CourierServices (ServiceID, ServiceName, Cost) VALUES
(1, 'Standard Delivery', 5.00),
(2, 'Express Delivery', 10.00),
(3, 'Overnight Shipping', 15.00),
(4, 'International Shipping', 20.00),
(5, 'Same Day Delivery', 25.00);

-- Inserting into Courier Table
INSERT INTO Courier (CourierID, UserID, ServiceID, SenderName, SenderAddress, ReceiverName, ReceiverAddress, Weight, Status, TrackingNumber, DispatchDate, DeliveryDate) VALUES
(1, 101, 1, 'John Doe', '123 West St', 'Mary Lee', '456 Oak St', 10.50, 'In Transit', 'TRK12345', '2025-04-01', NULL),
(2, 102, 2, 'Jane Smith', '456 Avenue St', 'Peter Green', '789 Pine St', 5.00, 'Delivered', 'TRK12346', '2025-03-25', '2025-03-28'),
(3, 103, 3, 'Alice Johnson', '789 Pine St', 'John Doe', '123 West St', 5.00, 'In Transit', 'TRK12389', '2025-04-10', '2025-04-15')

-- Inserting into Employee Table
INSERT INTO Employee (EmployeeID, Name, Email, ContactNumber, Role, Salary, ServiceId) VALUES
(1, 'Michael Clark', 'michael.clark@email.com', '2233445566', 'Courier Handler', 35000.00, 1),
(2, 'Sarah Adams', 'sarah.adams@email.com', '9988776655', 'Operations Manager', 55000.00, 2),
(3, 'David Wilson', 'david.wilson@email.com', '6677889900', 'Courier Driver', 40000.00, 3),
(4, 'Emily Davis', 'emily.davis@email.com', '1122334455', 'Customer Support', 30000.00, 4),
(5, 'James Miller', 'james.miller@email.com', '3344556677', 'Logistics Coordinator', 45000.00, 5);

-- Inserting into Location Table
INSERT INTO Location (LocationID, LocationName, Address) VALUES
(1, 'New York Office', '123 Broadway, New York, NY'),
(2, 'Los Angeles Office', '456 Sunset Blvd, Los Angeles, CA'),
(3, 'Chicago Office', '789 Michigan Ave, Chicago, IL'),
(4, 'San Francisco Office', '101 Golden Gate, San Francisco, CA'),
(5, 'Miami Office', '202 Ocean Dr, Miami, FL');

-- Inserting into Payment Table
INSERT INTO Payment (PaymentID, CourierID, LocationID, Amount, PaymentDate) VALUES
(1, 1, 1, 5.00, '2025-04-02'),
(2, 2, 2, 10.00, '2025-03-28')





SELECT * FROM Customer;
SELECT * FROM Courier;
SELECT * FROM CourierServices;
SELECT * FROM Employee;
SELECT * FROM Location;
SELECT * FROM Payment;
--
-- 1. List all customers:
SELECT * FROM Customer;

-- 2. List all orders for a specific customer:

SELECT * FROM Courier WHERE UserID = 101;

-- 3. List all couriers:
SELECT * FROM Courier;

-- 4. List all packages for a specific order:

SELECT * FROM Courier WHERE CourierID = 1;

-- 5. List all deliveries for a specific courier:

SELECT * FROM Courier WHERE TrackingNumber = 'TRK12345';

-- 6. List all undelivered packages:
SELECT * FROM Courier WHERE Status != 'Delivered';

-- 7. List all packages that are scheduled for delivery today:
SELECT * FROM Courier WHERE DeliveryDate = CAST(GETDATE() AS DATE);

-- 8. List all packages with a specific status:

SELECT * FROM Courier WHERE Status = 'In Transit';

-- 9. Calculate the total number of packages sent by each customer:
SELECT UserID, COUNT(*) AS TotalPackages 
FROM Courier 
GROUP BY UserID;

-- 10. Find the average delivery time (in days) for each customer:

SELECT UserID,AVG(DATEDIFF(DAY, DispatchDate, DeliveryDate)) AS AvgDeliveryDays 
FROM Courier 
WHERE DeliveryDate IS NOT NULL AND DispatchDate IS NOT NULL
GROUP BY UserID;

-- 11. List all packages with a specific weight range:

SELECT * FROM Courier WHERE Weight BETWEEN 5.0 AND 10.0;

-- 12. Retrieve employees whose names contain 'John':
SELECT * FROM Employee WHERE Name LIKE '%John%';

-- 13. Retrieve all courier records with payments greater than $50
SELECT C.*
FROM Courier C
JOIN Payment P ON C.CourierID = P.CourierID
WHERE P.Amount > 50;

-- 14. Find the total number of couriers handled by each employee.

SELECT E.EmployeeID, E.Name, COUNT(C.CourierID) AS TotalCouriers
FROM Employee E
JOIN CourierServices CS ON E.ServiceId = CS.ServiceID
JOIN Courier C ON C.ServiceID = CS.ServiceID
GROUP BY E.EmployeeID, E.Name;

-- 15. Calculate the total revenue generated by each location
SELECT L.LocationID, L.LocationName, SUM(P.Amount) AS TotalRevenue
FROM Payment P
JOIN Location L ON P.LocationID = L.LocationID
GROUP BY L.LocationID, L.LocationName;

-- 16. Find the total number of couriers delivered to each location

SELECT ReceiverAddress AS Location, COUNT(*) AS TotalDelivered
FROM Courier
WHERE Status = 'Delivered'
GROUP BY ReceiverAddress;

-- 17. Find the courier with the highest average delivery time
SELECT TOP 1
    CourierID,
    AVG(DATEDIFF(DAY, DispatchDate, DeliveryDate)) AS AvgDeliveryTime
FROM Courier
WHERE DeliveryDate IS NOT NULL
GROUP BY CourierID
ORDER BY AvgDeliveryTime DESC;

-- 18. Find locations with total payments less than a certain amount (e.g., 1000)
SELECT LocationID, SUM(Amount) AS TotalAmount
FROM Payment
GROUP BY LocationID
HAVING SUM(Amount) < 1000;

-- 19. Calculate total payments per location
SELECT LocationID, SUM(Amount) AS TotalPayments
FROM Payment
GROUP BY LocationID;

-- 20. Couriers with total payments > $1000 in a specific location (LocationID = 2)
SELECT CourierID, SUM(Amount) AS TotalAmount
FROM Payment
WHERE LocationID = 2
GROUP BY CourierID
HAVING SUM(Amount) > 1000;

-- 21. Couriers with payments > $1000 after a certain date
SELECT CourierID, SUM(Amount) AS TotalAmount
FROM Payment
WHERE PaymentDate > '2024-01-01'
GROUP BY CourierID
HAVING SUM(Amount) > 1000;

-- 22. Locations where total amount received > $5000 before a certain date
SELECT LocationID, SUM(Amount) AS TotalAmount
FROM Payment
WHERE PaymentDate < '2024-01-01'
GROUP BY LocationID
HAVING SUM(Amount) > 5000;

-- 23. Retrieve Payments with Courier Information
SELECT P.*, C.TrackingNumber, C.Status
FROM Payment P
INNER JOIN Courier C ON P.CourierID = C.CourierID;

-- 24. Retrieve Payments with Location Information
SELECT P.*, L.LocationName, L.Address
FROM Payment P
INNER JOIN Location L ON P.LocationID = L.LocationID;

-- 25. Payments with Courier and Location Info
SELECT P.PaymentID, P.Amount, P.PaymentDate, 
       C.TrackingNumber, C.Status, 
       L.LocationName
FROM Payment P
JOIN Courier C ON P.CourierID = C.CourierID
JOIN Location L ON P.LocationID = L.LocationID;

-- 26. List all payments with courier details
SELECT P.PaymentID, P.Amount, P.PaymentDate, C.TrackingNumber, C.Status
FROM Payment P
JOIN Courier C ON P.CourierID = C.CourierID;

-- 27. Total payments received for each courier
SELECT CourierID, SUM(Amount) AS TotalAmount
FROM Payment
GROUP BY CourierID;

-- 28. List payments made on a specific date (e.g., '2024-01-01')
SELECT *
FROM Payment
WHERE PaymentDate = '2024-01-01';

-- 29. Get Courier Information for Each Payment
SELECT P.PaymentID, P.Amount, C.*
FROM Payment P
JOIN Courier C ON P.CourierID = C.CourierID;

-- 30. Get Payment Details with Location
SELECT P.*, L.LocationName, L.Address
FROM Payment P
JOIN Location L ON P.LocationID = L.LocationID;

-- 31. Calculating Total Payments for Each Courier
SELECT CourierID, SUM(Amount) AS TotalPayments
FROM Payment
GROUP BY CourierID;

-- 32. List Payments Within a Date Range
SELECT *
FROM Payment
WHERE PaymentDate BETWEEN '2024-01-01' AND '2024-12-31';

-- 33. Users and Couriers (Full Outer Join)
SELECT C.*, Co.*
FROM Customer C
FULL OUTER JOIN Courier Co ON C.UserID = Co.UserID;

-- 34. Couriers and Services (Full Outer Join)
SELECT C.*, CS.*
FROM Courier C
FULL OUTER JOIN CourierServices CS ON C.ServiceID = CS.ServiceID;

-- 35. Employees and Payments (assuming via CourierServices -> Courier -> Payment)
SELECT E.*, P.*
FROM Employee E
LEFT JOIN Courier C ON C.ServiceID = E.ServiceId
LEFT JOIN Payment P ON C.CourierID = P.CourierID;

-- 36. All users and all courier services (Cross Join)
SELECT C.Name, CS.ServiceName
FROM Customer C
CROSS JOIN CourierServices CS;

-- 37. All employees and all locations (Cross Join)
SELECT E.Name AS EmployeeName, L.LocationName
FROM Employee E
CROSS JOIN Location L;

-- 38. Couriers with Sender Info
SELECT CourierID, SenderName, SenderAddress FROM Courier;

-- 39. Couriers with Receiver Info
SELECT CourierID, ReceiverName, ReceiverAddress FROM Courier;

-- 40. Couriers with Service Details
SELECT C.*, CS.ServiceName, CS.Cost
FROM Courier C
LEFT JOIN CourierServices CS ON C.ServiceID = CS.ServiceID;

-- 41. Employees and number of couriers assigned
SELECT E.EmployeeID, E.Name, COUNT(C.CourierID) AS NumCouriers
FROM Employee E
LEFT JOIN Courier C ON C.ServiceID = E.ServiceId
GROUP BY E.EmployeeID, E.Name;

-- 42. Locations and total payment amount
SELECT L.LocationID, L.LocationName, SUM(P.Amount) AS TotalAmount
FROM Location L
LEFT JOIN Payment P ON L.LocationID = P.LocationID
GROUP BY L.LocationID, L.LocationName;

-- 43. Couriers sent by same sender
SELECT *
FROM Courier
WHERE SenderName IN (
    SELECT SenderName
    FROM Courier
    GROUP BY SenderName
    HAVING COUNT(*) > 1
);

-- 44. Employees sharing the same role
SELECT *
FROM Employee
WHERE Role IN (
    SELECT Role
    FROM Employee
    GROUP BY Role
    HAVING COUNT(*) > 1
);

-- 45. Payments made for couriers from same location
SELECT P.*
FROM Payment P
JOIN Courier C ON P.CourierID = C.CourierID
WHERE SenderAddress IN (
    SELECT SenderAddress
    FROM Courier
    GROUP BY SenderAddress
    HAVING COUNT(*) > 1
);

-- 46. Couriers sent from same location
SELECT *
FROM Courier
WHERE SenderAddress IN (
    SELECT SenderAddress
    FROM Courier
    GROUP BY SenderAddress
    HAVING COUNT(*) > 1
);

-- 47. Employees and couriers they delivered (assuming status = 'Delivered')
SELECT E.EmployeeID, E.Name, COUNT(C.CourierID) AS DeliveredCouriers
FROM Employee E
LEFT JOIN Courier C ON E.ServiceId = C.ServiceID AND C.Status = 'Delivered'
GROUP BY E.EmployeeID, E.Name;

-- 48. Couriers paid more than service cost
SELECT C.CourierID, C.ServiceID, P.Amount, CS.Cost
FROM Courier C
JOIN Payment P ON C.CourierID = P.CourierID
JOIN CourierServices CS ON C.ServiceID = CS.ServiceID
WHERE P.Amount > CS.Cost;

-- 49. Couriers with weight greater than average
SELECT *
FROM Courier
WHERE Weight > (
    SELECT AVG(Weight) FROM Courier
);

-- 50. Employees with salary > average
SELECT *
FROM Employee
WHERE Salary > (
    SELECT AVG(Salary) FROM Employee
);

-- 51. Total cost of services less than max cost
SELECT SUM(Cost) AS TotalCost
FROM CourierServices
WHERE Cost < (
    SELECT MAX(Cost) FROM CourierServices
);

-- 52. All couriers that have been paid for
SELECT *
FROM Courier
WHERE CourierID IN (
    SELECT CourierID FROM Payment
);

-- 53. Locations with max payment amount
SELECT *
FROM Payment
WHERE Amount = (
    SELECT MAX(Amount) FROM Payment
);

-- 54. Couriers with weight greater than all couriers by a specific sender
SELECT *
FROM Courier
WHERE Weight > ALL (
    SELECT Weight FROM Courier WHERE SenderName = 'SenderName'
);
