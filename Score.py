import mysql.connector

def add_score(username, difficulty):
    POINTS_OF_WINNING = (difficulty * 3) + 5

    # Connect to MySQL
    connection = mysql.connector.connect(
        host='mysql',
        user='root',
        password='Aa123456!',
        database='games'
    )

    cursor = connection.cursor()

    # Check if the user already has a score in the database
    query = "SELECT score FROM users_scores WHERE username = %s"
    values = (username,)
    cursor.execute(query, values)

    result = cursor.fetchone()
    if result:
        current_score = result[0]
        total_score = current_score + POINTS_OF_WINNING

        # Update the score in the database
        query = "UPDATE users_scores SET score = %s WHERE username = %s"
        values = (total_score, username)
        cursor.execute(query, values)
    else:
        # If the user doesn't exist, create a new record
        query = "INSERT INTO users_scores (username, score) VALUES (%s, %s)"
        values = (username, POINTS_OF_WINNING)
        cursor.execute(query, values)

    # Commit the transaction
    connection.commit()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    print("Score successfully updated for user:", username)



