import subprocess
import platform
import requests
import threading
import time

# Store the process object
flask_server_process = None

def start_flask_server():
    global flask_server_process

    system = platform.system()
    if system == "Linux":
        command = ["python", "app.py"]
    elif system == "Windows":
        command = ["start", "python", "app.py"]
    else:
        raise NotImplementedError("Unsupported operating system")

    try:
        # Run the Flask app in a separate subprocess
        flask_server_process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=(system == "Windows"))
        print("Flask Server Running In Background")
    except Exception as e:
        print("An error occurred:", str(e))


def stop_flask_server():
    global flask_server_process

    if flask_server_process:
        try:
            # Send a request to the Flask server to shut down
            requests.post("http://127.0.0.1:5000/shutdown")
            print("Stopping Flask app...")
            time.sleep(1)  # Wait for the server to shut down
        except Exception as e:
            print("An error occurred while stopping the Flask app:", str(e))
    else:
        print("Flask server process not found.")

if __name__ == "__main__":
    start_flask_server()

    # Start a thread to listen for user input and trigger the stop function
    threading.Thread(target=lambda: input("Press Enter to stop the Flask app...")).start()

    # Keep the script running to allow the Flask app to run in the background
    while True:
        time.sleep(1)
