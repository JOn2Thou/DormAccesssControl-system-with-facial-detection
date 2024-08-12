import datetime

from django.core.mail import send_mail


def login_smtp(user, ip):
    subject = '宿舍门禁管理系统 - 登录提醒'  # 主题
    message = '内容'  # 内容
    sender = '宿舍门禁管理系统<yutite@qq.com>'
    receiver = [user[0].email]  # 目标邮箱
    now_time = datetime.datetime.now()
    now_time_str = datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
    html_message = '您的账户' + user[0].username + '在' + now_time_str + '登陆成功，登录IP：' + ip + '，如非本人登录，请及时修改密码！'   # 发送html格式
    send_mail(subject, message, sender, receiver, html_message=html_message)


def code_smtp(email, code):
    subject = '宿舍门禁管理系统 - 验证码'  # 主题
    message = '内容'  # 内容
    sender = '宿舍门禁管理系统<yutite@qq.com>'
    receiver = [email]  # 目标邮箱
    now_time = datetime.datetime.now()
    now_time_str = datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
    html_message = '您的验证码为：' + code + '，该验证码有效期为5分钟。'   # 发送html格式
    return send_mail(subject, message, sender, receiver, html_message=html_message)