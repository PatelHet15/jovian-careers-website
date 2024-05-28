from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'Location': 'Bengaluru, India',
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'Location': 'Delhi, India',
        'Salary': 'Rs. 10,50,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'Location': 'Remote',
        'Salary': 'Rs. 5,00,000'
    },
    {
      'id' : 4,
      'title' : 'Backend Engineer',
      'Location' : 'San Fransisco, USA',
      'Salary' : '$1,20,000'
    },
]


@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS,company_Name='Jovian')

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
