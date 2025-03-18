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
            "first_name": "Divana",
            "last_name": "Williams",
            "email": "divanawilliams@gmail.com",
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
            "first_name": "Sameer",
            "last_name": "Mohammed",
            "email": "urzsameer12@gmail.com",
            "MSI ClientID": "",
            "phone number": "248-855-5735"
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
            "first_name": "Osvaldo",
            "last_name": "ORtiz",
            "email": "",
            "MSI ClientID": "650361",
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
            "first_name": "Eddie",
            "last_name": "Velasquez",
            "email": "ev53352@gmail.com",
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
            "first_name": "Alberto",
            "last_name": "Munoz Jr.",
            "email": "Marinalongoria100@gmail.com",
            "MSI ClientID": "",
            "phone number": "5415612512"
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
            "first_name": "Nechemyah",
            "last_name": "Levi",
            "email": "",
            "MSI ClientID": "",
            "phone number": "4134064977"
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
            "first_name": "",
            "last_name": "",
            "email": "nrfink1593@gmail.com",
            "MSI ClientID": "712208",
            "phone number": "7048089254"
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
            "first_name": "Annaleeza",
            "last_name": "Macias",
            "email": "Mannaleeza@gmail.com",
            "MSI ClientID": "",
            "phone number": "909-559-3894"
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
            "first_name": "Alliyah",
            "last_name": "Gates",
            "email": "Alliyahgates@gmail.com",
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
            "first_name": "Tiana",
            "last_name": "Dominguez",
            "email": "",
            "MSI ClientID": "",
            "phone number": "8402084551"
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
            "first_name": "",
            "last_name": "",
            "email": "Drueda0294@yahoo.com",
            "MSI ClientID": "731320",
            "phone number": "3128268444"
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
            "first_name": "Diana",
            "last_name": "Rueda",
            "email": "Drueda0294@yahoo.com",
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
            "first_name": "Kevontae",
            "last_name": "Higgins",
            "email": "higgyt42@gmail.com",
            "MSI ClientID": "",
            "phone number": "2566178519"
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
            "first_name": "Jonathan",
            "last_name": "Delcid Aguilar",
            "email": "",
            "MSI ClientID": "",
            "phone number": "4422543988"
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
            "first_name": "Nathan",
            "last_name": "Wright",
            "email": "",
            "MSI ClientID": "732783",
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
            "first_name": "Ronald",
            "last_name": "White",
            "email": "ronniewhite.me@gmail.com",
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
            "first_name": "Charles",
            "last_name": "Perry Jr.",
            "email": "Ckperry93@yahoo.com",
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
            "first_name": "Hector Y ",
            "last_name": "Lewis",
            "email": "",
            "MSI ClientID": "",
            "phone number": "7084462228"
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
            "first_name": "Joaquin",
            "last_name": "Fernandez Torres",
            "email": "",
            "MSI ClientID": "738524",
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
            "first_name": "Damariz",
            "last_name": "Coronado",
            "email": "Damarizcoronado2000@gmail.com",
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
