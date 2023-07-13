from flask import Flask, request

app = Flask(__name__)

@app.route("/welcome")
def home_page():
    html = """
    <html>
     <body>
        <p>welcome </p>
      </body>
    </html>
    """
    return html

@app.route("/welcome/home")
def home_welcome():
    home = """
    <html>
     <body>
        <p>welcome home </p>
      </body>
    </html>
    """
    return home

@app.route("/welcome/back")
def home_back():
    back = """
    <html>
     <body>
        <p>welcome back </p>
      </body>
    </html>
    """
    return back


    