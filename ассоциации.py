import requests


def associations(theme):
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 YaBrowser/19.10.0.1522 Yowser/2.5 Safari/537.36'}


    ok = []

    to_work = []
    answ = requests.get('https://zen.yandex.ru/api/v3/launcher/suggest?from_person=&search_text=' + theme, headers=head).text
    for i in answ.split('"normal_title":"')[1:]:
        if i.split('"')[0] not in to_work:
            to_work.append(i.split('"')[0])
    for i in to_work:
        answ = requests.get('https://zen.yandex.ru/t/' + i.replace(' ', ''), headers=head).text
        for j in answ.split('<h3 class="interest-tag__title">')[1:]:
            if j.split('</h3>')[0] not in ok:
                ok.append(j.split('</h3>')[0])
    if ok == []:
        ok.extend(to_work)
    return ok

while 1:
    print('\n'.join(associations(input('Тема: '))))
