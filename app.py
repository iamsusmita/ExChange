from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
  return "Welcome to ExChange! ... one stop solution for like minded people."
  
print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
