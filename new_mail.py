from __future__ import print_function

import base64
from email.message import EmailMessage


import google.auth
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError



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
def gmail_send_message():
    """Create and send an email message
    Print the returned  message id
    Returns: Message object, including message id

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    try:
        service = build('gmail', 'v1', credentials=creds)
        message = EmailMessage()

        message.set_content('<h1>This is automated draft mail</h1>')

        message['To'] ='perseu912@gmail.com'
        message['From'] ='sendmailreysofts@gmail.com'
        message['Subject'] = 'Automated draft'

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
            .decode()

        create_message = {
            'raw': encoded_message
        }
        # pylint: disable=E1101
        send_message = (service.users().messages().send
                        (userId="me", body=create_message).execute())
        print(F'Message Id: {send_message["id"]}')
    except HttpError as error:
        print(F'An error occurred: {error}')
        send_message = None
    return send_message


if __name__ == '__main__':
    gmail_send_message()