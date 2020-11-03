import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['From'] = 'cthomas4293@hotmail.com'
email['To'] = 'cxenvyxthomas4293@gmail.com'
email['Subject'] = 'Hi this is a test email!'
email.set_content(html.substitute(name="Carl"), "html")

with smtplib.SMTP(host='smtp.office365.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('cthomas4293@hotmail.com', 'Tiger6034+')
    smtp.send_message(email)
    print('All good!')
