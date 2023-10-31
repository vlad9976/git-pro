import os
import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)

def get_user_scores():
    try:
        # Create a MySQL connection
        connection = mysql.connector.connect(
            host='git-pro-mysql-1',
            user='mysql',
            password='Aa123456!',
            database='games'
        )

        cursor = connection.cursor(dictionary=True)

        # Query the database
        query = "SELECT username, score FROM users_scores"
        cursor.execute(query)

        # Get the results of the query
        scores = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return scores

    except Exception as e:
        # Log the error
        print("Error fetching scores from the database:", str(e))

        # Return an empty list
        return []

@app.route("/")
def index():
    # Get the user scores
    scores = get_user_scores()

    # Render the index template with the user scores
    return render_template("index.html", scores=scores)

@app.route("/shutdown", methods=["POST"])
def shutdown():
    # Validate the request
    if request.method != "POST":
        return "Invalid request method", 405

    # Shut down the server gracefully
    os.kill(os.getpid(), 9)  # Terminate the current process

    # Return a message to the user
    return "Server shutting down..."

if __name__ == "__main__":
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
