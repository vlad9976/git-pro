import mysql.connector

def add_score(user, difficulty):
    POINTS_OF_WINNING = (difficulty * 3) + 5

    # Create a MySQL connection
    connection = mysql.connector.connect(
        host='git-pro-mysql-1',
        user='mysql',
        password='Aa123456!',
        database='games'
    )

    cursor = connection.cursor()

    # Check if the user already has a score in the database
    query = "SELECT score FROM users_scores WHERE username = %s"
    cursor.execute(query, (user,))
    result = cursor.fetchone()

    if result:
        current_score = result[0]
        total_score = current_score + POINTS_OF_WINNING

        # Update the score in the database
        update_query = "UPDATE users_scores SET score = %s WHERE username = %s"
        cursor.execute(update_query, (total_score, user))
    else:
        # If the user doesn't exist, create a new record
        insert_query = "INSERT INTO users_scores (username, score) VALUES (%s, %s)"
        cursor.execute(insert_query, (user, POINTS_OF_WINNING))

    # Commit the transaction and close the connection
    connection.commit()
    cursor.close()
    connection.close()

    print("Score successfully updated for user:", user)
