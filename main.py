from tkinter import *
from tkinter.messagebox import showerror
import requests


def get_ip():
    url = f'https://ipinfo.io/json' # ссылка на запрос текущего ip в формате json
    try:
        response = requests.get(url, stream=True) # получили данные
        response.raise_for_status()
        ip_client = response.json()
        print(response) # вывели статус соединения
        value_1 = list(ip_client.values())[0] # нулевое значение словаря
        value_2 = list(ip_client.values())[4] # четвертое значение словаря
        formatted_value = f'IP: {value_1}\nСтрана: {value_2}'
        label_ip.config(text=formatted_value) # направляем результат в метку
        return formatted_value
    except requests.exceptions.ConnectionError: # исключения
        print("Ошибка соединения с API")
        showerror(title='Ошибка', message='Ошибка соединения с API')
    except requests.exceptions.Timeout:
        print("Превышено время ожидания ответа API")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP ошибка: {err}")
    except Exception as err:
        print(f"Другая ошибка: {err}")


window = Tk()
window.title('VPN')
# размер окна и параметры его отображения(посередине экрана)
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
width_position = screenwidth // 2 - 150
height_position = screenheight // 2 - 150
window.geometry(f'300x300+{width_position}+{height_position}')

# метка и кнопка, чтобы запустить функцию get_ip
label_info = Label(text='Нажми чтобы узнать свой IP')
label_info.pack()
button_url = Button(text='Тык', command=get_ip)
button_url.pack(pady=20)

# метка с результатом функции get_ip
label_text_ip = Label(text='Данные вашего компьютера:')
label_text_ip.pack()
label_ip = Label(window)
label_ip.pack()

window.mainloop()