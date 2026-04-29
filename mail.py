import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")

site_name = "https://dvmn.org/referrals/O4w62S83RdL7taQOLhpAbfnnOJtFhQndmLAxHndr/!"
friend_name = "gergygho@yandex.ru"
sender_name = "devmanorg@yandex.ru"

letter = """\
From: ivan@yandex.ru
To: petr@yandex.ru
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
@ghost00763
Comment
"""

letter = letter.replace("ivan@yandex.ru","devmanorg@yandex.ru")
letter = letter.replace("petr@yandex.ru","gergygho@yandex.ru")
letter = letter.replace("%website%","https://dvmn.org/profession-ref-program/boshkaev2001/UAMDR/" )
letter = letter.replace("%friend_name%","Грек")
letter = letter.replace("%my_name%","Иван")

letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(login, password)
server.sendmail(sender_name,friend_name, letter)
server.quit()