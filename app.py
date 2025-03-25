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

@app.route('/contact_search', methods=['POST'])
def contact_search():
    search_data = request.json
    contact_name = search_data.get('contact_name')
    contact_email = search_data.get('contact_email')
    contact_phone = search_data.get('contact_phone')
    contact_msi_clientid = search_data.get('contact_msi_clientid')

    conn = get_connection()
    cursor = conn.cursor()

    sql_query = """
    SELECT first_name, last_name, email, client_id, mobile_phone
    FROM [MSIOPS].[dbo].[CRIDS_cm_clients]
    WHERE first_name = ? OR email = ? OR mobile_phone = ? OR client_id = ?
    """
    try:
        cursor.execute(sql_query, (contact_name, contact_email, contact_phone, contact_msi_clientid))
        contact = cursor.fetchone()
    except pyodbc.ProgrammingError as e:
        return jsonify({'error': f"Database error: {e}"}), 500
    finally:
        conn.close()

    if contact:
        contact_info = {
            'first_name': contact[0],
            'last_name': contact[1],
            'email': contact[2],
            'MSI_ClientID': contact[3],
            'phone_number': contact[4]
        }
        print(contact_info)
        return jsonify(contact_info)
    else:
        return jsonify({'error': 'Contact not found'}), 404

@app.route('/update_contact', methods=['POST'])
def update_contact():
    data = request.json
    contact_name = data['contact_name']
    contact_email = data['contact_email']
    contact_phone = data['contact_phone']
    contact_msi_clientid = data['contact_msi_clientid']
    communications_number = data['communications_number']  # Correct variable name

    conn = get_connection()
    cursor = conn.cursor()

    sql_query = """
    UPDATE [MessageAIML].[dbo].[Communications]
    SET contact_first_name = ?, contact_last_name = ?, contact_email = ?, contact_phone_number = ?, contact_MSI_ClientID = ?
    WHERE communication_number = ?
    """
    try:
        cursor.execute(sql_query, (
            contact_name.split()[0],  # First name
            contact_name.split()[1],  # Last name
            contact_email,
            contact_phone,
            contact_msi_clientid,
            communications_number  # Correct variable name
        ))
        conn.commit()
    except pyodbc.ProgrammingError as e:
        return jsonify({'error': f"Database error: {e}"}), 500
    finally:
        conn.close()

    return jsonify({'status': 'success'})

@app.route('/')
def index():
    return render_template('MSIIT Communications.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
