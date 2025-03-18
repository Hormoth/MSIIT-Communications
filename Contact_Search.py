import pyodbc
import json
from app import get_connection


def contact_search():
    conn = get_connection()
    cursor = conn.cursor()
    