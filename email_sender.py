import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# environment variables
HOST = 'smtp.gmail.com'
PORT = 587
USERNAME = "oscar.cardenasg@gmail.com"
PASSWORD = "0scarCardenas90"
FROM_EMAIL = 'Oscar Cárdenas <oscar.cardenasg@gmail.com>'
HTML_TEMPLATE = """
<h1>{subject}</h1>
<div style="color: #00FF00; background: #fefefe!important; text-align: center; font-size: 1rem; min-height: 200px; padding: 1rem;">
    {text}
</div>
"""


def emailSender(toEmails=[], subject='Hello, how are you?', text='This is the body of email', isHTML=False):
    try:
        assert isinstance(toEmails, list)
        email = MIMEMultipart('alternative')
        email['From'] = FROM_EMAIL
        email['To'] = ', '.join(toEmails)
        email['Subject'] = subject

        # set text plain as a part of body message
        textPart = MIMEText(text, 'plain')
        email.attach(textPart)

        # set html encoded text as a part of body message if required
        if isHTML:
            htmlText = HTML_TEMPLATE.format(subject=subject, text=text)
            htmlPart = MIMEText(htmlText, 'html')
            email.attach(htmlPart)

        # login on stmp server
        server = smtplib.SMTP(host=HOST, port=PORT)
        server.ehlo()
        server.starttls()
        server.login(USERNAME, PASSWORD)
        server.sendmail(FROM_EMAIL, toEmails, email.as_string())
        server.quit()
        return True
    except:
        print('somenthing went wrong')
        return False


if __name__ == "__main__":
    emails = []
    terminal_arguments = sys.argv
    if len(terminal_arguments) > 1:
        emails = terminal_arguments[1].split(',')
    if len(terminal_arguments) > 2:
        subject = terminal_arguments[2]
    if len(terminal_arguments) > 3:
        body = terminal_arguments[3]

    print('Sending message...')
    isSent = emailSender(
        toEmails=emails,
        subject=subject,
        text=body,
        isHTML=True
    )
    if isSent:
        print('Sent message!')
    else:
        print('Somenting went wrong, the message dont sent :(')
