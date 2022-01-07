from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import time
root = Tk()
root.title('Приложение Банкомат')
def on_closing():
    '''
    :return: window when trying to close the application
    '''
    if messagebox.askokcancel('Выход из приложения банкомат', 'Вы уверены, что хотите закрыть приложение?'):
        root.destroy()
# function that is triggered when the main window is closed
root.protocol('WM_DELETE_WINDOW', on_closing)
root.resizable(0,0)
root.geometry('1250x750+150+50')
root.wm_attributes('-topmost', 1)
# ATM picture
photo_bank = ImageTk.PhotoImage(Image.open("tinkoff.jpg"))
bank = Label(root, width=1250, height=750, image = photo_bank)
bank.pack()
root.update()

# application usage information
information = Tk()
information.title('Ознакомьтесь!')
information.resizable(0, 0)
information.wm_attributes('-topmost', 1)
information.geometry('+500+200')
Label(information, text ='Данная информация представляет собой навигацию по приложению', font = ('SchoolBook', 18)).pack()
Label(information).pack()
Label(information, text ='Ваш PIN-code: 0000', font = ('SchoolBook', 15), bg='lightblue').pack(anchor = NW)
Label(information, text ='Ваш баланс: 5000', font = ('SchoolBook', 15), bg='lightblue').pack(anchor = NW)
Label(information).pack()
Label(information, text ='Навигация по клавиатуре:', font = ('SchoolBook', 12), bg='lightgreen').pack(anchor = NW)
Label(information, text ='Enter - Далее').pack(anchor = NW)
Label(information, text ='Cancel - Удаляет последний символ').pack(anchor = NW)
Label(information, text ='Clear - стирает весь текст').pack(anchor = NW)
Label(information).pack()
Label(information, text ='Навигация по банкомату:', font = ('SchoolBook', 12), bg='lightgreen').pack(anchor = NW)
Label(information, text ='Боковые кнопки - перемещение по окнам банкомата').pack(anchor = NW)
Label(information, text ='Чтобы вставить карту (начать обслуживание) - нажмите на кнопку "вставить карту"').pack(anchor = NW)
Label(information, text ='Чтобы забрать карту (завершить обслуживание) - нажмите на боковую кнопку напротив функции "забрать карту"').pack(anchor = NW)
Label(information, text ='Чтобы вставить или снять купюру - нужно внести желаемую сумму, купюра сама появится').pack(anchor = NW)
Label(information, text ='У Вас 3 попытки, чтобы ввести правильный ПИН-код! Иначе, обслуживание прекратится', bg="lightpink").pack(anchor = NW)

option_card = False        # indicates whether the card is inserted or not
                           # provides tolerance for side button presses from the screen
b_one = False
b_two = False
b_three = False
b_four = False
b_five = False
b_six = False
number_of_attempts = 2     # number of attempts to enter a pin code
option_pin_code = False    # an option that shows whether the pin code was entered or not
option_get_money = False   # admission to the issue of money
option_give_money = False  # admission to the return of money
animation_money = False    # animation admission
PIN = '0000'               # PIN code of the card
balance = 5000             # card balance

photo_card = ImageTk.PhotoImage(Image.open("card_t.jpg"))       # picture of a bank card
photo_window_card = ImageTk.PhotoImage(Image.open("wind.jpg"))  # terminal
photo_money = ImageTk.PhotoImage(Image.open("money_t.jpg"))     # picture of banknotes

def animation_get_money():
    '''
    :return: animation for issuing a bill
    '''
    canvas= Canvas(root, width = 295, height = 129, highlightthickness=0, bd = 0)
    canvas.place(x=920, y=335)
    canvas.create_image(150, 65, image = photo_window_card)
    money = canvas.create_image(150, -110, image=photo_money)
    for i in range(1,150):
        canvas.move(money, 0, 3)
        root.update()
        time.sleep(0.005)
    canvas.destroy()

def animation_give_money():
    '''
    :return: animation on the return of the bill
    '''
    global animation_money
    if animation_money:
        canvas = Canvas(root, width=295, height=129, highlightthickness=0, bd=0)
        canvas.place(x=920, y=335)
        canvas.create_image(150, 65, image=photo_window_card)
        money = canvas.create_image(150, 250, image=photo_money)
        for i in range(1, 150):
            canvas.move(money, 0, -3)
            root.update()
            time.sleep(0.005)
        canvas.destroy()
        animation_money = False

