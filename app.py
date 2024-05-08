from flask import Flask, render_template, request
from models import save_form_data # imports a fuction from models.py

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
  name = request.form.get('name')
  email = request.form.get('email')
  message = request.form.get('message')
  # Process form data here (e.g., save to database, send email)
  save_form_data(name, message, email)
  return f"Thanks {name} for your message! We'll be in touch soon."

if __name__ == '__main__':
  app.run(debug=True)
