from celery import Celery
import time
app = Celery("task",broker="redis://localhost:6379/0",backend="redis://localhost:6379/0")

@app.task
def send_email():
    print("邮件开始发送")
    time.sleep(3)
    print("邮件发送完成")