def animation_give_card():
    '''
    :return: card release animation
    '''
    canvas = Canvas(root, width=295, height=129, highlightthickness=0, bd=0)
    canvas.place(x=920, y=619)
    canvas.create_image(150, 65, image=photo_window_card)
    money = canvas.create_image(150, 250, image=photo_card)
    for i in range(1, 150):
        canvas.move(money, 0, -3)
        root.update()
        time.sleep(0.005)
    canvas.destroy()

def animation_get_card():
    '''
    :return: card issuance animation
    '''
    canvas = Canvas(root, width=295, height=129, highlightthickness=0, bd=0)
    canvas.place(x=920, y=619)
    canvas.create_image(150, 65, image=photo_window_card)
    money = canvas.create_image(150, -110, image=photo_card)
    for i in range(1, 150):
        canvas.move(money, 0, 3)
        root.update()
        time.sleep(0.005)
    canvas.destroy()

def add_digit(digit):
    '''
    :param digit: input digit
    :return: number
    '''
    try:
        value = entry.get() + str(digit)
        entry.delete(0, END)
        entry.insert(0, value)
    except:
        return None

def delete_digit():
    '''
    :return: delete digit
    '''
    try:
        value = str(entry_pin.get())[:len(str(entry_pin.get())) - 1]
        entry.delete(0, END)
        entry.insert(0, value)
    except:
        return None

def clear_digit():
    '''
    :return: entry clearing
    '''
    try:
        value = ''
        entry.delete(0, END)
        entry.insert(0, value)
    except:
        return None

def enter():
    '''
    :return: continuation
    '''
    try:
        global option_pin_code
        global option_get_money
        global option_card
        global b_one
        global b_two
        global b_three
        global b_four
        global b_five
        global b_six
        global entry
        global balance
        global number_of_attempts
        global attempts_to_enter
        value = entry.get()
        if option_pin_code == True: # triggered when we press Enter when entering the pin code
            if value == PIN and number_of_attempts > 0:
                entry.destroy()
                option_card = True
                Label(root, image=photo_menu, bd=0).place(x=115, y=190)
                b_one = True
                b_two = True
                b_three = True
                b_four = True
                b_five = True
                b_six = True
                option_pin_code = False
            elif value != PIN and number_of_attempts > 0:
                number_of_attempts -= 1
                messagebox.showerror('НЕВЕРНЫЙ ПИН-КОД', 'Вы ввели неверный пин-код, попробуйте еще раз')
                attempts_to_enter.configure(text=str(number_of_attempts))
                entry.delete(0, END)
                entry.insert(0, '')
            elif number_of_attempts ==  0:
                messagebox.showerror('НЕВЕРНЫЙ ПИН-КОД', 'Вы ввели неверный пин-код 3 раза! Обслуживание прекращено!')
                entry.destroy()
                animation_get_card()
                number_of_attempts = 2
                option_card = False
                Label(root, image=photo_main, bd=0).place(x=115, y=190)

        if option_get_money == True: # works when we click on Enter when entering the amount for issuing money
            balance = int(balance)
            if int(value) <= balance and int(value) > 0:
                balance -= int(value)
                print(balance)
                entry.destroy()
                messagebox.showinfo('Операция по выдаче наличных', 'Операция успешно выполнена! Вернитесь в главное меню')
                animation_get_money()
                b_two = False
                b_three = False
                b_four = False
                b_five = False
                option_get_money = False
            elif int(value) > balance:
                messagebox.showerror('Ошибка операции', 'На вашем счете недостаточно средств. Выберете другую сумму или '
                                                        'вернитесь в главное меню')
                entry.delete(0, END)
                entry.insert(0, '')

        if option_give_money == True: # triggered when we press Enter when entering the amount for the return of money
            balance = int(balance)
            if int(value) >=100 and int(value) <= 50000:
                animation_give_money()
                balance += int(value)
                print(balance)
                entry.destroy()
                messagebox.showinfo('Операция пополнения  баланса', 'Операция успешно выполнена! Вернитесь в главное меню')
                b_one = False
                b_three = False
                b_four = False
                b_five = False
            else:
                messagebox.showerror('Ошибка операции', 'Вносимая сумма должна быть в диапазоне 100 и 50000')
                entry.delete(0, END)
                entry.insert(0, '')

    except:
        return None



