from dingtalkchatbot.chatbot import DingtalkChatbot
from settings import base
# WebHook地址
# webhook = 'https://oapi.dingtalk.com/robot/send?access_token=803ff14513df896c84a82b4f9f418d0498d730577641b732bd532fcd19348d8f'
secret = 'SEC5ea2ef690cce56f768ba1039355da3bbe9c9efa6da2fbe9fa74a8c8721cbdfb3'  # 可选：创建机器人勾选“加签”选项时使用
# 初始化机器人小丁
# xiaoding = DingtalkChatbot(webhook)  # 方式一：通常初始化方式
def send(message, at_mobiles=[]):
    webhook = base.DINGTALK_WEB_HOOK
    xiaoding = DingtalkChatbot(webhook,secret=secret)
    xiaoding.send_text(msg=('面试通知：%s'%message),at_mobiles=at_mobiles)


