# file_worker
1. Даний модуль був створений, аби допомагати юзеру орієнтуватися в json файлі. Програма висвітлює користувачу підказки(тип певної структури даних, його елементи(якщо список) або ключі(якщо словник).
2. Програма надає користувачу дані про структуру(його елементи, з чого він складається) json файлу. Завдяки цій інформації користувач може легко дізнатися де знаходиться потрібна йому інформація і як до неї доступитися.
Примітка: даний модуль працює лише з json файлами, тому перед початком роботи файл, з яким юзер планує працювати, повинен знаходитися в одній папці що й сам модуль.
3.Приклад запуску модуля(Аргумент: user_timeline_obama.json. Примітка: на зображенні програма працює з меншим файлом аніж він є в оригінальному вигляді.
![Знімок екрана (788)](https://user-images.githubusercontent.com/73779019/108887149-8652e300-7612-11eb-900b-92e03afca8db.png)
Коротко про деякі функції модуля:
1) def get_info - дістає з певної структури даних(словника) значення його елементів(ключів). get_info('data',{'data':123,'info':'name'})(перший аргумент - назва ключа,другий сама структура даних). Щоб відбувся виклик цієї функції, дані, які обробляються, повинні містити спеціальне значення, яке має дорівнювати одиниці(якщо нуль то не буде виклику функції).
Це значення даним(залежно від їхнього типу)надає функція thinker, яка відповідає за визначення типу.
2) def info_list - повертає список елементів або ключів певної структури даних.
Приклад:
list = [(('entities', "<class 'dict'>"),('source', "<class 'str'>")),(('id', "<class 'dict'>"),('loc', "<class 'str'>"))]
info_list(list,0) - означає, що функція поверне ['entities', 'source']. Кожен елемент list - це окремий елемент попередньої структури даних.
Приклад:
  [
  {entities:{.......}},
  {source:'string'},
  {id:{......}},
  {loc:'data'}
  ]
Другий елемент кожного кортежа(списку list) відповідає за:
1.  Якщо перший елемент тапла: id ключ словника, то другий елемент - це type(dict['id'])
2.  Якщо перший елемент тапла: loc елемент списку, то другий елемент - це type('loc')
