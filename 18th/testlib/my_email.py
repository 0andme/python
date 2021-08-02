class Email:
    def __init__(self):
        self.from_email = ''
        self.to_email = ''
        self.subject = ''
        self.contents = ''

    def send_mail(self):
        print('From: '+ self.from_email)
        print('To: '+ self.to_email)
        print('Subject: '+ self.subject)
        print('Contents: '+ self.contents)

if __name__ == '__main__':
    e = Email()
    e.from_email = 'alghost@gmail.com'
    e.to_email = 'yskim@gmail.com'
    e.subject = 'subject'
    e.contents = 'contents'
    e.send_mail()