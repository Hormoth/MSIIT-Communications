import pandas as pd
import pyodbc
from dbconfig import dbconfig

def Insert_Data(message_data):
   
    df = pd.DataFrame([message_data])
    
    
    conn = pyodbc.connect(
        f"DRIVER={dbconfig['driver']};"
        f"SERVER={dbconfig['server']};"
        f"PORT={dbconfig['port']};"
        f"DATABASE={dbconfig['database']};"
        f"UID={dbconfig['username']};"
        f"PWD={dbconfig['password']}"
    )
    cursor = conn.cursor()
    
    
    for index, row in df.iterrows():
        cursor.execute(
            "UPDATE [MessageAIML].[dbo].[Communications] SET Response = ?, ResponseOrder = ? WHERE CommunicationsNumber = ?",
            row['Response'],
            row['ResponseOrder'],
            row['CommunicationsNumber']
        )
    conn.commit()
    
    # Close the connection
    conn.close()

