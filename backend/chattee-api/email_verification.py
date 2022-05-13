import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def get_random_code(digits: int = 6) -> str:
    """Generating a random code with the given number of digits"""

    max_value = 10 ** digits - 1
    int_code = random.randint(0, max_value)
    code = str(int_code).rjust(digits, '0')

    return code


class EmailVerification:
    """
    Sending a verification code to an email and verifying
    the user-entered code.
    """

    def __init__(self):
        self.email_address = 'chattee@list.ru'
        self.email_password = 'Abc4QZ9akYDvS0pzfEBU'
        self.smtp_server = smtplib.SMTP('smtp.mail.ru:25')
        self.smtp_server.starttls()
        self.smtp_server.login(self.email_address, self.email_password)

    def send_verification_code(self, recipient_email: str):
        message_data = MIMEMultipart()
        code = get_random_code()

        message_data['Subject'] = f'Your verification code is {code}.'
        message_data.attach(MIMEText(message_data['Subject']))

        self.smtp_server.sendmail(
            self.email_address,
            recipient_email,
            message_data.as_string()
        )


if __name__ == '__main__':
    emails = (
        'askarbink29@gmail.com',
        'garifullininsaf4@gmail.com',
        'insafich18@mail.ru'
    )

    test = EmailVerification()

    for address in emails:
        test.send_verification_code(address)
