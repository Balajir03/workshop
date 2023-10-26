from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        # Save data to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mydb"
        )
        cursor = connection.cursor()
        cursor.execute("INSERT INTO form_data (name, email) VALUES (%s, %s)", (name, email))
        connection.commit()
        connection.close()

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
