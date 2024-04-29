import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="chatbot_database"
)

# Function to insert a new user
def insert_user(name, email):
    cursor = cnx.cursor()
    insert_query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    cursor.execute(insert_query, (name, email))
    cnx.commit()
    cursor.close()
    return cursor.lastrowid

# Function to retrieve a response based on a trigger word
def get_response(trigger_word):
    cursor = cnx.cursor()
    query = "SELECT response_text FROM responses WHERE trigger_word = %s"
    cursor.execute(query, (trigger_word,))
    result = cursor.fetchone()
    cursor.close()
    if result:
        return result[0]
    else:
        return "I'm sorry, I don't understand that."

# Function to store a user message
def store_user_message(user_id, message_text):
    cursor = cnx.cursor()
    insert_query = "INSERT INTO user_messages (user_id, message_text) VALUES (%s, %s)"
    cursor.execute(insert_query, (user_id, message_text))
    cnx.commit()
    cursor.close()

# Example usage of the functions
if __name__ == "__main__":
    # Insert a new user
    user_id = insert_user("Alice", "alice@example.com")
    print(f"New user inserted with user_id: {user_id}")

    # Retrieve a response based on a trigger word
    response = get_response("hello")
    print(f"Response for 'hello': {response}")

    # Store a user message
    store_user_message(user_id, "What is the weather today?")
    print("User message stored successfully.")
