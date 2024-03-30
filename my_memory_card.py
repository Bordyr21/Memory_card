from random import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel, QButtonGroup)

from random import shuffle


app = QApplication([])

window = QWidget()

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')


RadioGroupBox = QGroupBox("Варианты ответов")


rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)


RadioGroupBox.setLayout(layout_ans1)


# Создаем панель результата
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel('ответ будет тут!') # здесь будет написан текст правильного ответа


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)


# Размещаем все виджеты в окне:
layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"


layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
# Размещаем в одной строке обе панели, одна из них будет скрываться, другая показываться:
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
RadioGroupBox.hide() # эту панель мы уже видели, скроем, посмотрим, как получилась панель с ответом


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)


# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым

right_answer = rbtn_1
wrong1 = rbtn_2
wrong2 = rbtn_3
wrong3 = rbtn_4
question = lb_Question
right_answer = lb_Correct

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(
    Question('Государственный язык бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Русский'))
questions_list.append(
    Question('Какого цвета нет в флаге России?', 'Зелёный', 'Красный', 'Синий', 'Белый'))
questions_list.append(
    Question('Влад?', "Возможно частично", "Да", "Нет", "Скорее да чем нет"))
questions_list.append(
    Question("Внешний долг США на момент 4 октября 2022 года", "31,12 триллиов", "12900 рублей", "48,6 миллиардов", "18,9 миллионов"))
questions_list.append(
    Question("Скорость света", "≈300.000.000 м/с", "13 км/ч", "140.765.823 м/с", "Почти как у скрости звука"))
questions_list.append(
    Question("Самый высокий человек в мире", "Султан Кесен(8.2 Фута)", "Олег(183 см)", "Усейн Болт(44,72 км/ч)", "Данил Гангнамстайл(42 см)"))
questions_list.append(
    Question("88 + 22", "110", "100", "14.940.764 млн", "-5,4"))
questions_list.append(
    Question("Государственный язык Нигерии", "Английский", "Нидерландский", "Испанский", "Русский"))
questions_list.append(
    Question("Самый старый человек в мире", "Мария Браньяс Морера", "Жданов Дмитрий", "Олег", "Сосед Данила Гангнамстайл"))
questions_list.append(
    Question("Сколько серий в смешариках?", "320", "143", "7", "98.657.345"))

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_qestion():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def test():
    if btn_OK.text() == 'Ответить':
        show_result()
    else:
        show_qestion()

answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_qestion()

def show_correct(res):
    lb_Result.setText(res)
    show_result()


def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
    else:
        #if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неверно!')



def next_question():
    window.total += 1
    score = window.score / window.total
    score1 = score * 100
    print("Статистика")
    print("-Всего вопросов:", window.total)
    print("-Правильных ответов:", window.score)
    print("Рейтинг:", score1)
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Следующий вопрос':
        next_question()
    else:
        check_answer()


window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
window.show()

btn_OK.clicked.connect(click_OK)
window.total = 0
window.score = 0
next_question()

window.resize(400, 300)
app.exec()
