from flask import Flask

app = Flask(__name__)
app.debug = True

@app.route("/main")
def main():
    return "Hello WOrld!"


if __name__ == "__main__":
    app.run()