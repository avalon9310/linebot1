from django.shortcuts import render
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse,HttpResponseBadRequest,HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from linebot import LineBotApi, WebhookHandler,WebhookParser
from linebot.exceptions import InvalidSignatureError,LineBotApiError
from linebot.models import MessageEvent,TextSendMessage,TextMessage,ImageSendMessage
import random
import requests
from bs4 import BeautifulSoup
import numpy as np
import json
import time
from datetime import datetime

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parse=WebhookParser(settings.LINE_CHANNEL_SECRET)


def index(requests):
    return HttpResponse("<h1>Linebot APP</h1>")

@csrf_exempt    
def callback(request):
    words=['早安你好','天氣很不錯!','我準備去上班','快中午了','再說一次']
    if request.method=='POST':
        signature=request.META['HTTP_X_LINE_SIGNATURE']
        body=request.body.decode('utf-8')
        try:
            events=parse.parse(body,signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
        for event in events:
            if isinstance(event,MessageEvent):
                if isinstance(event.message,TextMessage):
                    message,image_url=None,None
                    text=event.message.text
                    print(text)  
                    if '大樂透'==text:
                        message=get_biglotto()
                    elif '中文' in text:
                        message=get_cmusic()
                    elif '日文' in text:
                        message=get_jmusic()
                    elif '西洋' in text:
                        message=get_wmusic()
                    elif '韓文' in text:
                        message=get_kmusic()
                    elif '台語' in text:
                        message=get_tmusic()
                    elif '粵語' in text:
                        message=get_hmusic()              
                    elif '樂透' in text:
                        message = lotto()
                    elif '早安' in text:
                        message='早安你好'
                    else:  
                        message=random.choice(words)
                                      
                else:
                    message='無法解析'
                   

                messageObject=TextSendMessage(text=message) if message is not None else \
                    ImageSendMessage(original_content_url=image_url,
                                    preview_image_url=image_url)   
                
                line_bot_api.reply_message(event.reply_token,messageObject)
                
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
    
def lotto():
    numbers = sorted(random.sample(range(1,50),6))
    result = ' '.join(map(str, numbers))
    n = random.randint(1, 50)

    return (f'{result} 特別號:{n}')


def get_biglotto():
    url='https://www.taiwanlottery.com.tw/lotto/lotto649/history.aspx'
    resp=requests.get(url)
    soup=BeautifulSoup(resp.text,'lxml')
    trs=soup.find('table',class_='table_org td_hm').find_all('tr')
    numbers=[td.text.strip() for td in trs[4].find_all('td')[1:]]
    numbers=' '.join(numbers[:-1])+' 特別號:'+numbers[-1]
    data1=[td.text.strip() for td in trs[0].find_all('td')]
    data2=[td.text.strip() for td in trs[1].find_all('td')]
    data=list(zip(data1,data2))
    title=':'.join(np.array(data).reshape(10))
    result=f'{title}\n{numbers}'
    return result

def get_cmusic():
    url="https://kma.kkbox.com/charts/api/v1/daily?category=297&lang=tc&limit=50&terr=tw&type=newrelease"
    response=requests.get(url)
    data=json.loads(response.text)
    song_list = data["data"]["charts"]["newrelease"]
    temp_str=''
    for i, song in enumerate(song_list[:20]):
        song_rank=song["rankings"]["this_period"]
        last_rank=song["rankings"]["last_period"]
        song_name=song["song_name"]
        song_artist=song["artist_name"]
        song_url=song["song_url"]    
        temp_str += f'{i+1}. {song_artist}-{song_name} 今日排名:{song_rank}, 上期排名:{last_rank}, 連結:{song_url}\n'
    return temp_str

def get_jmusic(): 
    url1="https://kma.kkbox.com/charts/api/v1/daily?category=308&lang=tc&limit=50&terr=tw&type=newrelease"
    response1=requests.get(url1)
    data1=json.loads(response1.text)
    song_list1 = data1["data"]["charts"]["newrelease"]
    temp_str1='' 
    for i, song1 in enumerate(song_list1[:20]):
        song_rank1=song1["rankings"]["this_period"]
        last_rank1=song1["rankings"]["last_period"]
        song_name1=song1["song_name"]
        song_artist1=song1["artist_name"]
        song_url1=song1["song_url"]    
        temp_str1 += f'{i+1}. {song_artist1}-{song_name1} 今日排名:{song_rank1}, 上期排名:{last_rank1}, 連結:{song_url1}\n'
    return temp_str1 
        


def get_wmusic():
    url2="https://kma.kkbox.com/charts/api/v1/daily?category=390&lang=tc&limit=50&terr=tw&type=newrelease"
    response2=requests.get(url2)
    data2=json.loads(response2.text)
    song_list2 = data2["data"]["charts"]["newrelease"]
    temp_str2=''
    for i, song2 in enumerate(song_list2[:20]):
        song_rank2=song2["rankings"]["this_period"]
        last_rank2=song2["rankings"]["last_period"]
        song_name2=song2["song_name"]
        song_artist2=song2["artist_name"]
        song_url2=song2["song_url"]    
        temp_str2 += f'{i+1}. {song_artist2}-{song_name2} 今日排名:{song_rank2}, 上期排名:{last_rank2}, 連結:{song_url2}\n'
    return temp_str2 




def get_kmusic(): 
    url3="https://kma.kkbox.com/charts/api/v1/daily?category=314&lang=tc&limit=50&terr=tw&type=newrelease"
    response3=requests.get(url3)
    data3=json.loads(response3.text)
    song_list3 = data3["data"]["charts"]["newrelease"]
    temp_str3=''
    for i, song3 in enumerate(song_list3[:20]):
        song_rank3=song3["rankings"]["this_period"]
        last_rank3=song3["rankings"]["last_period"]
        song_name3=song3["song_name"]
        song_artist3=song3["artist_name"]
        song_url3=song3["song_url"]    
        temp_str3 += f'{i+1}. {song_artist3}-{song_name3} 今日排名:{song_rank3}, 上期排名:{last_rank3}, 連結:{song_url3}\n'
    return temp_str3



def get_tmusic(): 
    url4="https://kma.kkbox.com/charts/api/v1/daily?category=304&lang=tc&limit=50&terr=tw&type=newrelease"
    response4=requests.get(url4)
    data4=json.loads(response4.text)
    song_list4 = data4["data"]["charts"]["newrelease"]
    temp_str4=''  
    for i, song4 in enumerate(song_list4[:20]):
        song_rank4=song4["rankings"]["this_period"]
        last_rank4=song4["rankings"]["last_period"]
        song_name4=song4["song_name"]
        song_artist4=song4["artist_name"]
        song_url4=song4["song_url"]    
        temp_str4 += f'{i+1}. {song_artist4}-{song_name4} 今日排名:{song_rank4}, 上期排名:{last_rank4}, 連結:{song_url4}\n'
    return temp_str4 


def get_hmusic(): 
    url5="https://kma.kkbox.com/charts/api/v1/daily?category=320&lang=tc&limit=50&terr=tw&type=newrelease"
    response5=requests.get(url5)
    data5=json.loads(response5.text)
    song_list5 = data5["data"]["charts"]["newrelease"]
    temp_str5=''   
    for i, song5 in enumerate(song_list5[:20]):
        song_rank5=song5["rankings"]["this_period"]
        last_rank5=song5["rankings"]["last_period"]
        song_name5=song5["song_name"]
        song_artist5=song5["artist_name"]
        song_url5=song5["song_url"]    
        temp_str5 += f'{i+1}. {song_artist5}-{song_name5} 今日排名:{song_rank5}, 上期排名:{last_rank5}, 連結:{song_url5}\n'
    return temp_str5