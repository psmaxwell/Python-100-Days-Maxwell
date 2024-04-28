"""
用户身份验证

Version: 0.1

Author: Maxwell 
"""
username = input('please input username: ')
password = input('please input password: ')

# username : admin and password: 123456 to verify
if username == 'admin' and password == '123456':
    print('Verification sucessful')
else:
    print('Verification failed')
