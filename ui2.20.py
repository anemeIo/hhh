import requests
from tkinter import *


def get_vid():
    api_key = "AIzaSyBV3BrrB23enM93FByisngccYGen1i5Fsk"
    query = cityField.get()

    url = f"https://www.googleapis.com/youtube/v3/search?key={api_key}&part=snippet&q={query}&maxResults=2&type=video"

    response = requests.get(url)
    data = response.json()

    for item in data["items"]:
        video_id = item["id"]["videoId"]
        video_title = item["snippet"]["title"]
        video_link = f"https://www.youtube.com/watch?v={video_id}"
        info['text'] = f"{video_title}"
        infolink['text'] = f"{video_link}"

root = Tk()
root['bg'] = '#fafafa'
# Указываем название окна
root.title('находи видео')
# Указываем размеры окна
root.geometry('1000x1000')
# Делаем невозможным менять размеры окна
root.resizable(width=False, height=False)

# Создаем фрейм (область для размещения других объектов)
# Указываем к какому окну он принадлежит, какой у него фон и какая обводка
frame_top = Frame(root, bg='#ffb700', bd=5)
# Также указываем его расположение
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

# Все то-же самое, но для второго фрейма
frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

# Создаем текстовое поле для получения данных от пользователя
cityField = Entry(frame_top, bg='white', font=30)
cityField.pack()  # Размещение этого объекта, всегда нужно прописывать

# Создаем кнопку и при нажатии будет срабатывать метод "get_weather"
btn = Button(frame_top, text='найти', command=get_vid)
btn.pack()

# Создаем текстовую надпись, в которую будет выводиться информация о погоде
info = Label(frame_bottom, text='название', bg='#ffb700', font=40)
info.pack()
infolink = Label(frame_bottom, text='ссылка', bg='#ffb700', font=40)
infolink.pack()

# Запускаем постоянный цикл, чтобы программа работала
root.mainloop()