from flask import Flask, render_template
import os
import mysql.connector

app = Flask(__name__)

# MySQL database configuration
db_config = {
    'user': 'root',
    'password': '',
    'host': 'mysql',  # Use the correct service name
    'database': 'games'
}

def get_user_scores():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = "SELECT username, score FROM users_scores"
        cursor.execute(query)

        scores = cursor.fetchall()
        return scores

    except Exception as e:
        print("Error fetching scores from the database:", str(e))
        return []

@app.route("/")
def index():
    scores = get_user_scores()

    return render_template("index.html", scores=scores)

@app.route("/shutdown", methods=["POST"])
def shutdown():
    print("Shutting down gracefully...")
    os.kill(os.getpid(), 9)  # Terminate the current process
    return "Server shutting down..."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
