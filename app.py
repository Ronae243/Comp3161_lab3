from flask import Flask, request, make_response
import mysql.connector


app = Flask(__name__)






@app.route('/hello_world', methods=['GET'])
def hello_world():
    return "hello world"






@app.route('/customers', methods=['GET'])
def get_students():
    try:
        cnx = mysql.connector.connect(user='root', password='bfkraCtsWHi384',
                                host='localhost',
                                database='uwi3')
        cursor = cnx.cursor()
        cursor.execute('SELECT * from Customers')
        customer_list = []
        for customer_id, gender, age, annual_income, spending_score, profession, work_experience, family_size in cursor:
            customer = {}
            customer['CustomerID'] = customer_id 
            customer['Gender'] = gender
            customer['Age'] = age
            customer['AnnualIncome'] = annual_income
            customer['SpendingScore'] = spending_score
            customer['Profession'] = profession
            customer['WorkExperience'] = work_experience
            customer['FamilySize'] = family_size
         

            customer_list.append(customer)
        cursor.close()
        cnx.close()
        return make_response(customer_list, 200)
    except Exception as e:
        return make_response({'error': str(e)}, 400)

@app.route('/customer/<customer_id>', methods=['GET'])
def get_customer(customer_id):
    try:
        cnx = mysql.connector.connect(user='root', password='bfkraCtsWHi384',
                                host='localhost',
                                database='uwi3')
        cursor = cnx.cursor()
        cursor.execute(f"SELECT * from Customers WHERE CustomerID={customer_id}")
        row = cursor.fetchone()
        customer = {}
        if row is not None:
            customer_id, gender, age, annual_income, spending_score, profession, work_experience, family_size  = row
            customer = {}
            customer['CustomerID'] = customer_id 
            customer['Gender'] = gender
            customer['Age'] = age
            customer['AnnualIncome'] = annual_income
            customer['SpendingScore'] = spending_score
            customer['Profession'] = profession
            customer['WorkExperience'] = work_experience
            customer['FamilySize'] = family_size
            cursor.close()
            cnx.close()
            return make_response(customer, 200)
        else:
            return make_response({'error': 'Customer not found'}, 400)
    except:
        return make_response({'error': 'An error has occured'}, 400)

@app.route('/add_customer', methods=['POST'])
def add_customer():
    try:
        cnx = mysql.connector.connect(user='root', password='bfkraCtsWHi384',
                                    host='localhost',
                                    database='uwi3')
        cursor = cnx.cursor()
        content = request.json
        id = content['CustomerID']
        gender = content['Gender']
        age = content['Age']
        annual_income = content['AnnualIncome']
        spending_score = content['SpendingScore']
        profession = content['Profession']
        work_experience = content['WorkExperience']
        family_size = content['FamilySize']
        cursor.execute(f"INSERT INTO Customers VALUES('{id}','{gender}','{age}','{annual_income}','{spending_score}','{profession}','{work_experience}','{family_size}')")
        cnx.commit()
        cursor.close()
        cnx.close()
        return make_response({"success" : "Customer added"}, 201)
    except Exception as e:
        print(e)
        return make_response({'error': 'An error has occured'}, 400)

@app.route('/update_profession/<customer_id>', methods=['PUT'])
def update_profession(customer_id):
    try:
        cnx = mysql.connector.connect(user='root', password='bfkraCtsWHi384',
                                        host='localhost',
                                        database='uwi3')
        cursor = cnx.cursor()
        content = request.json
        profession = content['Profession']
        cursor.execute(f"UPDATE Customers SET Profession='{profession}' WHERE CustomerID={customer_id}")
        cnx.commit()
        cursor.close()
        return make_response({"success" : "Customer updated"}, 202)
    except Exception as e:
        return make_response({'error': str(e)}, 400)

@app.route('/highest_income_report', methods=['GET'])
def get_highest_income_report():
    try:
        cnx = mysql.connector.connect(user='root', password='bfkraCtsWHi384',
                                host='localhost',
                                database='uwi3')
        cursor = cnx.cursor()
        cursor.execute('SELECT CustomerID, Profession, MAX(`Annual_Income`) as `Highest Income` FROM Customers GROUP BY Profession')
        customer_list = []
        for customer_id, profession, max_annual_income in cursor:
            customer = {}
            customer['CustomerID'] = customer_id
            customer['AnnualIncome'] = max_annual_income
            customer['Profession'] = profession
            customer_list.append(customer)
        cursor.close()
        cnx.close()
        return make_response(customer_list, 200)
    except Exception as e:
        return make_response({'error': str(e)}, 400)

@app.route('/total_income_report', methods=['GET'])
def get_total_income_report():
    try:
        cnx = mysql.connector.connect(user='root', password='bfkraCtsWHi384',
                                host='localhost',
                                database='uwi3')
        cursor = cnx.cursor()
        cursor.execute('SELECT Profession, SUM(`Annual_Income`) as `Total Income` FROM Customers GROUP BY Profession')
        customer_list = []
        for profession, tot_income in cursor:
            customer = {}
            customer['TotalIncome'] = tot_income
            customer['Profession'] = profession
            customer_list.append(customer)
        cursor.close()
        cnx.close()
        return make_response(customer_list, 200)
    except Exception as e:
        return make_response({'error': str(e)}, 400)

@app.route('/average_work_experience', methods=['GET'])
def get_average_work_experience():
    try:
        cnx = mysql.connector.connect(user='root', password='bfkraCtsWHi384',
                                host='localhost',
                                database='uwi3')
        cursor = cnx.cursor()
        cursor.execute('SELECT Profession, round(AVG(Work_Experience)) AS AvgWorkExperience FROM Customers WHERE Age < 35 AND Annual_Income > 50000 GROUP BY Profession')
        customer_list = []
        for profession, average_exp in cursor:
            customer = {}
            customer['AverageExperience'] = average_exp
            customer['Profession'] = profession
            customer_list.append(customer)
        cursor.close()
        cnx.close()
        return make_response(customer_list, 200)
    except Exception as e:
        return make_response({'error': str(e)}, 400)
   
@app.route('/average_spending_score/<profession>', methods=['GET'])
def get_average_spending_score(profession):
    try:
        cnx = mysql.connector.connect(user='root', password='bfkraCtsWHi384',
                                host='localhost',
                                database='uwi3')
        cursor = cnx.cursor()
        cursor.execute(f"SELECT Gender, round(AVG(`Spending_Score`)) as `Average Spending Score` FROM Customers WHERE Profession ='{profession}' GROUP BY Gender")
        customer_list = []
        for gender, average_spending_score in cursor:
            customer = {}
            customer['Gender'] = gender
            customer['AverageSpendingScore'] = average_spending_score
            customer_list.append(customer)
        cursor.close()
        cnx.close()
        return make_response(customer_list, 200)
    except Exception as e:
        return make_response({'error': str(e)}, 400)
   
if __name__ == '__main__':
    app.run(host="localhost", port=6000, debug=True)