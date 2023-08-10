import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    contact = request.form.get('contact')
    cooperative = request.form.get('cooperative')
    emergency_contact = request.form.get('emergency_contact')
    address = request.form.get('address')

    # Create the directory if it doesn't exist
    if not os.path.exists('Registration-Requests'):
        os.makedirs('Registration-Requests')

    with open('Registration-Requests/{}.txt'.format(name), 'w') as file:
        file.write(f"Name: {name}\nContact: {contact}\nCooperative: {cooperative}\nEmergency Contact: {emergency_contact}\nAddress: {address}")

    return "Registration submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
