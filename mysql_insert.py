from datetime import date, datetime
import random
import mysql.connector

def createConnection(user_name, database_name, user_password, host, port):
    """Creates a connection to the mysql database
    
    Parameters
    -----------
        user_name {string} -- The username to the database
        database_name {string} -- The name of the database
        user_password {string} -- The password to the database
        host {string} -- The host of the database
        port {string} -- The port of the database

    Returns
    --------
        tuple -- A tuple containing the connection and the cursor
    """
    cnx = mysql.connector.connect(user=user_name, database=database_name, password=user_password, host=host, port=port)
    cursor = cnx.cursor()
    return (cnx, cursor)

def select_data():
    """Selects all the data from the database"""
    try:
        # Create a connection to the database
        cnx, cursor = createConnection('root', 'iot_situacionproblema', 'R0drigo,1805', 'localhost','3306') #AGREGAR PSSWRD

        # Query the database
        query = ("SELECT * FROM dht_data")

        # Execute the query
        cursor.execute(query)

        # Get the data
        data = cursor.fetchall()

        # Return the data
        return data
    
    except mysql.connector.Error as err:
        """Handle possible errors"""
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    finally:
        """Close the connection"""
        if ('cnx' in locals() or 'cnx' in globals()) and ('cursor' in locals() or 'cursor' in globals()):
            cnx.close()
            cursor.close()

def insert_data():
    """Inserts random sensor data into the database"""
    try:
        # TODO: Create random data that represents sensor data
        # For the float values, use the random.uniform() function.
        # Humidity: 0 to 100%, +-5%.
        # Temperature: 0 to 100%, +-5%.
        # Date/Time: Current date and time. Check the datetime module for help.
        # When you have the data, print it out to the console. 

        humidity = random.uniform(0, 100)  
        temperature = random.uniform(0, 100)  
        current_date_time = datetime.now()  
        print(f"Humidity: {humidity}, Temperature: {temperature}, DateTime: {current_date_time}")

        # Create a connection to the database
        # TODO: Call the createConnection() function and store the connection and cursor in variables. 
        # Dont forget to pass in the correct parameters
        cnx, cursor = createConnection('root', 'iot_situacionproblema', 'R0drigo,1805', 'localhost','3306')

        # Insert the data into the database
        # TODO: Create the query string that inserts the data you created into the database
        # The query string should be an insert statement that inserts the data into the dht_sensor_data table
        query = ("INSERT INTO dht_data (humidity, temperature, date_time) VALUES (%s, %s, %s)")
        data = (humidity, temperature, current_date_time)
        
        # TODO: Execute the query string you created
        cursor.execute(query, data)

        # Commit the changes
        cnx.commit()

        print("Data inserted successfully")

    except mysql.connector.Error as err:
        """Handle possible errors"""
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    finally:
        """Close the connection"""
        if ('cnx' in locals() or 'cnx' in globals()) and ('cursor' in locals() or 'cursor' in globals()):
            cnx.close()
            cursor.close()

print("sdfghjk")
for i in range(100):
    insert_data()
    