import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def get_random_code(digits: int = 6) -> str:
    max_value = 10 ** digits - 1
    int_code = random.randint(0, max_value)
    code = str(int_code).rjust(6, '0')

    return code


class EmailVerification:
    """Send email check code and checking entered code"""

    def __init__(self):
        """Server raising"""

        self.email_to_send = 'chattee@list.ru'
        self.email_password = 'Abc4QZ9akYDvS0pzfEBU'
        self.smtp_server = smtplib.SMTP('smtp.mail.ru:25')
        self.smtp_server.starttls()
        self.smtp_server.login(self.email_to_send, self.email_password)

    def send_check_code(self, recipient_email: str):
        message_data = MIMEMultipart()
        code = get_random_code()

        message_data['Subject'] = f'Ваш код для входа {code}'
        email_text = f'Ваш код для вода {code}'
        message_data.attach(MIMEText(email_text, 'plain'))

        self.smtp_server.sendmail(
            self.email_to_send,
            recipient_email,
            msg=message_data.as_string()
        )


if __name__ == '__main__':
    emails = (
        'askarbink29@gmail.com',
        'garifullininsaf4@gmail.com',
        'insafich18@mail.ru'
    )

    test = EmailVerification()

    for i in emails:
        test.send_check_code(i)
