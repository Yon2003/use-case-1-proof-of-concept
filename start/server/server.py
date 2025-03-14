from flask import Flask, jsonify, request, abort
from snowflake.snowpark import Session


SNOWFLAKE_CONFIG = {
    "account": "your_account",
    "user": "your_user",
    "password": "your_password",
    "warehouse": "your_warehouse",
    "database": "your_database",
    "schema": "your_schema",
    "role": "your_role"
}

def get_snowflake_session():
    return Session.builder.configs(SNOWFLAKE_CONFIG).create()

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Amusement Park API!"

@app.route('/attractions', methods=['GET'])
def get_attractions():
    session = get_snowflake_session()
    df = session.sql("SELECT * FROM ATTRACTIONS").collect()
    session.close()
    return jsonify([row.as_dict() for row in df])

@app.route('/attractions/<int:id>', methods=['GET'])
def get_attraction(id):
    session = get_snowflake_session()
    df = session.sql(f"SELECT * FROM ATTRACTIONS WHERE ATTRACTIONID = {id}").collect()
    session.close()
    if df:
        return jsonify(df[0].as_dict())
    else:
        abort(404)


from datetime import time


@app.route('/employees', methods=['GET'])
def get_employees():
    session = get_snowflake_session()
    try:
        df = session.sql("SELECT * FROM EMPLOYEES").collect()
        session.close()

        if df:
            employees = []
            for row in df:
                row_dict = row.as_dict()

                if isinstance(row_dict["START_SHIFT"], time):
                    row_dict["START_SHIFT"] = row_dict["START_SHIFT"].strftime("%H:%M:%S")
                if isinstance(row_dict["END_SHIFT"], time):
                    row_dict["END_SHIFT"] = row_dict["END_SHIFT"].strftime("%H:%M:%S")

                employees.append(row_dict)

            return jsonify(employees)
        else:
            abort(404)

    except Exception as e:
        print(f"Error fetching employees: {str(e)}")
        abort(500)


@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    session = get_snowflake_session()
    try:
        df = session.sql(f"SELECT * FROM EMPLOYEES WHERE EMPLOYEEID = {id}").collect()
        session.close()

        if df:
            row_dict = df[0].as_dict()

            if isinstance(row_dict.get("START_SHIFT"), time):
                row_dict["START_SHIFT"] = row_dict["START_SHIFT"].strftime("%H:%M:%S")
            if isinstance(row_dict.get("END_SHIFT"), time):
                row_dict["END_SHIFT"] = row_dict["END_SHIFT"].strftime("%H:%M:%S")

            return jsonify(row_dict)
        else:
            abort(404)

    except Exception as e:
        print(f"Error fetching employee {id}: {str(e)}")
        abort(500)


@app.route('/sale', methods=['GET'])
def get_sale():
    session = get_snowflake_session()
    df = session.sql("SELECT * FROM SALE").collect()
    session.close()
    return jsonify([row.as_dict() for row in df])

@app.route('/sale/<int:id>', methods=['GET'])
def get_sales(id):
    session = get_snowflake_session()
    df = session.sql(f"SELECT * FROM SALE WHERE SALEID = {id}").collect()
    session.close()
    if df:
        return jsonify(df[0].as_dict())
    else:
        abort(404)

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