# digit 1
photo_1 = ImageTk.PhotoImage(Image.open('1.jpg'))
button_1 = Button(root, image = photo_1, bd = 0, relief = FLAT, command=lambda : add_digit(1)).place(x = 250, y = 520)
# digit 2
photo_2= ImageTk.PhotoImage(Image.open('2.jpg'))
button_2 = Button(root, image = photo_2, bd = 0, relief = FLAT, command=lambda : add_digit(2)).place(x = 320, y = 520)
# digit 3
photo_3 = ImageTk.PhotoImage(Image.open('3.jpg'))
button_3 = Button(root, image = photo_3, bd = 0, relief = FLAT, command=lambda : add_digit(3)).place(x = 390, y = 520)
# digit 4
photo_4 = ImageTk.PhotoImage(Image.open('4.jpg'))
button_4 = Button(root, image = photo_4, bd = 0, relief = FLAT, command=lambda : add_digit(4)).place(x = 250, y = 575)
# digit 5
photo_5 = ImageTk.PhotoImage(Image.open('5.jpg'))
button_5 = Button(root, image = photo_5, bd = 0, relief = FLAT, command=lambda : add_digit(5)).place(x = 320, y = 575)
# digit 6
photo_6 = ImageTk.PhotoImage(Image.open('6.jpg'))
button_6 = Button(root, image = photo_6, bd = 0, relief = FLAT, command=lambda : add_digit(6)).place(x = 390, y = 575)
# digit 7
photo_7 = ImageTk.PhotoImage(Image.open('7.jpg'))
button_7 = Button(root, image = photo_7, bd = 0, relief = FLAT, command=lambda : add_digit(7)).place(x = 250, y = 630)
# digit 8
photo_8 = ImageTk.PhotoImage(Image.open('8.jpg'))
button_8 = Button(root, image = photo_8, bd = 0, relief = FLAT, command=lambda : add_digit(8)).place(x = 320, y = 630)
# digit 9
photo_9 = ImageTk.PhotoImage(Image.open('9.jpg'))
button_9 = Button(root, image = photo_9, bd = 0, relief = FLAT, command=lambda : add_digit(9)).place(x = 390, y = 630)

photo_none = ImageTk.PhotoImage(Image.open('none.jpg'))
button_none = Button(root, image = photo_none, bd = 0, relief = FLAT).place(x = 250, y = 685)
# digit 0
photo_0 = ImageTk.PhotoImage(Image.open('0.jpg'))
button_0 = Button(root, image = photo_0, bd = 0, relief = FLAT, command=lambda : add_digit(0)).place(x = 320, y = 685)

photo_none1 = ImageTk.PhotoImage(Image.open('none.jpg'))
button_none1 = Button(root, image = photo_none1, bd = 0, relief = FLAT).place(x = 390, y = 685)

photo_cancel = ImageTk.PhotoImage(Image.open('cancel.jpg'))
button_cancel = Button(root, image = photo_cancel, bd = 0, relief = FLAT, command = delete_digit).place(x = 490, y = 520)

photo_clear = ImageTk.PhotoImage(Image.open('clear.jpg'))
button_clear = Button(root, image = photo_clear, bd = 0, relief = FLAT, command = clear_digit).place(x = 490, y = 575)

photo_enter = ImageTk.PhotoImage(Image.open('enter.jpg'))
button_enter = Button(root, image = photo_enter, bd = 0, relief = FLAT, command = enter).place(x = 490, y = 630)

photo_none2 = ImageTk.PhotoImage(Image.open('none2.jpg'))
button_none2 = Button(root, image = photo_none2, bd = 0, relief = FLAT).place(x = 490, y = 685)

def put_card():
    '''
    :return: insert a bank card
    '''
    global option_card
    global b_one
    global b_two
    global b_three
    global b_four
    global b_five
    global b_six
    global entry
    global option_pin_code
    global option_get_money
    global option_give_money
    global number_of_attempts
    global attempts_to_enter
    if option_card == False:
        number_of_attempts = 2
        animation_give_card()
        option_pin_code = True
        option_get_money = False
        option_give_money = False
        Label(root, image=photo_pin).place(x=115, y=190)
        Label(root, text= 'Осталось попыток:', bg = 'white').place(x=220, y= 300)
        attempts_to_enter = Label(root, text= str(number_of_attempts), bg='white') #
        attempts_to_enter.place(x=335, y=300)
        entry = Entry(root, text='', width=10, font = ('SchoolBook', 40), show ='*')
        entry.place(x=220, y=330)

# button to insert the card
photo_put_card = ImageTk.PhotoImage(Image.open('card.jpg'))
button_put_card = Button(root, image = photo_put_card, bd = 0, relief = RAISED, command = put_card).place(x = 930, y = 510)

