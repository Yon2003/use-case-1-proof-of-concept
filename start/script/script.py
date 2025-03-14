from snowflake.snowpark import Session
import random
from datetime import time

def insert_visitors(session: Session):
    first_names = ["John", "Jane", "Alex", "Emily", "Chris", "Katie", "Michael", "Sarah", "David", "Laura"]
    last_names = ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin"]

    visitor_data = [
        (
            random.choice(first_names), 
            random.choice(last_names), 
            random.randint(5, 80), 
            f'+359-{random.randint(100,999)}-{random.randint(1000,9999)}'
        )
        for _ in range(1, 40)
    ]
    
    for fname, lname, age, phone in visitor_data:
        session.sql(f"""
            INSERT INTO Visitor (FName, LName, Age, PHONE) 
            VALUES ('{fname}', '{lname}', {age}, '{phone}')
        """).collect()
    
    print("Inserted visitor data successfully.")

def insert_employees(session: Session):
    first_names = ["John", "Jane", "Alex", "Emily", "Chris", "Katie", "Michael", "Sarah", "David", "Laura"]
    last_names = ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin"]
    positions = ["Manager", "Cashier", "Security", "Cleaner", "Technician"]

    employee_data = [
        (
            random.choice(first_names), 
            random.choice(last_names), 
            random.choice(positions), 
            time(random.randint(6, 14), random.choice([0, 30])),
            time(random.randint(15, 23), random.choice([0, 30]))
        )
        for _ in range(1, 20)
    ]
    
    for fname, lname, position, start_shift, end_shift in employee_data:
        session.sql(f"""
            INSERT INTO Employees (First_Name, Last_Name, Position_J, Start_Shift, End_Shift) 
            VALUES ('{fname}', '{lname}', '{position}', '{start_shift}', '{end_shift}')
        """).collect()
    
    print("Inserted employee data successfully.")

def insert_tickets(session: Session):
    ticket_types = ["Standard", "VIP", "Family", "Student", "Senior"]
    prices = {"Standard": 20, "VIP": 50, "Family": 45, "Student": 15, "Senior": 10}
    
    visitor_ids = [row.asDict()["VISITORID"] for row in session.sql("SELECT VisitorID FROM Visitor").collect()]
    
    if not visitor_ids:
        print("No visitors found. Skipping ticket insertion.")
        return
    
    ticket_data = [
        (
            random.choice(visitor_ids),
            ticket_type := random.choice(ticket_types),
            prices[ticket_type]
        )
        for _ in range(1, 30)
    ]
    
    for visitor_id, ticket_type, price in ticket_data:
        session.sql(f"""
            INSERT INTO Tickets (VisitorID, Type_Of_Ticket, Price) 
            VALUES ({visitor_id}, '{ticket_type}', {price})
        """).collect()
    
    print("Inserted ticket data successfully.")

def insert_departments(session: Session):
    departments = ["Rides", "Security", "Maintenance", "Food Services", "Guest Relations"]
    
    employee_ids = [row.asDict()["EMPLOYEEID"] for row in session.sql("SELECT EmployeeID FROM Employees").collect()]
    
    if not employee_ids:
        print("No employees found. Skipping department insertion.")
        return
    
    department_data = [
        (
            random.choice(employee_ids),
            random.choice(departments)
        )
        for _ in range(1, len(employee_ids) + 1)
    ]
    
    for employee_id, department in department_data:
        session.sql(f"""
            INSERT INTO Departments (EmployeeID, Department) 
            VALUES ({employee_id}, '{department}')
        """).collect()
    
    print("Inserted department data successfully.")


def insert_attractions(session: Session):
    attraction_names = ["Roller Coaster", "Ferris Wheel", "Haunted House", "Bumper Cars", "Water Slide"]
    statuses = ["Open", "Closed", "Maintenance"]
    
    department_ids = [row.asDict()["DEPARTMENTID"] for row in session.sql("SELECT DepartmentID FROM Departments").collect()]
    ticket_ids = [row.asDict()["TICKETID"] for row in session.sql("SELECT TicketID FROM Tickets").collect()]
    
    if not department_ids:
        print("No departments found. Skipping attraction insertion.")
        return
    
    attraction_data = [
        (
            name := random.choice(attraction_names),
            random.choice(ticket_ids) if ticket_ids else "NULL",
            random.randint(10, 50),  # Capacity
            random.choice(statuses),
            random.choice(department_ids)
        )
        for _ in range(1, 15)
    ]
    
    for name, ticket_id, capacity, status, department_id in attraction_data:
        ticket_value = "NULL" if ticket_id == "NULL" else ticket_id 
        session.sql(f"""
            INSERT INTO Attractions (Name_of_Attraction, TicketID, Capacity_of_Attraction, Status, DepartmentID) 
            VALUES ('{name}', {ticket_value}, {capacity}, '{status}', {department_id})
        """).collect()
    
    print("Inserted attraction data successfully.")

def main(session: Session):
    insert_visitors(session)
    insert_employees(session)
    insert_tickets(session)
    insert_departments(session)
    insert_attractions(session)
    
    
    return session.create_dataframe([("Success",)], schema=["Status"])
