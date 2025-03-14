// Таблица Visitor с техните данни 
CREATE OR REPLACE TABLE Visitor (
    VisitorID INT AUTOINCREMENT PRIMARY KEY,
    First_Name STRING,
    Last_Name STRING,
    Age INT,
    PHONE STRING
);

// Таблица Employees, която съдържа информация за служителите, тяхната позиция и график за деня
CREATE OR REPLACE TABLE Employees (
    EmployeeID INT AUTOINCREMENT PRIMARY KEY,
    First_Name STRING,
    Last_Name STRING,
    Position_J STRING,
    Start_Shift TIME,
    End_Shift TIME
);

// Таблица Ticket, която съдържа информация за самия билет и кой го е купил
CREATE OR REPLACE TABLE Tickets (
    TicketID INT AUTOINCREMENT PRIMARY KEY,
    VisitorID INT,
    Type_Of_Ticket STRING,
    Price DECIMAL(6,2),
    FOREIGN KEY (VisitorID) REFERENCES Visitor(VisitorID)
);

// Местата, на които работят служителите
CREATE OR REPLACE TABLE Departments (
    DepartmentID INT AUTOINCREMENT PRIMARY KEY,
    EmployeID INT,
    Department STRING,
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

// Самата атракция с описание за нея 
CREATE OR REPLACE TABLE Attractions (
    AttractionID INT AUTOINCREMENT PRIMARY KEY,
    Name_of_Attraction STRING,
    TicketID INT,
    Capacity_of_Attraction INT,
    Status STRING,
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

// Самото плащане за атракцията и детайли по това
CREATE OR REPLACE TABLE Payment (
    PaymentID INT AUTOINCREMENT PRIMARY KEY,
    VisitorID INT,
    TicketID INT,
    Amount DECIMAL(6,2),
    Payment_Date TIME,
    Payment_Method STRING,
    FOREIGN KEY (VisitorID) REFERENCES Visitor(VisitorID),
    FOREIGN KEY (TicketID) REFERENCES Tickets(TicketID)
);

// Магазин/ресторант, който ще бъде в една таблица 
CREATE OR REPLACE TABLE Shop (
    ShopID INT AUTOINCREMENT PRIMARY KEY,
    Name STRING,
    Type STRING, // Дали е магазин или ресторант
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

// Самото плащане и детайли в магазина/ресторанта
CREATE OR REPLACE TABLE Sale (
    SaleID INT AUTOINCREMENT PRIMARY KEY,
    VisitorID INT,
    ShopID INT,
    Total_Price DECIMAL(10,2),
    Order_Time TIMESTAMP,
    Payment STRING,
    FOREIGN KEY (VisitorID) REFERENCES Visitor(VisitorID),
    FOREIGN KEY (ShopID) REFERENCES Shop(ShopID)
);

SELECT * FROM Tickets;
SELECT * FROM Attractions;
SELECT * FROM Visitor;
SELECT * FROM Employees;
SELECT * FROM department;
select * from sale

SHOW WAREHOUSES;
