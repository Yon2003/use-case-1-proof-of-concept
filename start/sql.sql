CREATE DATABASE Amusement_Park
USE Amusement_Park

//Таблица Visitor с техните данни 
create TABLE Visitors (
    VisitorID INT AUTOINCREMENT PRIMARY KEY,
    FName STRING,
    LName STRING,
    Age INT,
    PHONE STRING
);

//Таблица Ticket където има информация за самия билет и кой го е купил
CREATE TABLE Tickets(
 TicketID INT AUTOINCREMENT PRIMARY KEY,
 VisitorID INT,
 Type_Of_Ticket STRING,
 Price decimal(2,2),
 FOREIGN KEY (VisitorID) REFERENCES Visitor(VisitorID)
);

//Employer таблица в която пише за служителите и тяхната позиция и график за деня
Create or replace table Employers(
 EmployerID INT AUTOINCREMENT PRIMARY KEY,
 First_Name STRING,
 Last_Name STRING,
 Position_J STRING,
 Start_Shift TIME,
 End_Shift TIME
);

//местата на който работят служителите
create or replace table Department(
DepartmentID INT AUTOINCREMENT PRIMARY KEY,
EmployerID INT,
Department STRING,
FOREIGN KEY (EmployerID) REFERENCES Employer(EmployerID)
);

//самата атракция с описание за нея 
create or replace table Attractions(
AttractionID INT AUTOINCREMENT PRIMARY KEY,
Name_of_Attraction STRING,
TicketID INT,
Capacity_of_Attraction INT,
status STRING,
DepartmentID INT,
FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID)
);

//самото плащане за атракцията и детайли по това
create or replace table Payment (
PaymentID INT AUTOINCREMENT PRIMARY KEY,
VisitorID INT,
TicketID INT,
Amount DECIMAL(3,2),
Payment_Date TIME,
Payment_Method STRING,
FOREIGN KEY (VisitorID) REFERENCES Visitor(VisitorID),
FOREIGN KEY (TicketID) REFERENCES Ticket(TicketID)
);

//магазин/ресорант който ще бъде в една таблица 
create or replace table Shop(
ShopID INT AUTOINCREMENT PRIMARY KEY,
Name STRING,
Type STRING, //Дали е магазин или ресторанд
DepartmentID INT,
FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID)
);

//самото плащане и детайли в магазина/ресторанта
create or replace table Sale(
SaleID INT AUTOINCREMENT PRIMARY KEY,
VisitorID INT,
ShopID INT,
Total_Price DECIMAL(2,2),
Oreder_Time Time,
Payment STRING,
FOREIGN KEY (VisitorID) REFERENCES Visitor(VisitorID),
FOREIGN KEY (ShopID) REFERENCES Shop(ShopID)
);
