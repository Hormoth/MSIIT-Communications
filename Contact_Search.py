import pyodbc
import json
from flask import Flask, request, jsonify
from app import get_connection

app = Flask(__name__)

@app.route('/contact_search', methods=['POST'])
def contact_search():
    email = request.args.get('email')
    print(f"This is the email: {email}")
    if not email:
        return jsonify({"error": "Email parameter is required"}), 400

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT
        [client_id],
        [first_name],
        [last_name],
        [email],
        [mobile_phone],
        [notes]
    FROM [MSIOPS].[dbo].[CRIDS_cm_clients]
    WHERE [email] = ?
    """
    cursor.execute(query, (email,))
    contact = cursor.fetchone()

    conn.close()

    if contact:
        contact_dict = {
            "client_id": contact.client_id,
            "first_name": contact.first_name,
            "last_name": contact.last_name,
            "email": contact.email,
            "mobile_phone": contact.mobile_phone,
            "notes": contact.notes
        }
        print(contact_dict)
        return jsonify(contact_dict)

    else:
        return jsonify({"error": "Contact not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

