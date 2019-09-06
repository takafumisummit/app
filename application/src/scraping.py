from bs4 import BeautifulSoup
import urllib.request as req
import re
import requests
import urllib.parse
import json


def main():
    #numbers = [2869,1771]#2945,2965,2965,1189,2169,
    sentence_list = []
    for number in range(2200,3000):
        try:
            name,total_sentence = Yugihoh_Scraping(str(number))
            sum_list = sumarization(total_sentence)
            if sum_list == 'next':
                continue
            else:
                sentence_list.append({'name':name, 'sentences':sum_list})
        except AttributeError:
            continue
    return sentence_list

def Yugihoh_Scraping(number):
    url = "https://yugioh-list.com/c_dtls/review/"+ number
    res = req.urlopen(url)
    soup = BeautifulSoup(res, 'html.parser')
    obj = soup.find('h2', id='review').a
    name = obj['name']
    sentences = soup.find_all('div', class_='subject', style='width:80%;')
    total_sentence = []
    for i in sentences:
        try:
            a = i.string.strip()
            txt = re.findall(r'[^。]+(?:[。]|$)', a)
            total_sentence += txt
        except AttributeError:
            continue
    return name,total_sentence

def sumarization(total_sentence):
    sum_list = ''
    if len(total_sentence)//50 == 0:
        return 'next'
    else:
        num = len(total_sentence)//10
        for i in range(0,num):
            try:
                txt = ','.join(total_sentence[i*10:i*10+9])

                data = [
                  ('apikey', 'DZZJwH0cU71OY99O5xbVOaIIDvygGNuX'),
                  ('sentences', txt),
                ]
                r =requests.post('https://api.a3rt.recruit-tech.co.jp/text_summarization/v1/', data=data)

                data = json.loads(r.text)
                sum_list += data['summary'][0].strip(',')
            except KeyError:
                pass

    return sum_list

if __name__ == '__main__':
    main()
