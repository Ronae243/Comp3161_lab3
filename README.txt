1.First run the Customer.sql script in mysql workbench to create the database and the table Customers

2.Next run the csv_to_db.sql script in mysql workbench to import the csv data to the table Customers in the database.

3.Finally in the app.py file do the following in your terminal to run it: 


-----------Step 1 - Setup and activate a virtual environment----------------

Navigate to the folder with the code you just cloned and setup a virtual environment. cd Comp3161_lab3 Next in your terminal do the following python -m venv venv or python3 -m venv venv (if you have both Python 2 and Python 3)

-------Activate the environment---------------- source venv/bin/activate or .\venv\Scripts\activate (if using Windows) Step 3 - Install Flask Install Flask by running the following command: pip install Flask pip install mysql-connector-python



---------------------------Step 2 run flask app-------------------------------------

To run the flask app in the app.py file use the command python app.py in the terminal.