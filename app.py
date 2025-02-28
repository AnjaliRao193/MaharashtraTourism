import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        print(f"Form Submission Received\nName: {name}\nEmail: {email}\nMessage: {message}")

        # Define the file path
        file_path = os.path.join(os.getcwd(), "submissions.txt")
        print(f"Saving data to: {file_path}")

        try:
            # Open the file and write data
            with open(file_path, "a", encoding="utf-8") as file:
                file.write(f"Name: {name}\nEmail: {email}\nMessage: {message}\n\n")
            print("✅ Data successfully written to file!")
        except Exception as e:
            print(f"❌ Error writing to file: {e}")

        return "Form Submitted Successfully!"

if __name__ == '__main__':
    app.run(debug=True)