photo_main = ImageTk.PhotoImage(Image.open('main.jpg'))              # main screen
main = Label(root, image = photo_main, bd = 0).place(x=115, y = 190)
photo_pin = ImageTk.PhotoImage(Image.open('pin.jpg'))                # PIN code entry window
photo_menu = ImageTk.PhotoImage(Image.open('menu.jpg'))              # main menu
photo_get_money = ImageTk.PhotoImage(Image.open('get_money.jpg'))    # money dispensing window
photo_give_money = ImageTk.PhotoImage(Image.open('give_money.jpg'))  # money-giving window
photo_balance = ImageTk.PhotoImage(Image.open('balance.jpg'))        # window for viewing card balance
photo_cabinet = ImageTk.PhotoImage(Image.open('cabinet.jpg'))        # personal account window

def open_menu():
    '''
    :return: open the main menu
    '''
    global option_card
    global b_one
    global b_two
    global b_three
    global b_four
    global b_five
    global b_six
    if option_card == True:
        Label(root, image=photo_menu, bd=0).place(x=115, y=190)
        b_one = True
        b_two = True
        b_three = True
        b_four = True
        b_five = True
        b_six = True

def open_main():
    '''
    :return: open home screen
    '''
    global option_card
    global b_five
    if b_five == True:
        animation_get_card()
        option_card = False
        Label(root, image=photo_main, bd=0).place(x=115, y=190)


def open_get_money():
    '''
    :return: withdrawal operation
    '''
    global option_card
    global b_one
    global b_two
    global b_three
    global b_four
    global b_five
    global b_six
    global option_get_money
    global option_pin_code
    global option_give_money
    global entry
    global balance
    if option_card == True and b_one == True:
        option_get_money = True
        option_pin_code = False
        option_give_money = False
        Label(root, image=photo_get_money, bd=0).place(x=115, y=190)
        entry = Entry(root, text='', width=10, font=('SchoolBook', 40)) #
        entry.place(x=300, y=350)
        Label(root, text='Введите желаемую сумму и нажмите Enter', bg='white', font=40).place(x=300, y=280)


def open_give_money():
    '''
    :return: to put money into the account
    '''
    global option_card
    global b_one
    global b_two
    global b_three
    global b_four
    global b_five
    global b_six
    global option_get_money
    global option_give_money
    global option_pin_code
    global entry
    global balance
    global animation_money
    if option_card == True and b_two == True:
        animation_money = True
        option_get_money = False
        option_pin_code = False
        option_give_money = True
        Label(root, image=photo_get_money, bd=0).place(x=115, y=190)
        entry = Entry(root, text='', width=10, font = ('SchoolBook', 40))
        entry.place(x=300, y=350)
        Label(root, text='Введите сумму от 100 до 50000 и нажмите Enter', bg='white', font=40).place(x=300, y=280)

def open_balance():
    '''
    :return: view card balance
    '''
    global option_card
    global b_one
    global b_two
    global b_three
    global b_four
    global b_five
    global b_six
    global balance
    if option_card == True and b_three == True:
        Label(root, image=photo_balance, bd=0).place(x=115, y=190)
        Label(root, text = balance, bg = 'white', font = ('SchoolBook', 40)).place(x=300, y=300)
        b_one = False
        b_two = False
        b_four = False
        b_five = False

def open_cabinet():
    '''
    :return: go to your personal account
    '''
    global option_card
    global b_one
    global b_two
    global b_three
    global b_four
    global b_five
    global b_six
    if option_card == True and b_four == True:
        Label(root, image=photo_cabinet, bd=0).place(x=115, y=190)
        b_one = False
        b_two = False
        b_three = False
        b_five = False

# button around the screen
button_one = Button(root, image = photo_none2, bd = 2, relief = RAISED, command = open_get_money).place(x = 30, y = 275)
button_two = Button(root, image = photo_none2, bd = 2, relief = RAISED, command = open_give_money).place(x = 30, y = 355)
button_three = Button(root, image = photo_none2, bd = 2, relief = RAISED, command = open_balance).place(x = 30, y = 430)
button_four = Button(root, image = photo_none2, bd = 2, relief = RAISED, command = open_cabinet).place(x = 770, y = 275)
button_five = Button(root, image = photo_none2, bd = 2, relief = RAISED, command = open_main).place(x = 770, y = 355)
button_six = Button(root, image = photo_none2, bd = 2, relief = RAISED, command = open_menu).place(x = 770, y = 430)

bank.mainloop()