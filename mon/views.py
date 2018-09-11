from django.shortcuts import render
import requests

def index(request):
    urls = [
           ['http://kkoon.duckdns.org:8888', '2018 HYUNDAI AUTOEVER CORP', '', ''],
           ['http://kkoon.duckdns.org:8000', '2018 HYUNDAI AUTOEVER CORP', '', ''],
           ['http://kkoon.duckdns.org:8000/faq/', 'Recently Answers', '', ''],
           ['http://kkoon.duckdns.org:8000/faq/4/', '아이디/비밀번호를 알고 싶습니다.', '', ''],
           ['http://kkoon.duckdns.org:8000/faq/5/', '아이디/비밀번호를 알고 싶습니다.', '', ''],
        ]

#    msg = check_alive('http://kkoon.duckdns.org', '2018 HYUNDAI AUTOEVER CORP')
    for url in urls:
        res = check_alive(url[0], url[1])
        url[2] = res[0]
        url[3] = res[1]
    context = {'results':urls}
    return render(request, 'index.html', context)

def check_alive(url, txt):
    msg = ["비정상", "orange"]
    try:
        with requests.Session() as s:
            req = s.get(url)
            if req.text.find(txt) > -1:
                msg = ["정상", "green"]
    except:
        msg = ["점검오류", "red"]
    return msg
