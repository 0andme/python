# 이메일 기본 패키지를 가져온다
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
# 정규표현식을 가져오는 패키지
import re

# SMTP 서버 이용을 위한 data
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
SMTP_USER = 'yu00mi97@gmail.com'
SMTP_PASSWORD = 'dbdudal**97'

# 함수 - 이메일을 발송하는 함수
# attachment-첨부파일을 위한 파라미터
def send_mail(name, addr, subject, contents, attachment):
    # 이메일 유효성 검사-정규표현식
    # 패턴과 addr가 일치한지 판단하여 결과 return
    # ^ : 문자열의 시작 [a부터z, A부터Z,0-9,_ . -올수있다]
    # + : 앞의 문자가 하나이상나온다
    # @ : @가 나온다.
    # \. : .무조건 와야한다.
    # $ : 문자열의 끝
    if not re.match('(^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', addr):
        print('Wrong email')
        return
    # text메일을 보낼 것이라는 의미
    msg = MIMEMultipart('alternative')
    # 첨부파일이 있다면 아래 문장으로 변경
    if attachment:
        # mixed : text뿐 아니라 data를 가지고 있다는 뜻
        msg = MIMEMultipart('mixed') 

    # 보낼 메일을 정해진 양식대로 작성
    msg['From'] = SMTP_USER
    msg['To'] = addr
    msg['Subject'] = name + '님, ' + subject
    # contents를 위한 기본 설정-아래는 텍스트를 위한 것
    text = MIMEText(contents, _charset='utf-8')
    # text를 msg에 넣음. attach를 통해
    # 문자, 이미지 등을 계속해서 붙여나갈수 있음 
    msg.attach(text)
    # 첨부파일이 있으면 MIMEBase 패키지 가져와야함
    if attachment:
        from email.mime.base import MIMEBase
        from email import encoders
        # 파일을 읽어온다 
        file_data = MIMEBase('application', 'octect-stream')
        # rb : 바이너리로 읽기 모드
        # 파일을 열고 내용을 read()로 읽고 그 내용을 file_data에 넣기
        file_data.set_payload(open(attachment, 'rb').read())
        # smtp 서버에서 원하는 형식으로 첨부 파일 인코딩
        encoders.encode_base64(file_data)

        # 파일명을 뽑아내주는 패키지 OS
        import os
        filename = os.path.basename(attachment)
        file_data.add_header('Content-Disposition', 'attachment; filename="'+filename+'"')
        msg.attach(file_data)
    # 서버에 접속할 준비
    smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    # 서버에 로그인 
    smtp.login(SMTP_USER, SMTP_PASSWORD)
    # 메일 보내기- msg를 문자열로 전환 
    smtp.sendmail(SMTP_USER, addr, msg.as_string())
    smtp.close()
# 보낼 내용
contents = '''안녕하세요.

자동화로 보내지는 메일입니다. '''
# send_mai 함수 호출
send_mail('0amdme', '21_smilebom@naver.com', '자동화 메일입니다.', contents, 'test.txt')