import mysql.connector

# Establish a connection to the MySQL database
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="chatbot_database"  # Change to your actual database name
)

# Function to execute a query and return the results
def execute_query(query, params=None):
    # Create a cursor
    cursor = cnx.cursor()
    
    # Execute the query
    cursor.execute(query, params)
    
    # Fetch all results
    results = cursor.fetchall()
    
    # Close the cursor
    cursor.close()
    
    return results

# Function to execute an update query (INSERT, UPDATE, DELETE)
def execute_update(query, params=None):
    # Create a cursor
    cursor = cnx.cursor()
    
    # Execute the update query
    cursor.execute(query, params)
    
    # Commit changes
    cnx.commit()
    
    # Close the cursor
    cursor.close()

# Example function to fetch chatbot data (e.g., responses)
def get_chatbot_response(user_input):
    query = "SELECT response FROM chatbot_responses WHERE user_input = %s"
    params = (user_input,)
    result = execute_query(query, params)
    
    if result:
        return result[0][0]  # Return the response if found
    else:
        return "Sorry, I didn't understand that."

# Close the database connection when the script finishes
if __name__ == "__main__":
    # Example usage of the chatbot function
    user_input = "Hello"
    response = get_chatbot_response(user_input)
    print(response)

    # Close the database connection
    cnx.close()
