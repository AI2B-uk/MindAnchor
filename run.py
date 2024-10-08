import webbrowser
from threading import Timer
from app import create_app

app = create_app()

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == "__main__":
    # Start a timer to open the browser after the server starts
    Timer(1, open_browser).start()
    app.run(host="0.0.0.0", port=5000)
