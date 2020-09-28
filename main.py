from requests_html import HTMLSession
from src.win10toast.win10toast import ToastNotifier
#call_back feature was not merged into the web10toast so i had to 
#pull the version i needed .
import time
import webbrowser

session = HTMLSession()
h = ToastNotifier()

url = 'https://blackclover.online'

prev_chapter = 263

def check_new():
    global prev_chapter
    r = session.get(url)
    r.html.render(sleep=1, keep_page=True, scrolldown=1)

    chapter_info = r.html.find('.col-6', first = True).text
    chapter_no = int(chapter_info[22:25])

    chapter_link = r.html.find('.col-6', first = True).absolute_links
    chapter_link = str(chapter_link)
    chapter_link = chapter_link[2:len(chapter_link)-2]
    print(chapter_link)
   
    if chapter_no > prev_chapter :
       send_notif(chapter_info , chapter_link)
       prev_chapter = chapter_no

def send_notif(chapter_info , chapter_link):
    h.show_toast("New Black Clover Chapter :" + chapter_info , chapter_link ,
                   duration=None , callback_on_click =lambda: open_link(chapter_link))

def open_link(url):
    webbrowser.open_new(url)

while(True):
    check_new()
    time.sleep(60 * 60 * 24)