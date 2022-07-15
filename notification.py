import requests
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

MAIL_ENABLE = os.environ['MAIL_ENABLE']
MAIL_HOST = os.environ['MAIL_HOST']
MAIL_ACCOUNT = os.environ['MAIL_ACCOUNT']
MAIL_PW = os.environ['MAIL_PW']
MAIL_SENDER = os.environ['MAIL_SENDER']
MAIL_RECEIVER = os.environ['MAIL_RECEIVER']

# ===== cqhttp配置 =====
cqhttp = False  # 是否启用cqhttp
api = "http://127.0.0.1:5700/send_msg"  # cqhttp http API 地址
uid = ""  # 收信QQ号，不填则不发送
gid = ""  # 收信群号，不填则不发送
# ===== 邮件设置 =====
mail = MAIL_ENABLE  # 是否启用邮件
ssl = True  # 是否启用SSL
host = "MAIL_HOST"  # SMTP服务器地址（如smtp.qq.com）
port = 465  # 输入SMTP服务器端口（如465）
account = "MAIL_ACCOUNT"  # 发信账号
password = "MAIL_PW"  # 发信密码
sender = "MAIL_SENDER"  # 发信人邮箱
receiver = "MAIL_RECEIVER"  # 收信人邮箱


def msg(text):
    if cqhttp:
        send_cqhttp(text)
    if mail:
        send_mail(text)


def send_cqhttp(text):
    data_user = {
        "user_id": uid,
        "message": text
    }
    data_group = {
        "group_id": gid,
        "message": text
    }
    if data_user["user_id"] != "":
        requests.get(api, params=data_user)
    if data_group["group_id"] != "":
        requests.get(api, params=data_group)


def send_mail(text):
    if ssl:
        server = smtplib.SMTP_SSL(host, port)
    else:
        server = smtplib.SMTP(host, port)
    server.login(account, password)
    mail_msg = MIMEText(text, "plain", "utf-8")
    mail_msg["From"] = formataddr(["WHUT-AutoHealthReport", sender])
    mail_msg["Subject"] = "【WHUT-AutoHealthReport】"
    server.sendmail(sender, receiver, mail_msg.as_string())
    server.close()
