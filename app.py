from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'New York',
    'salary': 50000
}, {
    'id': 2,
    'title': 'Data Analyst',
    'location': 'Calgary',
    'salary': 65000
}, {
    'id': 3,
    'title': 'Cloud Engineer',
    'location': 'New Delhi',
    'salary': 120000
}, {
    'id': 4,
    'title': 'UI/UX Developer',
    'location': 'Remote'
}]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
