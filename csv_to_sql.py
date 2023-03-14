import csv

with open('Customers.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    
    # Connect to MySQL database
    import mysql.connector
    mydb = mysql.connector.connect(user='root', password='bfkraCtsWHi384',
                                host='localhost',
                                database='uwi3')
    
    mycursor = mydb.cursor()

    for row in csv_reader:
        if line_count == 0:
            # Skip header row
            line_count += 1
        else:
            # Generate insert query
            customer_id = int(row[0])
            gender = row[1]
            age = int(row[2])
            annual_income = int(row[3])
            spending_score = int(row[4])
            profession = row[5]
            work_experience = int(row[6])
            family_size = int(row[7])

            
            sql = "INSERT INTO Customers (CustomerID, Gender, Age, Annual_Income, Spending_Score, Profession, Work_Experience, Family_Size) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (customer_id,  gender, age, annual_income, spending_score, profession, work_experience, family_size )
            mycursor.execute(sql, val)

            line_count += 1

    # Commit changes to database
    mydb.commit()

    print(f'Processed {line_count-1} records.')
