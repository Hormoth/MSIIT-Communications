import requests
import json
import csv
import os

def get_message_response(contactPhone, accountPhone, contactID, timestamp):
    url = "https://api-app2.simpletexting.com/v2/api/messages"

    payload = json.dumps([
        {
            "id": contactID,
            "contactPhone": contactPhone,
            "accountPhone": accountPhone,
            "directionType": "MO",
            "timestamp": timestamp,
            "referenceType": "API_SEND",
            "category": "SMS"
        }
    ])

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 5b51659c5e9a5e3380c6bc3c7bd92f00'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_data = response.json()

    # Define the CSV file path
    csv_file_path = os.path.join(os.getcwd(), 'Messages', 'messages_Marketing.csv')

    # Extract the relevant data from the response
    content = response_data.get('content', [])

    # Define the CSV headers
    csv_headers = ['id', 'contactPhone', 'accountPhone', 'directionType', 'timestamp', 'text']  # added 'text'

    # Check if the CSV file already exists
    file_exists = os.path.isfile(csv_file_path)

    # Open the CSV file in append mode
    with open(csv_file_path, mode='a', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)

        # Write the headers if the file does not exist
        if not file_exists:
            writer.writeheader()

        # Write the message data to the CSV file
        for message in content:
            writer.writerow({
                'id': message.get('id'),
                'text': message.get('text'),
                'contactPhone': message.get('contactPhone'),
                'accountPhone': message.get('accountPhone'),
                'directionType': message.get('directionType'),
                'timestamp': message.get('timestamp'),
                
            })


accountPhone = "2073679805"
contactPhone = "8584627686"
contactID = "66aa84f6179fe9180d9ac80d"
timestamp = "2020-04-28T23:20:08.489Z"

get_message_response(contactPhone, accountPhone, contactID, timestamp)
