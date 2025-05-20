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
# определим размер игрового поля 
s_x = s_y = 10
# определим расстояния между линиями на поле
# шаг по горизонтали
step_x = size_canvas_x // s_x
# шаг по вертикали 
step_y = size_canvas_y // s_y
# повторно скорректируем размер окна, если будет остаток 
# от целочисленного деления 
size_canvas_x = step_x * s_x
size_canvas_y = step_y * s_y

# создадим окно отладки справа, где будут кнопки и др инфа
menu_x = 250



# пропишем функцию при закрытия окна
def on_closing():
	# чтобы передать наружу значение 
	global app_running
	# выведем окно для подтверждения
	if messagebox.askokcancel("Выход из игры", "Хотите выйти из игры?"):
		app_running = False
		tk.destroy()

# пропишем (обработчик событий) что будем делать на момент 
# закрытия окна, запустим нашу функцию on_closing
tk.protocol("WM_DELETE_WINDOW", on_closing)

# определим параметры нашего окна
# название окна
tk.title("Игра Морской Бой")
# пропишем чтобы размер окна нельзя было менять
tk.resizable(0,0)
# зададим атрибут, что наше окно должно быть поверх всех окон
tk.wm_attributes("-topmost", 1)


# создадим canvas для нашего приложения, а также 
# меню для отладки и кнопок 
canvas = Canvas(tk, width = size_canvas_x + menu_x, height = size_canvas_y, bd = 0, highlightthickness = 0)
# на канвасе создадим прямоугольник белого цвета
canvas.create_rectangle(0,0, size_canvas_x, size_canvas_y, fill = '#B8F5F7')
# запакуем наш канвас
canvas.pack()
# и обновим tk
tk.update()

# -----------функции будут тут----------------
# ф для прорисовки клеток в нашем поле
def draw_table():
	# нарисуем вертикальные линии
	for i in range(0, s_x + 1):
		canvas.create_line(step_x*i, 0, step_x*i, size_canvas_y)
		# рисует диагональ, пример
		#canvas.create_line(0,0,size_canvas_x,size_canvas_y)
	# нарисуем горизонтальные линии
	for i in range(0, s_y + 1):
		canvas.create_line(0, step_y*i, size_canvas_x, step_y*i)

# ф для кнопок
def button_show_enemy():
	pass

def button_begin_again():
	pass

#---------------------------------------------


# вызовем функцию чтобы нарисовать клетки
draw_table()

# создадим 2 кнопки в нашем окне (укажем какую функцию вызывает) 
# и их расположение 
b0 = Button(tk, text = 'Показать корабли противника', command = button_show_enemy)
b0.place(x = size_canvas_x + 20, y = 30)
b1 = Button(tk, text = 'Начать заново!', command = button_begin_again)
b1.place(x = size_canvas_x +20, y = 70)



# сделаем цикл для работы нашего приложения
while app_running:
	if app_running:
		tk.update_idletasks()
		tk.update()
	time.sleep(0.005)


