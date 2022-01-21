{\rtf1\ansi\ansicpg1252\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # this code is not working in jupyter enviornment.\
from requests_html import HTMLSession\
\
session = HTMLSession()\
\
url = 'https://www.youtube.com/c/setindia/videos'\
\
r = session.get(url)\
\
r.html.render(sleep=1, keep_page=True, scrolldown=1)\
\
videos = r.html.find('#video-title')\
\
video_list = []\
for item in videos:\
    video = \{\
        'title': item.text,\
        'link' : item.absolute_links\
    \}\
    video_list.append(video)}