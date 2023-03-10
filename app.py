from flask import Flask, render_template, jsonify

app = Flask(__name__)

SKILLS=[
  {
   'id': 1,
    'skill' : 'Python',
    'Profeciency Level' : 'Beginner',
    'Daily Rate' : 'INR 800'
  },
  {
   'id': 2,
    'skill' : 'Python',
    'Profeciency Level' : 'Intermidiate',
    'Daily Rate' : 'INR 1000'
  },
  {
   'id': 3,
    'skill' : 'HTML/CSS',
    'Profeciency Level' : 'Beginner',
    'Daily Rate' : 'INR 600'
  },
    {
   'id': 4,
    'skill' : 'HTML/CSS',
    'Profeciency Level' : 'Intermidiate',
    'Daily Rate' : 'INR 900'
  }
]
@app.route("/")
def welcome():
  return render_template('home.html' , 
                         skills=SKILLS, company='IIM')

@app.route("/skills")
def list_skills():
    return jsonify(SKILLS)
  
#print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
