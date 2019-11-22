# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 11:31
# @Author  : Wang Bingyin
# @Email   : xxxxxxx@163.com
# @File    : email_uitl.py
# @Software: PyCharm
import smtplib
from Common.base_path import reports_html
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class SendMail(object):
    def __init__(self,username,passwd,recv,title,content,
                 file=None,
                 email_host='smtp.163.com',port=25):
        self.username = username
        self.passwd = passwd
        self.recv = recv
        self.title = title
        self.content = content
        self.file = file
        self.email_host = email_host
        self.port = port
    def send_mail(self):
        msg = MIMEMultipart()
        #发送内容的对象
        if self.file:#处理附件的
            att = MIMEText(open(self.file, encoding='utf-8').read())
            att["Content-Type"] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename="%s"'%self.file
            msg.attach(att)
        msg.attach(MIMEText(self.content))#邮件正文的内容
        msg['Subject'] = self.title  # 邮件主题
        msg['From'] = self.username  # 发送者账号
        msg['To'] = self.recv  # 接收者账号列表
        self.smtp = smtplib.SMTP(self.email_host,port=self.port)
        #发送邮件服务器的对象
        self.smtp.login(self.username,self.passwd)
        try:
            self.smtp.sendmail(self.username,self.recv,msg.as_string())
        except Exception as e:
            print('出错了。。',e)
        else:
            print('发送成功！')
    def __del__(self):
        self.smtp.quit()

if __name__ == '__main__':
    m = SendMail(
        username='15942123962@163.com', passwd='qwe12345', recv='wangbingyin-zkhtg@gome.com.cn',
        title='新鞋的发送邮件', content='哈哈哈啊哈哈哈哈', file=reports_html
    )
    m.send_mail()

