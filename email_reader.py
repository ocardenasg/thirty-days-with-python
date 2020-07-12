import imaplib
import email

HOST = 'imap.gmail.com'
username = 'oscar.cardenasg@gmail.com'
password = '0scarCardenas90'


def email_reader():
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    imap.login(username, password)
    imap.select('INBOX')

    _, response = imap.uid('search', None, 'UNSEEN')
    unread_msg_nums = response[0].split()

    unread_messages = []
    for num in unread_msg_nums:
        num = num.decode('utf-8')
        _, response = imap.uid('fetch', num, '(RFC822)')
        html = response[0][1].decode('utf-8')
        email_message = email.message_from_string(html)

        body = ''
        for part in email_message.walk():
            email_content_type = part.get_content_type()
            if email_content_type == 'text/plain':
                body = part.get_payload()
            elif email_content_type == 'text/html':
                body = part.get_payload()

        unread_messages.append({
            "to": email_message['To'],
            "from": email.utils.parseaddr(email_message['From']),
            "subject": email_message['Subject'],
            "body": body
        })

    return unread_messages


if __name__ == "__main__":
    inbox = email_reader()
    print(inbox)
