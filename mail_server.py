import smtplib

class mail_server:

    mail_out = ''
    mail_to = ''

    def __init__(self, mail_out, mail_to):
        self.mail_out = mail_out
        self. mail_to = mail_to

    def send_total_cases(self, totalcases):

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('erik.jareman@gmail.com', '*******')

        subject = 'Total Cases'
        body = 'World:' + totalcases

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail(self.mail_out, self.mail_to, msg)

        print(totalcases)
        server.quit()
