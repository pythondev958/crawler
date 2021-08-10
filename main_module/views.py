from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.

def index(request):
    return render(request,"login.html")


def registration(request):
    return render(request, "registration.html")


from datetime import date


def login(request):
    return render(request, "login.html")

    CODate = models.CharField(max_length=100)  # required  charge off date
    AccountOpenDate = models.CharField(max_length=100)  # required
    CurBalance = models.CharField(max_length=100)  # required
    pbirthdate = models.CharField(max_length=100)  # required
    firstcity = models.CharField(max_length=100)  # required
    firstzippostal = models.CharField(max_length=100)  # required
    score = models.CharField(max_length=100)  # it will be predicted
def getReport(request):
    if 'first' in request.POST:
        import requests
        from bs4 import BeautifulSoup

        # Defining the url of the site
        base_site = "https://www.babnet.net/"

        response = requests.get(base_site)

        html = response.content

        soup = BeautifulSoup(html, "html.parser")

        x1 = soup.find_all('h2', class_='post-title arabi')
        x2 = soup.find_all('h2', class_='post-title title-medium arabi')
        x3 = soup.find_all('h2', class_='post-title title-small arabi')
        x4 = x1 + x2 + x3
        aa = BeautifulSoup(str(x4), "html.parser")

        links = aa.find_all('a')

        from urllib.parse import urljoin

        relative_urls = [link.get('href') for link in links]

        full_urls = [urljoin(base_site, url) for url in relative_urls]

        article = []
        titles = []
        types = []

        i = 0

        for url in full_urls[0:100]:
            note_resp = requests.get(url)

            if note_resp.status_code != 200:
                print('Status code {0}: Skipping URL #{1}: {2}'.format(note_resp.status_code, i + 1, url))
                i = i + 1
                continue

            note_html = note_resp.content

            note_soup = BeautifulSoup(note_html, 'lxml')

            for div in note_soup.find_all("div", {'class': 'noprint'}):
                div.decompose()

            for src in note_soup.find_all("span", {'class': 'source'}):
                src.decompose()

            note_pars = note_soup.find_all('div', class_='entry-content arabi')

            note_titles = note_soup.find_all('h2', class_='post-title arabi')

            note_types = note_soup.find_all('li', class_='nav-item active')

            art = [(p.text).replace('\n', '').replace('\t', '').replace('\r', '') for p in note_pars]
            tit = [(t.text).replace('\n', '').replace('\t', '').replace('\r', '') for t in note_titles]
            typ = [(ty.text).replace('\n', '').replace('\t', '').replace('\r', '') for ty in note_types]

            article.append(str(art)[2:-2])
            titles.append(str(tit)[2:-2])
            types.append(str(typ)[2:-2])

            i = i + 1

        print('-------------------------- SCRAPING DONE --------------------------')

        import pandas as pd

        df = pd.DataFrame(list(zip(full_urls, titles, article, types)), columns=['link', 'titles', 'article', 'type'])
        path = ('BabNet.csv')
        # df.to_csv(path, encoding='utf-8-sig')
        return HttpResponse(df.to_html())

    if 'second' in request.POST:
        import re
        from urllib.parse import urlparse
        import os
        download_google(
            'https://www.google.com/search?q=flowers&sxsrf=ALeKk00uvzQYZFJo03cukIcMS-pcmmbuRQ:1589501547816&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjEm4LZyrTpAhWjhHIEHewPD1MQ_AUoAXoECBAQAw&biw=1440&bih=740')
        myfile=open('images_flowers.txt','r')
        data=myfile.readlines()

        myfile.close()
        print(type(data))
        grades=[]
        for i in range(len(data)):
            grades.append(data[i].strip('\n'))
        print(grades)
        del grades[0]
        return render(request, "images.html",{'links':grades})



def download_google(url):
    import requests
    from bs4 import BeautifulSoup
        # url = 'https://www.google.com/search?q=flowers&sxsrf=ALeKk00uvzQYZFJo03cukIcMS-pcmmbuRQ:1589501547816&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjEm4LZyrTpAhWjhHIEHewPD1MQ_AUoAXoECBAQAw&biw=1440&bih=740'
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    f = open("images_flowers.txt", "w")
    res = []
    for raw_img in soup.find_all('img'):
        link = raw_img.get('src')
        res.append(link)
        if link:
            f.write(link + "\n")


    f.close()


def registration2(request):
    name = request.POST['name']
    email = request.POST['email2']
    username = request.POST['username']
    password = request.POST['password']
    from .models import registration
    obj = registration(name=name, email=email, username=username, password=password)
    obj.save()
    return render(request, "login2.html")

from random import randint as ml_metric
def login_check(request):
    input_email=request.POST['email']
    input_password=request.POST['password']
    from .models import registration

    temp = registration.objects.all()
    emails = list(temp.values_list('email', flat=True))
    passwords = list(temp.values_list('password', flat=True))

    e=False
    p=False
    for item in emails:
        print(item)
    if input_email in emails:
        e=True
    if input_password in passwords:
        p=True

    if e==True and p==True:
        print('success')
        return render(request,"index.html")

    else:
        print('failed')
        return render(request,"login3.html")

