from flask import Flask, jsonify, render_template, request
import pyodbc
from dbconfig import dbconfig
import json
from upload_data import Insert_Data

app = Flask(__name__)

def get_connection():  
    conn = pyodbc.connect(
        f"DRIVER={dbconfig['driver']};"
        f"SERVER={dbconfig['server']};"
        f"PORT={dbconfig['port']};"
        f"DATABASE={dbconfig['database']};"
        f"UID={dbconfig['username']};"
        f"PWD={dbconfig['password']}"
    )
    return conn

def download_data():
    # Establish connection to the database using pyodbc and dbconfig.py data
    conn = get_connection()
    cursor = conn.cursor()

    # SQL query to select all rows from the Communications table with ResponseOrder = 0
    sql_query = "SELECT * FROM [MessageAIML].[dbo].[Communications] WHERE ResponseOrder = 0"
    cursor.execute(sql_query)
    rows = cursor.fetchall()

    # Create a list of dictionaries from the rows
    clients = []
    for row in rows:
        client = {
            'CommunicationsNumber': row[0],
            'ResponseOrder': row[1],
            'location': {
                'email': row[2],
                'text': row[3],
                'upload': row[4],
                'chat': row[5],
                'initiator': row[6]
            },
            'Subscriber': {
                'sub_Id': row[7],
                'Company': row[8],
                'Convo_Id': row[9]
            },
            'contact': {
                'first_name': row[10],
                'last_name': row[11],
                'email': row[12],
                'MSI_ClientID': row[13],
                'phone number': row[14]
            },
            'subject': {
                'body': row[15],
                'text convo': row[16],
                'upload comment': row[17],
                'chat log': row[18]
            },
            'Attachment': row[19],
            'Prompt': row[20],
            'Response': row[21]
        }
        clients.append(client)

    # Close the connection
    conn.close()

    return clients

@app.route('/download_data', methods=['GET'])
def get_data():
    clients = download_data()
    return jsonify(clients)

@app.route('/update_response', methods=['POST'])
def update_response():
    data = request.json
    response_text = data['response']
    message_data = data['message_data']
    
    # Add the response text to the message data
    message_data['Response'] = response_text
    message_data['ResponseOrder'] = 1
    
    # Insert the updated message data into the database
    Insert_Data(message_data)
    
    return jsonify({'status': 'success'})

@app.route('/')
def index():
    return render_template('MSIIT Communications.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
