import json
import pyodbc

dbconfig = {
    'server': '10.1.79.39',
    'port': '1433',
    'database': 'MessageAIML',
    'username': 'jhartman',
    'password': 'M@st3r$w0rdsm@n',
    'driver': 'ODBC Driver 17 for SQL Server'
}

# Establish a database connection
conn = pyodbc.connect(
    f"DRIVER={dbconfig['driver']};"
    f"SERVER={dbconfig['server']};"
    f"PORT={dbconfig['port']};"
    f"DATABASE={dbconfig['database']};"
    f"UID={dbconfig['username']};"
    f"PWD={dbconfig['password']}"
)

cursor = conn.cursor()

# JSON data
json_data = json.dumps([
    {   "CommunicationsNumber": 0,
        "ResponseOrder": 0,
        "location": {
            "email": "yes",
            "text": "",
            "upload": "",
            "chat": "",
            "initiator": "contact"
        },
        "Subscriber": {
            "sub_Id": "001",
            "Company": "ABC Corp",
            "Convo_Id": "N/A"
        },
        "contact": {
            "first_name": "Alex",
            "last_name": "Smith",
            "email": "alex.smith@example.com",
            "MSI ClientID": "",
            "phone number": ""
        },
        "subject": {
            "body": "Inquiry about recent transaction",
            "text convo": "",
            "upload comment": "",
            "chat log": ""
        },
        "Attachment": "none",
        "Prompt": "what is said in subject: Dear Alex, we have received your inquiry about the recent transaction. We will get back to you shortly.",
        "Response": ""
    },
    {
        "CommunicationsNumber": 1,
        "ResponseOrder": 0,
        "location": {
            "email": "",
            "text": "yes",
            "upload": "",
            "chat": "",
            "initiator": "account"
        },
        "Subscriber": {
            "sub_Id": "002", 
            "Company": "XYZ Inc",
            "Convo_Id": "N/A"
        },
        "contact": {
            "first_name": "Jamie",
            "last_name": "Doe",
            "email": "jamie.doe@example.com",
            "MSI ClientID": "",
            "phone number": "987-654-3210"
        },
        "subject": {
            "body": "",
            "text convo": "Follow-up on appointment",
            "upload comment": "",
            "chat log": ""
        },
        "Attachment": "none",
        "Prompt": "what is said in subject: Hi Jamie, this is a follow-up reminder for your upcoming appointment. Please confirm your availability.",
        "Response": ""
    },
    {
        "CommunicationsNumber": 2,
        "ResponseOrder": 0,
        "location": {
            "email": "",
            "text": "",
            "upload": "yes",
            "chat": "",
            "initiator": "contact"
        },
        "Subscriber": {
            "sub_Id": "003",
            "Company": "LMN Ltd",
            "Convo_Id": "N/A"
        },
        "contact": {
            "first_name": "Taylor",
            "last_name": "Johnson",
            "email": "",
            "MSI ClientID": "10001",
            "phone number": ""
        },
        "subject": {
            "body": "",
            "text convo": "",
            "upload comment": "Submission of documents",
            "chat log": ""
        },
        "Attachment": "file1.pdf, file2.docx",
        "Prompt": "what is said in subject: Taylor, your documents have been successfully submitted. We will review them and contact you if needed.",
        "Response": ""
    },
    {   
        "CommunicationsNumber": 3,
        "ResponseOrder": 0,
        "location": {
            "email": "yes",
            "text": "",
            "upload": "",
            "chat": "",
            "initiator": "account"
        },
        "Subscriber": {
            "sub_Id": "004",
            "Company": "OPQ Enterprises",
            "Convo_Id": "N/A"
        },
        "contact": {
            "first_name": "Morgan",
            "last_name": "Lee",
            "email": "morgan.lee@example.com",
            "MSI ClientID": "",
            "phone number": ""
        },
        "subject": {
            "body": "Assistance with account setup",
            "text convo": "",
            "upload comment": "",
            "chat log": ""
        },
        "Attachment": "none",
        "Prompt": "what is said in subject: Hello Morgan, we are here to assist you with your account setup. Please provide the necessary details.",
        "Response": ""
    },
    {
        "CommunicationsNumber": 4,
        "ResponseOrder": 0,
        "location": {
            "email": "",
            "text": "",
            "upload": "",
            "chat": "yes",
            "initiator": "contact"
        },
        "Subscriber": {
            "sub_Id": "005",
            "Company": "RST Solutions",
            "Convo_Id": "N/A"
        },
        "contact": {
            "first_name": "Jordan",
            "last_name": "Brown",
            "email": "jordan.brown@example.com",
            "MSI ClientID": "",
            "phone number": "222-333-4444"
        },
        "subject": {
            "body": "Request for information",
            "text convo": "",
            "upload comment": "",
            "chat log": ""
        },
        "Attachment": "none",
        "Prompt": "what is said in subject: Dear Jordan, we have received your request for information. Our team will respond to you shortly.",
        "Response": ""
    },
    {
        "CommunicationsNumber": 5,
        "ResponseOrder": 0,
        "location": {
            "email": "",
            "text": "yes",
            "upload": "",
            "chat": "",
            "initiator": "account"
        },
        "Subscriber": {
            "sub_Id": "006",
            "Company": "UVW Corp",
            "Convo_Id": "N/A"
        },
        "contact": {
            "first_name": "Casey",
            "last_name": "Davis",
            "email": "",
            "MSI ClientID": "",
            "phone number": "333-444-5555"
        },
        "subject": {
            "body": "",
            "text convo": "Confirmation of meeting",
            "upload comment": "",
            "chat log": ""
        },
        "Attachment": "none",
        "Prompt": "what is said in subject: Hi Casey, your meeting has been confirmed. We look forward to seeing you.",
        "Response": ""
    },
    {
        "CommunicationsNumber": 6,
        "ResponseOrder": 0,
        "location": {
            "email": "",
            "text": "",
            "upload": "yes",
            "chat": "",
            "initiator": "contact"
        },
        "Subscriber": {
            "sub_Id": "007",
            "Company": "XYZ Inc",
            "Convo_Id": "N/A"
        },
        "contact": {
            "first_name": "Riley",
            "last_name": "Martinez",
            "email": "",
            "MSI ClientID": "10002",
            "phone number": "444-555-6666"
        },
        "subject": {
            "body": "",
            "text convo": "",
            "upload comment": "Submission of application",
            "chat log": ""
        },
        "Attachment": "resume.pdf, cover_letter.docx, portfolio.zip",
        "Prompt": "what is said in subject: Riley, your application has been submitted successfully. We will review it and get back to you.",
        "Response": ""
    },
    {
        "CommunicationsNumber": 7,
        "ResponseOrder": 0,
        "location": {
            "email": "yes",
            "text": "",
            "upload": "",
            "chat": "",
            "initiator": "account"
        },
        "Subscriber": {
            "sub_Id": "008",
            "Company": "ABC Corp",
            "Convo_Id": "N/A"
        },
        "contact": {
            "first_name": "Alexis",
            "last_name": "Garcia",
            "email": "alexis.garcia@example.com",
            "MSI ClientID": "",
            "phone number": ""
        },
        "subject": {
            "body": "Help with password reset",
            "text convo": "",
            "upload comment": "",
            "chat log": ""
        },
        "Attachment": "none",
        "Prompt": "what is said in subject: Hello Alexis, we are here to help you reset your password. Please follow the instructions provided.",
        "Response": ""
    },
    {
        "CommunicationsNumber": 8,
        "ResponseOrder": 0,
        "location": {
            "email": "yes",
            "text": "",
            "upload": "",
            "chat": "",
            "initiator": "contact"
        },
        "Subscriber": {
            "sub_Id": "009",
            "Company": "LMN Ltd",
            "Convo_Id": "N/A"
        },
        "contact": {
            "first_name": "Peyton",
            "last_name": "Rodriguez",
            "email": "peyton.rodriguez@example.com",
            "MSI ClientID": "",
            "phone number": ""
        },
        "subject": {
            "body": "Inquiry about billing",
            "text convo": "",
            "upload comment": "",
            "chat log": ""
        },
        "Attachment": "invoice.pdf",
        "Prompt": "what is said in subject: Dear Peyton, we have received your inquiry about billing. Our billing department will contact you soon.",
        "Response": ""
    },
    {
        "CommunicationsNumber": 9,
        "ResponseOrder": 0,
        "location": {
            "email": "",
            "text": "yes",
            "upload": "",
            "chat": "",
            "initiator": "account"
        },
        "Subscriber": {
            "sub_Id": "010",
            "Company": "OPQ Enterprises",
            "Convo_Id": "N/A"
        },
        "contact": {
            "first_name": "Quinn",
            "last_name": "Wilson",
            "email": "",
            "MSI ClientID": "",
            "phone number": "777-888-9999"
        },
        "subject": {
            "body": "",
            "text convo": "Follow-up on service request",
            "upload comment": "",
            "chat log": ""
        },
        "Attachment": "none",
        "Prompt": "what is said in subject: Hi Quinn, this is a follow-up on your service request. Please let us know if you need further assistance.",
        "Response": ""
    },
    {
        "CommunicationsNumber": 10,
        "ResponseOrder": 0,
        "location": {
            "email": "",
            "text": "",
            "upload": "yes",
            "chat": "",
            "initiator": "contact"
        },
        "Subscriber": {
            "sub_Id": "011",
            "Company": "RST Solutions",
            "Convo_Id": "N/A"
        },
        "contact": {
            "first_name": "Blake",
            "last_name": "Lopez",
            "email": "",
            "MSI ClientID": "10003",
            "phone number": ""
        },
        "subject": {
            "body": "",
            "text convo": "",
            "upload comment": "Submission of feedback",
            "chat log": ""
        },
        "Attachment": "feedback_form.pdf",
        "Prompt": "what is said in subject: Blake, thank you for your feedback. We appreciate your input and will take it into consideration.",
        "Response": ""
    },
    {
        "CommunicationsNumber": 11,
        "ResponseOrder": 0,
        "location": {
            "email": "yes",
            "text": "",
            "upload": "",
            "chat": "",
            "initiator": "account"
        },
        "Subscriber": {
            "sub_Id": "012",
            "Company": "UVW Corp",
            "Convo_Id": "N/A"
        },
        "contact": {
            "first_name": "Avery",
            "last_name": "Gonzalez",
            "email": "avery.gonzalez@example.com",
            "MSI ClientID": "",
            "phone number": ""
        },
        "subject": {
            "body": "Assistance with login",
            "text convo": "",
            "upload comment": "",
            "chat log": ""
        },
        "Attachment": "screenshot.png",
        "Prompt": "what is said in subject: Hello Avery, we are here to assist you with your login issues. Please provide more details.",
        "Response": ""
    },
    {   "CommunicationsNumber": 12,
        "ResponseOrder": 0,
        "location": {
            "email": "",
            "text": "",
            "upload": "",
            "chat": "yes",
            "initiator": "contact"
        },
        "Subscriber": {
            "sub_Id": "013",
            "Company": "XYZ Inc",
            "Convo_Id": "N/A"
        },
        "contact": {
            "first_name": "Skyler",
            "last_name": "Perez",
            "email": "skyler.perez@example.com",
            "MSI ClientID": "",
            "phone number": "000-111-2222"
        },
        "subject": {
            "body": "Request for support",
            "text convo": "",
            "upload comment": "",
            "chat log": ""
        },
        "Attachment": "none",
        "Prompt": "what is said in subject: Dear Skyler, we have received your support request. Our support team will contact you shortly.",
        "Response": ""
    },
    {
        "CommunicationsNumber": 13,
        "ResponseOrder": 0,
        "location": {
            "email": "",
            "text": "yes",
            "upload": "",
            "chat": "",
            "initiator": "account"
        },
        "Subscriber": {
            "sub_Id": "014",
            "Company": "ABC Corp",
            "Convo_Id": "N/A"
        },
        "contact": {
            "first_name": "Dakota",
            "last_name": "Thompson",
            "email": "",
            "MSI ClientID": "",
            "phone number": "111-222-3333"
        },
        "subject": {
            "body": "",
            "text convo": "Confirmation of delivery",
            "upload comment": "",
            "chat log": ""
        },
        "Attachment": "none",
        "Prompt": "what is said in subject: Hi Dakota, your delivery has been confirmed. Thank you for choosing our service.",
        "Response": ""
    },
    {
        "CommunicationsNumber": 14,
        "ResponseOrder": 0,
        "location": {
            "email": "",
            "text": "",
            "upload": "yes",
            "chat": "",
            "initiator": "contact"
        },
        "Subscriber": {
            "sub_Id": "015",
            "Company": "LMN Ltd",
            "Convo_Id": "N/A"
        },
        "contact": {
            "first_name": "Reese",
            "last_name": "White",
            "email": "",
            "MSI ClientID": "10004",
            "phone number": ""
        },
        "subject": {
            "body": "",
            "text convo": "",
            "upload comment": "Submission of report",
            "chat log": ""
        },
        "Attachment": "report.pdf, data.xlsx",
        "Prompt": "what is said in subject: Reese, your report has been submitted successfully. We will review it and get back to you.",
        "Response": ""
    },
    {
        "CommunicationsNumber": 15,
        "ResponseOrder": 0,
        "location": {
            "email": "yes",
            "text": "",
            "upload": "",
            "chat": "",
            "initiator": "account"
        },
        "Subscriber": {
            "sub_Id": "016",
            "Company": "OPQ Enterprises",
            "Convo_Id": "N/A"
        },
        "contact": {
            "first_name": "Taylor",
            "last_name": "Harris",
            "email": "taylor.harris@example.com",
            "MSI ClientID": "",
            "phone number": ""
        },
        "subject": {
            "body": "Help with account recovery",
            "text convo": "",
            "upload comment": "",
            "chat log": ""
        },
        "Attachment": "none",
        "Prompt": "what is said in subject: Hello Taylor, we are here to help you recover your account. Please follow the instructions provided.",
        "Response": ""
    },
    {
        "CommunicationsNumber": 16,
        "ResponseOrder": 0,
        "location": {
            "email": "yes",
            "text": "",
            "upload": "",
            "chat": "",
            "initiator": "contact"
        },
        "Subscriber": {
            "sub_Id": "017",
            "Company": "RST Solutions",
            "Convo_Id": "N/A"
        },
        "contact": {
            "first_name": "Morgan",
            "last_name": "Clark",
            "email": "morgan.clark@example.com",
            "MSI ClientID": "",
            "phone number": ""
        },
        "subject": {
            "body": "Inquiry about product",
            "text convo": "",
            "upload comment": "",
            "chat log": ""
        },
        "Attachment": "product_brochure.pdf",
        "Prompt": "what is said in subject: Dear Morgan, we have received your inquiry about our product. Our sales team will contact you soon.",
        "Response": ""
    },
    {
        "CommunicationsNumber": 17,
        "ResponseOrder": 0,
        "location": {
            "email": "",
            "text": "yes",
            "upload": "",
            "chat": "",
            "initiator": "account"
        },
        "Subscriber": {
            "sub_Id": "018",
            "Company": "UVW Corp",
            "Convo_Id": "N/A"
        },
        "contact": {
            "first_name": "Jordan",
            "last_name": "Lewis",
            "email": "",
            "MSI ClientID": "",
            "phone number": "555-666-7777"
        },
        "subject": {
            "body": "",
            "text convo": "Follow-up on order",
            "upload comment": "",
            "chat log": ""
        },
        "Attachment": "none",
        "Prompt": "what is said in subject: Hi Jordan, this is a follow-up on your order. Please let us know if you need further assistance.",
        "Response": ""
    },
    {
        "CommunicationsNumber": 18,
        "ResponseOrder": 0,
        "location": {
            "email": "",
            "text": "",
            "upload": "yes",
            "chat": "",
            "initiator": "contact"
        },
        "Subscriber": {
            "sub_Id": "019",
            "Company": "XYZ Inc",
            "Convo_Id": "N/A"
        },
        "contact": {
            "first_name": "Casey",
            "last_name": "Walker",
            "email": "",
            "MSI ClientID": "10005",
            "phone number": ""
        },
        "subject": {
            "body": "",
            "text convo": "",
            "upload comment": "Submission of resume",
            "chat log": ""
        },
        "Attachment": "resume.pdf, cover_letter.docx",
        "Prompt": "what is said in subject: Casey, your resume has been submitted successfully. We will review it and contact you if needed.",
        "Response": ""
    },
    {
        "CommunicationsNumber": 19,
        "ResponseOrder": 0,
        "location": {
            "email": "yes",
            "text": "",
            "upload": "",
            "chat": "",
            "initiator": "account"
        },
        "Subscriber": {
            "sub_Id": "020",
            "Company": "ABC Corp",
            "Convo_Id": "N/A"
        },
        "contact": {
            "first_name": "Riley",
            "last_name": "Hall",
            "email": "riley.hall@example.com",
            "MSI ClientID": "",
            "phone number": ""
        },
        "subject": {
            "body": "Assistance with payment",
            "text convo": "",
            "upload comment": "",
            "chat log": ""
        },
        "Attachment": "none",
        "Prompt": "what is said in subject: Hello Riley, we are here to assist you with your payment issues. Please provide more details.",
        "Response": ""
    }
])

data = json.loads(json_data)

# Insert data into the database
for item in data:
    communications_number = item['CommunicationsNumber']
    response_order = item['ResponseOrder']
    location = item['location']
    subscriber = item['Subscriber']
    contact = item['contact']
    subject = item['subject']
    attachment = item['Attachment']
    prompt = item['Prompt']
    response = item['Response']

    cursor.execute('''
        INSERT INTO Communications (
            CommunicationsNumber,
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
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        communications_number,
        response_order,
        location['email'],
        location['text'],
        location['upload'],
        location['chat'],
        location['initiator'],
        subscriber['sub_Id'],
        subscriber['Company'],
        subscriber['Convo_Id'],
        contact['first_name'],
        contact['last_name'],
        contact['email'],
        contact['MSI ClientID'],
        contact['phone number'],
        subject['body'],
        subject['text convo'],
        subject['upload comment'],
        subject['chat log'],
        attachment,
        prompt,
        response
    ))

# Commit the transaction
conn.commit()

# Close the connection
cursor.close()
conn.close()
