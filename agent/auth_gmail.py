from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os

from utils.config import GMAIL_AUTH_LOCAL_SERVER_IP, GMAIL_AUTH_LOCAL_SERVER_PORT
os.environ['NO_PROXY'] = "http://127.0.0.1,localhost"

# Scopes for Gmail API
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

credentials_path = 'agent/gmail_client_config.json'

if os.path.exists(credentials_path):
    print("credentials.json file is accessible.")
else:
    print("Error: credentials.json file is not found.")

def authenticate_gmail():
    """
    Authenticates the user with Gmail API using credentials.json and returns credentials.
    Returns:
        Credentials: Authenticated credentials object.
    """
    creds = None
    # Check if token.json exists (to reuse existing credentials)
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    else:
        print("token.json file is not found.")
    # If no valid credentials are available, prompt user to log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(host=GMAIL_AUTH_LOCAL_SERVER_IP, port=GMAIL_AUTH_LOCAL_SERVER_PORT)

        # Save the credentials for future use
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds