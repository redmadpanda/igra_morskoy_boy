# используем библиотеку tkinter
from tkinter import *
# чтобы использовать окно, хотим ли мы закрывать окно
from tkinter import messagebox
# импортируем модуль для задержки кадра
import time

# создадим рабочую область для нашей игры
tk = Tk()
# создадим переменную которая будет отслеживать, что \
# наше приложение все еще работает
app_running = True

# окошко нашего приложения сделаем фиксированным размером
size_canvas_x = 600
size_canvas_y = 600

# пропишем функцию при закрытия окна
def on_closing():
	# чтобы передать наружу значение 
	global app_running
	# выведем окно для подтверждения
	if messagebox.askokcancel("Выход из игры", "Хотите выйти из игры?"):
		app_running = False
		tk.destroy()

# пропишем что будем делать на момент закрытия окна, запустим 
# нашу функцию on_closing
tk.protocol("WM_DELETE_WINDOW", on_closing)

# определим параметры нашего окна
# название окна
tk.title("Игра Морской Бой")
# пропишем чтобы размер окна нельзя было менять
tk.resizable(0,0)
# зададим атрибут, что наше окно должно быть поверх всех окон
tk.wm_attributes("-topmost", 1)

# создадим canvas для нашего приложения 
canvas = Canvas(tk, width = size_canvas_x, height = size_canvas_y, bd = 0, highlightthickness = 0)
# на канвасе создадим прямоугольник белого цвета
canvas.create_rectangle(0,0, size_canvas_x, size_canvas_y, fill = "white")
# запакуем наш канвас
canvas.pack()
# и обновим tk
tk.update()

# сделаем цикл для работы нашего приложения
while app_running:
	if app_running:
		tk.update_idletasks()
		tk.update()
	time.sleep(0.005)


