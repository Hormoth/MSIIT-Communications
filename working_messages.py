import pandas as pd
from app import get_connection
import os
import time
import subprocess

get_csv_file = 'C:\\OfficeProjects\\MSIIT Communications\\Messages\\messages_Marketing.csv'
conn = get_connection()
cursor = conn.cursor()

def open_Csv(get_csv_file):
    df = pd.read_csv(get_csv_file)
    return df

def process_messages(df):
    df = df[['id', 'contactPhone', 'accountPhone', 'directionType', 'text']]
    df = df.rename(columns={
        'id': 'Subscriber_sub_Id',
        'contactPhone': 'contact_phone_number',
        'text': 'Prompt'
    })
    df = df[df['directionType'] == 'MO']
    df['location_initiator'] = df['directionType'].apply(lambda x: 'contact' if x == 'MO' else None)
    df = df.drop(columns=['directionType'])
    print(df.head())
    return df

df = open_Csv(get_csv_file)
processed_df = process_messages(df)

def insert_messages(processed_df):
    for index, row in processed_df.iterrows():
        if row['location_initiator'] == 'contact':
            sql_query = """
            INSERT INTO [MessageAIML].[dbo].[Communications] (
                ResponseOrder,
                location_email,
                location_text,
                location_upload,
                location_chat,
                location_initiator,
                Subscriber_sub_Id,
                Subscriber_Company,
                Subscriber_Convo_Id,
                contact_first_name,
                contact_last_name,
                contact_email,
                contact_MSI_ClientID,
                contact_phone_number,
                subject_body,
                subject_text_convo,
                subject_upload_comment,
                subject_chat_log,
                Attachment,
                Prompt,
                Response
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(sql_query, (
                0,  # ResponseOrder
                '',  # location_email
                'yes',  # location_text
                '',  # location_upload
                '',  # location_chat
                row['location_initiator'],
                row['Subscriber_sub_Id'],
                '',  # Subscriber_Company
                '',  # Subscriber_Convo_Id
                '',  # contact_first_name
                '',  # contact_last_name
                '',  # contact_email
                '',  # contact_MSI_ClientID
                row['contact_phone_number'],
                '',  # subject_body
                '',  # subject_text_convo
                '',  # subject_upload_comment
                '',  # subject_chat_log
                '',  # Attachment
                row['Prompt'][:255],  # Truncate to fit column size
                '',  # Response
            ))
    conn.commit()
    conn.close()
    # Delete the CSV file after inserting data
    if os.path.exists(get_csv_file):
        os.remove(get_csv_file)
        print(f"File {get_csv_file} has been deleted.")
    else:
        print(f"File {get_csv_file} does not exist.")
insert_messages(processed_df)
print('Data inserted successfully!')

while True:
    subprocess.run(['python', '/C:/OfficeProjects/MSIIT Communications/working_messages.py'])
    time.sleep(180)  # Wait for 3 minutes (180 seconds)