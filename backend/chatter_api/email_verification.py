import smtplib
import random

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailVerification():
    """Send email check code and checking entered code"""
    def __init__(self) -> None:
        """Server raising"""
        self.email_to_send = "chattee@list.ru"
        self.email_password = "Abc4QZ9akYDvS0pzfEBU"
        self.smtp_server = smtplib.SMTP("smtp.mail.ru:25")
        self.smtp_server.starttls()
        self.smtp_server.login(self.email_to_send, self.email_password)
        
    def send_check_code(self, recipient_email: str) -> None:
        message_data = MIMEMultipart()
        code_to_enter = self._random_code()

        message_data["Subject"] = f"Ваш код для входа {code_to_enter}"        
        email_text = f"Ваш код для вода {code_to_enter}"
        message_data.attach(MIMEText(email_text, "plain"))

        self.smtp_server.sendmail(self.email_to_send, recipient_email, msg=message_data.as_string())
            
    def _random_code(self) -> str:
        """Get random 6-digit number"""
        return str(random.randint(0, 999999)).rjust(6, '0')

if __name__=='__main__':
    test = EmailVerification()
    test.send_check_code("garifullininsaf4@gmail.com")
    test.send_check_code("askarbink29@gmail.com")
    test.send_check_code("insafich18@mail.ru")