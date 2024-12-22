def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
#    print(sender)
    if ('@' in sender and ('.com' in sender[-4:] or '.ru' in sender[-3:] or '.net' in sender[-4:])):
        if ('@' in recipient and ('.com' in recipient[-4:] or '.ru' in recipient[-3:] or '.net' in recipient[-4:])):
  #          print('Можно отправлять!!!')
            if recipient == sender:
                print('Нельзя отправить письмо самому себе!')
            elif sender == 'university.help@gmail.com':
                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
            elif sender != 'university.help@gmail.com':
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

#send_email('Hello', 'chajrob@mail.ru')
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.uk', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')