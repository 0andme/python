def send_mail(from_email, to_email, subject, contents):
    print('From:\t' + from_email)
    print('To:\t' + to_email)
    print('Subject: ' + subject)
    print('Contents')
    print('*'*10)
    print(contents)
    print('*'*10)
    print('-'*10)

my_email = 'yskim@fastcampus.com'

users = []
users.append({'name':'john', 'email':'john@gmail.com'})
users.append({'name':'ray', 'email':'ray@gmail.com'})
users.append({'name':'jay', 'email':'jaygmail.com'})

contents = '''Thank you!
- Fastcampus'''
for user in users:
    title = 'Dear. ' + user['name']
    if '@' not in user['email']:
        continue
    send_mail(my_email, user['email'], title, contents)