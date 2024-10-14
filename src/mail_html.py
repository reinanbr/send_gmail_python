from __future__ import print_function

import base64

from email.mime.text import MIMEText

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



subject = "Hello from Python"
body = """
<html>
  <body>
  <h1>Test</h1>
    <p>This is an <b>HTML</b> email sent from Python using the Gmail SMTP server.</p>
    <img height=400 width=250 src='https://thumbnailer.mixcloud.com/unsafe/600x600/extaudio/0/0/b/9/e41c-4652-48a4-9c38-780a98c2a8cf.jpg'>
    <br><i>foi krl!!</i>
  </body>
</html>
"""



def gmail_send_message():
    """Create and send an email html_message
    Print the returned  html_message id
    Returns: Message object, including html_message id

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    try:
        service = build('gmail', 'v1', credentials=creds)
        html_message = MIMEText(body, 'html')


        html_message['To'] ='perseu912@gmail.com'
        html_message['From'] ='sendmailreysofts@gmail.com'
        html_message['Subject'] = 'Automated draft'

        # encoded html_message
        encoded_message = base64.urlsafe_b64encode(html_message.as_bytes()) \
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