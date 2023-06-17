import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError

from google.oauth2 import service_account



#If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly',
          "https://www.googleapis.com/auth/gmail.send",
          'https://www.googleapis.com/auth/drive',
          'https://www.googleapis.com/auth/drive.file',
          'https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/spreadsheets.readonly',
          'https://www.googleapis.com/auth/gmail.labels',
          'https://www.googleapis.com/auth/gmail.compose',
          'https://mail.google.com/',
          'https://www.googleapis.com/auth/gmail.settings.sharing',
          'https://www.googleapis.com/auth/gmail.settings.basic',
          'https://www.googleapis.com/auth/gmail.metadata',
          'https://www.googleapis.com/auth/gmail.modify',
          'https://www.googleapis.com/auth/gmail.insert'
          ]

creds = service_account.Credentials.from_service_account_file(
    'token.json', scopes=SCOPES)
service = build('gmail', 'v1', credentials=creds)
message = MIMEText('pelo menos estou funcionando')
message['to'] = 'perseu912@gmail.com'
message['subject'] = 'Email Subject'
create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

try:
    message = (service.users().messages().send(userId="me", body=create_message).execute())
    print(F'sent message to {message} Message Id: {message["id"]}')
except HTTPError as error:
    print(F'An error occurred: {error}')
    message = None
