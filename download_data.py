import pandas as pd
import pyodbc
from dbconfig import dbconfig
import json
from flask import Flask, jsonify


def download_data():
    # Establish connection to the database using pyodbc and dbconfig.py data
    conn = pyodbc.connect(
        f"DRIVER={dbconfig['driver']};"
        f"SERVER={dbconfig['server']};"
        f"PORT={dbconfig['port']};"
        f"DATABASE={dbconfig['database']};"
        f"UID={dbconfig['username']};"
        f"PWD={dbconfig['password']}"
    )
    cursor = conn.cursor()

    # SQL query to select all rows from the Communications table with ResponseOrder = 0
    sql_query = "SELECT * FROM [MessageAIML].[dbo].[Communications] WHERE ResponseOrder = 0"
    cursor.execute(sql_query)
    rows = cursor.fetchall()

    # Create a list of dictionaries from the rows
    clients = []
    for row in rows:
        client = {
            'ResponseOrder': row[0],
            'location': {
                'email': row[1],
                'text': row[2],
                'upload': row[3],
                'chat': row[4],
                'initiator': row[5]
            },
            'Subscriber': {
                'sub_Id': row[6],
                'Company': row[7],
                'misc': row[8]
            },
            'contact': {
                'first_name': row[9],
                'last_name': row[10],
                'email': row[11],
                'MSI_ClientID': row[12],
                'phone number': row[13]
            },
            'subject': {
                'body': row[14],
                'text convo': row[15],
                'upload comment': row[16],
                'chat log': row[17]
            },
            'Attachment': row[18],
            'Prompt': row[19],
            'Response': row[20]
        }
        clients.append(client)

    # Close the connection
    conn.close()

    return clients


