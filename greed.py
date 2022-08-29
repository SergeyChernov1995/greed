# -*- encoding: utf-8 -*-
# ----------------------------------------------------------------------------
# Greed
# Copyright © 2020-2022 Sergey Chernov aka Gamer
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# ----------------------------------------------------------------------------

import codecs
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import time
from datetime import datetime
from pyrecord import Record
from threading import Timer
from random import randint
from random import randrange
from random import choice
from operator import itemgetter, attrgetter, methodcaller
from PIL import Image, ImageTk
from enum import Enum
from tkinter import simpledialog
import pygame
#from test_canvas import holst

class h(Enum):
    unpicked = 1
    picked = 2
    rejected = 3
    changed = 4
    proverka = 5
    correct = 6

class term(Enum):
    default = 0
    random_pick = 1
    ready = 2
    pressed = 3
    after = 4

class _567 (Enum):
    priem = 0
    zamena1 = 1
    zamena2 = 2
    proverka = 3
    joker = 4


stage567 = _567.joker
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

root = tk.Tk()
root.geometry ("1000x650") #800x550
root.title ("Greed")
root.resizable(width=False, height=False)
freebie = True
root.term_state = term.default
global Terminator_Question


TermQ = []

qterm = codecs.open('qbaset.txt', 'r', "utf_8_sig")  # stage+1
for line in qterm:
    x = {}

    HUH = line.rstrip("\n")
    x["Q"] = HUH
    x["A"] = list(map(str, qterm.readline().split()))
    test = []

    TermQ.append(x)

qterm.close()
joker = Image.open("Objects/cardJoker.png")
joker.thumbnail((50, 50), Image.ANTIALIAS)
joker_image = ImageTk.PhotoImage(joker)
pytaniaterm = TermQ.copy()
index_term = randint(0, len(pytaniaterm)-1)

OTBOR_X = 0.35
OTBOR_Y = 0.05
active_qual = 0  # type: int
active_term = 0
active_567 = 0
yellow = "#ff9f00"
qual_res = Record.create_type("qual_res", "Name", "Otvet", "Vremya", "Distance", Otvet = 0, Vremya = 0)
#Igroki = Record.create_type("Igroki", "Name", "Share", "Sgor", "Nesgor", Share=1, Sgor=0, Nesgor=0)
Players = []
XYZ = []
P = {}
IgrokiDummy = []
ImenaIgrokov = []
images = []
nuotraukos = []
dadc = []
eax = []
aux = {}
Qual_Field = False # false - ответ не начали вводить, true - ответ начали вводить
# for i in range (6):
#     IgrokiDummy = qual_res (Name = "Игрок №"+str(i+1), Otvet = 0, Vremya = 0, Distance = 0)
#     Players.append(IgrokiDummy)
Record_voprosy = Record.create_type("Record", "Question", "Answer")
base_otbor = []
index_voprosa = 0
counter = 0
money = [0, 25000, 50000, 75000, 100000, 250000, 500000, 1000000, 2000000]
varnumb = [4, 4, 5, 5, 6, 7, 8, 9]
term_pinigai = 25000
stage = 0  # номер вопроса (0)
varcorr = [1, 1, 1, 1, 4, 4, 4, 4]
question_greed = {}
#Klausimai = []
pytania = []
knopki = []
aceptadas = []
state = h.unpicked
picked = None
schetchik = 0
player_term = [None, None]
skem_knopka = []
skem_knopka2 = []
buzzer = []
buzzer2 = []
kto_nazhal = None
revealed = []
freebied = None
nextanswer = []
nextanswer2 = []
freebie = True
freebied = False
variants = set ()
golosoval = []
ku = 0
_otvet8 = 0
qualifying_round_stands = []
qualifying_showans = []
label_w_names = []
result = None
canvas = tk.Canvas(root, width=600, height=300, bg='#cfcfcf')
hravci = tk.Canvas(root, width=380, height=280, bg='#cfcfcf')
mistsya_hravciv =  []


def read_term():
    pass

def bribe(i):
    a = len(IgrokiDummy)
    for b in range (a):
        IgrokiDummy[b]["Sgor"] = ((money[stage + 1]) // 10) // a
        eax[b]["text"] = str(IgrokiDummy[b]["Sgor"] + IgrokiDummy[b]["Nesgor"])

def proverka_random(vernost):
    global edro, variants_backup
    edro = len(knopki) - 1
    if (vernost == False):
        while True:
            edro = choice(list(variants))
            if (revealed[edro - 1] == False) and (not (edro in root.pytania[index_voprosa]["C"])):
                break
        revealed[edro - 1] = True
        edro -=1
        tkinter.messagebox.showinfo(root.pytania[index_voprosa]["A"][edro].strip('\n'), "Правильный ли это ответ?")
        pygame.mixer.music.load("sounds/greed_incorrect.mp3")
        pygame.mixer.music.play(0)
        log.write(root.pytania[index_voprosa]["A"][edro]+' - неверный'+'\n')
        root.knopki[edro]["bg"] = "#cf0000"
        global vernich
        if (vernich <3):
            tkinter.messagebox.showinfo("Ответ неверный", "Покажите нам верные ответы!")
            log.write('Недостающие верные ответы - ')
        elif (vernich == 3):
            tkinter.messagebox.showinfo("Ответ неверный", "Покажите нам верный ответ!")
            log.write('Недостающий верный ответ - ')
        correct_after_fail = pygame.mixer.Sound("sounds/greed_correct_after_fail.wav")
        correct_after_fail.play()
        for o in range (len(root.pytania[index_voprosa]["A"])):
            revealed[o] = True
            if (o+1 in root.pytania[index_voprosa]["C"]):
                root.knopki[o]["bg"] = "#ff9f00"
            elif (aceptadas[o]):
                root.knopki[o]["bg"] = "#cf0000"
        q = list((set(root.pytania[index_voprosa]["C"]) - variants_backup))
        n = []
        for w in q:
            n.append(root.pytania[index_voprosa]["A"][w-1])
        log.write((", ".join(n))+'\n')

    else:
        while True:
            edro = choice(list(variants))
            if (revealed[edro - 1] == False) and (edro in root.pytania[index_voprosa]["C"]):
                break
        revealed[edro - 1] = True
        edro -= 1
        tkinter.messagebox.showinfo(root.pytania[index_voprosa]["A"][edro].strip('\n'), "Правильный ли это ответ?")
        root.knopki[edro]["bg"] = "#ff9f00"
        log.write(root.pytania[index_voprosa]["A"][edro]+' - верный'+'\n')
        variants.remove(edro + 1)


def who_answers(kto):
    global active_567
    active_567 = kto
    golosoval[kto] = False
    for op in range(len(nextanswer2)):
        nextanswer2[op].pack_forget()
    light_player(active_567)
    tk.messagebox.showinfo(' ', IgrokiDummy[active_567]["Name"] + ', отвечайте')
    choose.grab_release()
    choose.withdraw()


def noway():
    tkinter.messagebox.showinfo("Окно закрыть пока нельзя")



def noway2():
    tkinter.messagebox.showinfo("Не закрывайте это окно")

def accepted_in_terminator(*args):
    global termotvet
    otvet = str(termotvet.get())
    log.write ("Игрок даёт ответ "+otvet+'\n')
    a = otvet.replace(" ", "")
    b = a.lower()
    if (b == pytaniaterm[index_term]["A"][0]):
        tkinter.messagebox.showinfo("Верно!", "Поздравляю, ответ правильный!" )
        log.write("Это верный ответ"+'\n')
    elif (b in pytaniaterm[index_term]["A"]):
        tkinter.messagebox.showinfo("Верно!", "Правильный ответ - "+pytaniaterm[index_term]["A"][0])
        log.write("Это верный ответ ("+pytaniaterm[index_term]["A"][0]+')'+'\n')
    else:
        tkinter.messagebox.showinfo("Неверно!", "Ошибка! Правильный ответ - "+pytaniaterm[index_term]["A"][0])
        log.write("Это неверный ответ. Правильный ответ - " + pytaniaterm[index_term]["A"][0]+'\n')
    if ((root.kto_nazhal == 0) and (b in pytaniaterm[index_term]["A"])) or ((root.kto_nazhal ==1) and not(b in pytaniaterm[index_term]["A"])):
        winner = player_term[0]
        loser = player_term[1]
    elif ((root.kto_nazhal == 1) and (b in pytaniaterm[index_term]["A"])) or ((root.kto_nazhal ==0) and not(b in pytaniaterm[index_term]["A"])):
        winner = player_term[1]
        loser = player_term[0]
    pygame.mixer.music.load("sounds/greed_cue.mp3")
    pygame.mixer.music.play(0)
    IgrokiDummy[winner]["Sgor"], IgrokiDummy[loser]["Sgor"] = (IgrokiDummy[winner]["Sgor"]+IgrokiDummy[loser]["Sgor"]), 0
    IgrokiDummy[winner]["Share"], IgrokiDummy[loser]["Share"] = (IgrokiDummy[winner]["Share"] + IgrokiDummy[loser]["Share"]), 0
    global stage
    current_winnings(stage)
    tkinter.messagebox.showinfo(" ", 'Выигрыш '+IgrokiDummy[loser]["Name"]+ ': '+str(IgrokiDummy[loser]["Sgor"]+IgrokiDummy[loser]["Nesgor"]))
    log.write ('Выигрыш '+IgrokiDummy[loser]["Name"]+ ': '+str(IgrokiDummy[loser]["Sgor"]+IgrokiDummy[loser]["Nesgor"])+'\n')
    if loser == 0:
        log.write(IgrokiDummy[winner]["Name"] + ' - новый капитан команды'+'\n')
        tkinter.messagebox.showinfo("Новый капитан", IgrokiDummy[winner]["Name"] + ' - новый капитан команды')
        a1, b1 = hravci.coords(label_w_names[0])
        e1, f1 = hravci.coords(label_w_names[IgrokiDummy[winner]["Occupied"]])
        hravci.coords(label_w_names[0], e1, f1)
        hravci.coords(label_w_names[IgrokiDummy[winner]["Occupied"]], a1, b1)
        label_w_names[IgrokiDummy[winner]["Occupied"]], label_w_names[0] = label_w_names[0], label_w_names[IgrokiDummy[winner]["Occupied"]]
        IgrokiDummy[0]["Occupied"], IgrokiDummy[winner]["Occupied"] = IgrokiDummy[winner]["Occupied"], IgrokiDummy[0][
            "Occupied"]
        IgrokiDummy [winner], IgrokiDummy[0] = IgrokiDummy[0], IgrokiDummy[winner]
        nuotraukos[winner]["text"], nuotraukos[0]["text"] = nuotraukos[0]["text"], nuotraukos[winner]["text"]
        eax[winner]["text"], eax[0]["text"] = eax[0]["text"], eax[winner]["text"]
        nuotraukos[winner].place_forget()
        eax[winner].place_forget()
        nuotraukos.pop(winner)
        eax.pop(winner)
        hravci.delete(label_w_names[IgrokiDummy[winner]["Occupied"]])
        IgrokiDummy.pop(winner)
    else:
        nuotraukos[loser].place_forget()
        eax[loser].place_forget()
        nuotraukos.pop(loser)
        eax.pop(loser)
        hravci.delete(label_w_names[IgrokiDummy[loser]["Occupied"]])
        IgrokiDummy.pop(loser)
    current_winnings(stage)
    # for z in range(len(IgrokiDummy)):
    #     print(str(IgrokiDummy[z]["Name"]) + ': ' + str(IgrokiDummy[z]["Sgor"] + IgrokiDummy[z]["Nesgor"]) + '(' + str(
    #         IgrokiDummy[z]["Share"]) + ')')
    Terminator_Question.place_forget()
    root.buzzer2[0]["bg"] = "#cccccc"
    root.buzzer2[1]["bg"] = "#cccccc"
    root.buzzer2[0].place_forget()
    root.buzzer2[1].place_forget()
    pytaniaterm.pop(index_term)
    root.termotvet = ''
    vvod.place_forget()
    root.term_state = term.default
    root.kto_nazhal = None
    #stage+=1
    read_12345678(stage)

def supplement():
    root.after_cancel(root.dobav)
    if (golosoval[0] is True) and (len(variants)<4):
        global choose
        choose = tk.Toplevel(root)
        choose.protocol('WM_DELETE_WINDOW', noway2)
        choose.title ("Выберите, кто даст следующий ответ")
        root.title("Кто даст следующий ответ?")
        global nextanswer
        nextanswer = []
        for a in range(len(IgrokiDummy)):
            pl = tk.Button(choose, text=IgrokiDummy[a]["Name"], command=lambda ko=a: who_answers(ko))
            nextanswer.append(pl)
        global nextanswer2
        nextanswer2 = nextanswer.copy()
        for btn in range(len(nextanswer2)):
            nextanswer2[btn].pack(side=tk.LEFT)
        choose.grab_set()


def accept():
    global ku
    global active_567
    global stage567
    global variants
    if (ku == 0):
        ku = 1
    if (stage < 7):
        if (active_567>0) and ((len(variants))<4):
            active_567 -=1
            light_player(active_567)
            if (ku!=0):
                if (len(variants) < 4) and (active_567 > 0):
                    tk.messagebox.showinfo(' ', IgrokiDummy[active_567]["Name"] + ', отвечайте')
                elif (active_567 == 0) and (golosoval[0] == False):
                    tk.messagebox.showinfo(' ', IgrokiDummy[active_567]["Name"] + ', отвечайте')
                else:
                    pass
                root.after_cancel(root._5to1)
                stage567 = _567.priem
        if (golosoval[0] is True) and (len(variants) < 4):
            root.dobav = root.after(1000, supplement)
    elif (stage == 7):
        active_567 = 0
        root.after_cancel(root._5to1)
        stage567 = _567.priem
        global _otvet8
        if (_otvet8 == 0):
            tk.messagebox.showinfo(' ', IgrokiDummy[active_567]["Name"] + ', отвечайте')
            _otvet8 = 1
        else:
            pass




def current_winnings(f):
    sharez = 0
    for s in range (len(IgrokiDummy)):
        sharez += IgrokiDummy[s]["Share"]
    for s in range (len(IgrokiDummy)):
        IgrokiDummy[s]["Sgor"]= money[f]*IgrokiDummy[s]["Share"]//sharez
        #print(str(s)+': '+str(IgrokiDummy[s]["Sgor"]+IgrokiDummy[s]["Nesgor"]))
        eax[s]["text"] = str(IgrokiDummy[s]["Sgor"]+IgrokiDummy[s]["Nesgor"])
    #for z in range(len(IgrokiDummy)):
        #print(str(IgrokiDummy[z]["Name"]) + ': ' + str(IgrokiDummy[z]["Sgor"] + IgrokiDummy[z]["Nesgor"]) + '(' + str(
            #IgrokiDummy[z]["Share"]) + ')')
    for s in range (len(IgrokiDummy)):
         nuotraukos[s].place_forget()
         eax[s].place_forget()
    for a in range (len(IgrokiDummy)):
        nuotraukos[a].place(x=15, y=5 + 55 * a)
        eax[a].place(x=79, y=5 + 55 * a)




def onKeyPress(event):
    if not (root.term_state == term.ready):
        pass
    elif not (event.char in set ('AaLlфФдД')):
         pass
    else:
        if (event.char in set('AaфФ')):
            root.buzzer2[0]["bg"]="#ff0000"
            root.kto_nazhal = 0
        elif (event.char in set('LlдД')):
            root.buzzer2[1]["bg"]="#ff0000"
            root.kto_nazhal = 1
        button_pressed = pygame.mixer.Sound("sounds/greed_gong.wav")
        button_pressed.play()
        log.write('Кнопку нажимает '+IgrokiDummy[player_term[root.kto_nazhal]]["Name"]+'\n')
        root.term_state = term.pressed
        vvod.place(relx=0.5, rely = 0.5)
        vvod.focus_set()
        #print('Got key press: ', event.char)


def terminator(auz):
    player_term[1] = auz
    for a in range(5):
        if (IgrokiDummy[auz]["Occupied"]==a):
            hravci.itemconfig(mistsya_hravciv[a], fill="#ffffff")
    for op in range(len(skem_knopka2)):
        skem_knopka2[op].pack_forget()
    for a in range(2):
        b = tk.Label(text = IgrokiDummy[player_term[a]]["Name"])
        buzzer.append(b)
    root.buzzer2 = buzzer.copy()
    for a in range(2):
        root.buzzer2[a].place(relx = 0.4+0.3*a, rely = 0.3)
        root.buzzer2[a]["bg"]="#cccccc"
        root.buzzer2[a]["text"]= IgrokiDummy[player_term[a]]["Name"]
    tk.messagebox.showinfo("Готовность номер 1", IgrokiDummy[player_term[0]]["Name"]+', '+IgrokiDummy[player_term[1]]["Name"]+', прошу вас в зону Терминатора!')
    light_player(-1)
    hravci.place_forget()
    global Terminator_Question
    Terminator_Question = tk.Label(text =pytaniaterm[index_term]["Q"] )
    #global Terminator_Question
    Terminator_Question.place(relx=0.1, rely=0.85)
    skem.grab_release()
    skem.withdraw()
    log.write(IgrokiDummy[player_term[0]]["Name"]+ ' выбирает в соперники ' + IgrokiDummy[player_term[1]]["Name"]+'\n')
    log.write("Вопрос терминатора: "+pytaniaterm[index_term]["Q"]+'\n')
    root.term_state = term.ready



def term_choose():
    root.after_cancel(term_choose)
    global schetchik
    schetchik = schetchik-1
    global active_term, index_term
    active_term = randrange (len(IgrokiDummy))
    root.title (IgrokiDummy[active_term]["Name"])
    svet_term(active_term)
    if (schetchik == 0):
        pygame.mixer.music.load("sounds/greed_terminator_inter.mp3")
        pygame.mixer.music.play(-1)
        log.write('Терминатор выбрал '+IgrokiDummy[active_term]["Name"]+'\n')
        if tkinter.messagebox.askyesno(IgrokiDummy[active_term]["Name"], 'будете ли вы играть в терминатор?'):
            player_term[0] = active_term
            IgrokiDummy[active_term]["Nesgor"] += term_pinigai
            eax[active_term]["text"] = str(IgrokiDummy[active_term]["Sgor"]+IgrokiDummy[active_term]["Nesgor"])
            index_term = randint(0, len(pytaniaterm)-1)
            root.title (IgrokiDummy[active_term]["Name"]+ ', с кем вы будете играть?')
            global skem
            skem = tk.Toplevel(root)
            skem.protocol('WM_DELETE_WINDOW', noway)
            for a in range (len(IgrokiDummy)):
                if (a!=player_term[0]):
                    bar = tk.Button (skem, text = IgrokiDummy[a]["Name"], command = lambda ko = a: terminator(ko))
                    skem_knopka.append(bar)
            global skem_knopka2
            skem_knopka2 = skem_knopka.copy()
            for a in range (len(skem_knopka2)):
                skem_knopka2[a].pack(side=tk.LEFT)
            skem.grab_set()
        else:
            light_player(-1)
            pygame.mixer.music.load("sounds/greed_cue.mp3")
            pygame.mixer.music.play(0)
            log.write('Игрок отказывается играть в терминатор'+'\n')
            tk.messagebox.showinfo("Отказ", "Игрок отказывается играть в Терминатор, и мы продолжаем игру в полном составе")
            hravci.place_forget()
            global stage
            #stage += 1
            read_12345678(stage)
            pass
    else:
        root.termtimer = root.after(400, term_choose)

def check_5678():
    root.after_cancel(root.prov)
    global edro
    bailout = None
    edro = len(root.knopki) - 1
    if (vernich == 0):
        proverka_random(False)
        current_winnings(0)
        endgame()
    elif (vernich < 3):
        for p in range(vernich):
            proverka_random(True)
            correct = pygame.mixer.Sound("sounds/greed_correct.wav")
            correct.play()
        proverka_random(False)
        current_winnings(0)
        endgame()
    elif (vernich == 3) or (vernich == 4):
        for p in range(3):
            proverka_random(True)
            correct = pygame.mixer.Sound("sounds/greed_correct.wav")
            correct.play()
        if (stage < 7):
            if tkinter.messagebox.askyesno("Взятка", "Вы можете поделить " + str(
                    (money[stage + 1]) // 10) + ' и покинуть игру.' + '\n' + IgrokiDummy[0][
                                                         "Name"] + ', вы принимаете это предложение?'):
                bribe(stage + 1)
                # для отладки
                #for k in range(len(IgrokiDummy)):
                    #print(IgrokiDummy[k]["Name"] + ": " + str(IgrokiDummy[k]["Sgor"] + IgrokiDummy[k]["Nesgor"]))
                    # конец отладочной инфы
                bailout = True
                log.write(IgrokiDummy[0]["Name"]+ ' соглашается на взятку - '+str(((money[stage + 1]) // 10) )+'\n')
                tkinter.messagebox.showinfo("Вы взяли взятку", "Но был ли верным четвёртый ответ?")
            else:
                bailout = False
                tkinter.messagebox.showinfo("Вы отказались от взятки", "Проверяем четвёртый ответ")  # dopisat'
            pygame.mixer.music.stop()
            if (vernich == 3):
                proverka_random(False)
                if (bailout == True):
                    tkinter.messagebox.showinfo("Браво!", "Вы вовремя остановились!")
                else:
                    pass
                    current_winnings(0)
                endgame()
            elif (vernich == 4):
                proverka_random(True)
                if (bailout == False):
                    pygame.mixer.music.load("sounds/greed_correct_full.mp3")
                    pygame.mixer.music.play(0)
                    tkinter.messagebox.showinfo("Браво!", "Вы успешно завершили этот раунд")
                    right()
                else:
                    correct = pygame.mixer.Sound("sounds/greed_correct.wav")
                    correct.play()
                    tkinter.messagebox.showinfo("Жаль...", "Вы напрасно остановились!")
                    endgame()
        elif (stage == 7):
            tkinter.messagebox.showinfo("На 8 вопросе не дают взятку", "Проверяем четвёртый ответ")
            if (vernich == 3):
                proverka_random(False)
                current_winnings(0)
                endgame()
            elif (vernich == 4):
                proverka_random(True)
                pygame.mixer.music.load("sounds/greed_correct_full.mp3")
                pygame.mixer.music.play(0)
                tkinter.messagebox.showinfo("Поздравляем", "Вы успешно прошли игру!")
                right()
                endgame()

def right():
    global stage, nuotraukos, eax, ko, f
    current_winnings(stage+1)
    if (stage<=3):
        root.knopki[root.picked]["bg"] = "#ff9f00"
        pygame.mixer.music.load("sounds/greed_correct_full.mp3")
        pygame.mixer.music.play(0)
        tkinter.messagebox.showinfo("Верно!", "Поздравляю, ответ правильный!" )
        root.picked = None
        log.write('Это правильный ответ ' + "\n")
    t_v_otbor.place_forget()
    for b in range (varnumb[stage]):
        aceptadas[b] = False
        root.knopki[b]["bg"] = "#00007f"
        root.knopki[b].place_forget()
        root.otbor_corr_field.place_forget()
    if (0<=stage <=5):
        if tkinter.messagebox.askyesno("Капитан", IgrokiDummy[0]["Name"]+', '+"будете ли вы играть дальше?"):
            stage +=1
            light_player(-1)
            if ( 0 <= stage <=3):
                read_12345678(stage)
            elif stage <7:
                pygame.mixer.music.load("sounds/greed_terminator_intro.mp3")
                pygame.mixer.music.play(-1)
                global schetchik
                schetchik = randint(10, 20)
                svet_term(-1)
                tkinter.messagebox.showinfo('Терминатор', 'Играем в терминатор!')
                root.termtimer = root.after(400, term_choose)
                pass #to be rectified
            else:
                pass #to be rectified

        else:
            log.write('Капитан останавливает игру.'+"\n")
            endgame()
    elif (stage==6):
        notgoing = []
        x, y = hravci.coords(label_w_names[0])
        for decision in range (len(IgrokiDummy)):
            if tkinter.messagebox.askyesno ("Восьмой вопрос", IgrokiDummy[decision]["Name"]+', пойдёте ли на восьмой вопрос?'):
                pass
            else:
                #IgrokiDummy[decision]["Share"] = 0
                log.write(IgrokiDummy[decision]["Name"]+" покидает игру с выигрышем "+str(IgrokiDummy[decision]["Sgor"]+IgrokiDummy[decision]["Nesgor"])+'\n')
                notgoing.append(decision)
                hravci.delete(label_w_names[IgrokiDummy[decision]["Occupied"]])
        if (len(IgrokiDummy) == len(notgoing)):
            tkinter.messagebox.showinfo("Игра окончена", "Все игроки забрали деньги")
            log.write("Игра окончена"+'\n')
        else:
            for s in range(len(nuotraukos)):
                nuotraukos[s].place_forget()
                eax[s].place_forget()
            IgrokiDummy[:] = [x for i, x in enumerate(IgrokiDummy) if i not in notgoing]
            nuotraukos[:] = [x for i, x in enumerate(nuotraukos) if i not in notgoing]
            eax[:] = [x for i, x in enumerate(eax) if i not in notgoing]
            for a in range(len(IgrokiDummy)):
                nuotraukos[a].place(x=15, y=5 + 55 * a)
                eax[a].place(x=79, y=5 + 55 * a)
            if (0 in notgoing):
                ko = Image.open("Objects/target_colored.png")
                ko.thumbnail((20, 20), Image.ANTIALIAS)
                f = ImageTk.PhotoImage(ko)
                nuotraukos[0].configure(image=f)
                _a, _b = hravci.coords(label_w_names[IgrokiDummy[0]["Occupied"]])
                hravci.coords(label_w_names[0], _a, _b)
                hravci.coords(label_w_names[IgrokiDummy[0]["Occupied"]], x, y) #mozhet i ne nado
                IgrokiDummy[0]["Occupied"]=0
            if (len(IgrokiDummy) >= 2) and (0 in notgoing):
                log.write(IgrokiDummy[0]["Name"] + ' - новый капитан команды' + '\n')
                tkinter.messagebox.showinfo("Новый капитан", IgrokiDummy[0]["Name"] + ' - новый капитан команды')
            # if (0 in notgoing):
            #     hello = []
            #     for b in range(len(IgrokiDummy)):
            #         if (b == 0):
            #             ko = Image.open("Objects/target_colored.png")
            #         else:
            #             ko = Image.open("Objects/target_back.png")
            #         ko.thumbnail((20, 20), Image.ANTIALIAS)
            #         f = ImageTk.PhotoImage(ko)
            #         hello.append(f)
            #     nuotraukos = []
            #     eax = []
            #     for a in range(len(IgrokiDummy)):
            #         test = tk.Label(Igroki, compound=tk.BOTTOM, text=IgrokiDummy[a]["Name"], image=hello[a])
            #         # dadc.append(str(2520 // (a + 1)))
            #         eax.append(tk.Label(Igroki, text=str(IgrokiDummy[a]["Sgor"] + IgrokiDummy[a]["Nesgor"])))
            #         nuotraukos.append(test)
            #         nuotraukos[a].place(x=15, y=5 + 55 * a)
            #         eax[a].place(x=79, y=5 + 55 * a)
            #
            # дальше, похоже, идёт ошибка
            stage +=1
            read_12345678(stage)




def check():
    root.after_cancel(root.check)
    root.state = h.proverka
    tkinter.messagebox.showinfo("Проверка", "Правильный ли ответ "+root.pytania[index_voprosa]["A"][root.picked]+'?')
    if((root.pytania[index_voprosa]["C"][0]) == root.picked+1):
        right()
    else:
        root.knopki[root.picked]["bg"] = "#cf0000"
        current_winnings(0)
        pygame.mixer.music.load("sounds/greed_incorrect.mp3")
        pygame.mixer.music.play(0)
        tkinter.messagebox.showinfo("Ошибка", "Это неправильный ответ. Какой ответ правильный?")
        pygame.mixer.music.stop()
        root.knopki[root.pytania[index_voprosa]["C"][0]-1]["bg"] = "#ff9f00"
        correct_after_fail = pygame.mixer.Sound("sounds/greed_correct_after_fail.wav")
        correct_after_fail.play()
        log.write('Это неправильный ответ ' + "\n")
        log.write("Правильный ответ - "+root.pytania[index_voprosa]["A"][root.pytania[index_voprosa]["C"][0]-1])
        endgame()


def endgame():
    log.write ("Выигрыши: "+'\n')
    for k in range (len(IgrokiDummy)):
        log.write(IgrokiDummy[k]["Name"]+ ": "+ str (IgrokiDummy[k]["Sgor"]+IgrokiDummy[k]["Nesgor"])+'\n')


def num_of_corr():
    right = set(root.pytania[index_voprosa]["C"])
    global vernich
    vernich = len(variants & right)
    #print("Верных ответов: "+str(vernich))
    log.write('Проверка ответов: '+'\n')
    global variants_backup
    variants_backup = variants.copy()
    root.prov = root.after (1000, check_5678)




def callback(j):
    global stage
    if ( 0 <= stage <=3 ):
        if (root.state == h.unpicked):
            aceptadas[j]=True
            root.knopki[j]["bg"] = "#00ffff"
            root.state = h.picked
            root.picked = j
            choosing_answer = pygame.mixer.Sound("sounds/greed_choosing_answer.wav")
            choosing_answer.play()
            log.write(IgrokiDummy[4-stage]["Name"] + "  даёт ответ " + root.pytania[index_voprosa]["A"][root.picked] + "\n" )
            root.title (IgrokiDummy[0]["Name"]+', '+"вы согласны с этим ответом?")
            if tkinter.messagebox.askyesno("Капитан", IgrokiDummy[0]["Name"]+', '+"вы согласны с этим ответом?"):
                root.check = root.after(50, check)
                #state = h.proverka
            else:
                remove_answer=pygame.mixer.Sound("sounds/greed_remove_answer.wav")
                remove_answer.play()
                root.picked = None
                log.write(IgrokiDummy[0]["Name"]+ ' убирает этот ответ'+'\n')
                for a in range(varnumb[stage]):
                    aceptadas[a] = False
                    root.knopki[a]["bg"] = "#00007f"
                root.state = h.rejected
                light_player(0)
                root.title(IgrokiDummy[0]["Name"] + ', ' + "какой ответ вы считаете правильным?")
                # root.destroy()
        elif root.state == h.rejected:
            aceptadas[j] = True
            root.knopki[j]["bg"] = "#00ffff"
            root.picked = j
            log.write('Капитан ставит ответ ' + root.pytania[index_voprosa]["A"][root.picked] + "\n" )
            choosing_answer = pygame.mixer.Sound("sounds/greed_choosing_answer.wav")
            choosing_answer.play()
            root.check = root.after(50, check)
            # to be rectified

            #дописать
            #to be rectified
    else:
        global active_567
        global stage567
        if (stage567 == _567.priem):
            if (aceptadas[j]) or ((freebied == True) and (root.pytania[index_voprosa]["J"][0] == j + 1)) or (
                    (stage < 7) and (golosoval[active_567])):
                pass
            else:
                aceptadas[j] = True
                variants.add(j + 1)
                root.knopki[j]["bg"] = "#00ffff"
                choosing_answer = pygame.mixer.Sound("sounds/greed_choosing_answer.wav")
                choosing_answer.play()
                golosoval[active_567] = True
                log.write(IgrokiDummy[active_567]["Name"] +' - '+root.pytania[index_voprosa]["A"][j] + "\n" )
                # print (str(active_567))
                root._5to1 = root.after(1000, accept)
                if (len(variants) == 4) and (stage < 7):
                    if tkinter.messagebox.askyesno("Замена", "Будете менять один из ответов?"):
                        light_player(0)
                        stage567 = _567.zamena1
                    else:
                        light_player(-1)
                        stage567 = _567.proverka
                        num_of_corr()
                elif (len(variants) == 4) and (stage == 7):
                    stage567 = _567.proverka
                    num_of_corr()
                    # дописать
        elif (stage567 == _567.zamena1) and (aceptadas[j]):
            remove_answer = pygame.mixer.Sound("sounds/greed_remove_answer.wav")
            remove_answer.play()
            log.write(IgrokiDummy[0]["Name"] + ' убирает вариант ' + root.pytania[index_voprosa]["A"][j] + "\n" )
            variants.remove(j + 1)
            aceptadas[j] = False
            root.knopki[j]["bg"] = "#00007f"
            root.title("Поставьте свой ответ")
            stage567 = _567.zamena2
        elif (stage567 == _567.zamena2) and (aceptadas[j] == False) and not (
                (freebied == True) and (root.pytania[index_voprosa]["J"][0] == j + 1)):
            choosing_answer = pygame.mixer.Sound("sounds/greed_choosing_answer.wav")
            choosing_answer.play()
            log.write(' и ставит вариант ' + root.pytania[index_voprosa]["A"][j]+'.'+'\n')
            aceptadas[j] = True
            variants.add(j + 1)
            root.knopki[j]["bg"] = "#00ffff"
            light_player(-1)
            stage567 = _567.proverka
            num_of_corr()


def read_12345678(nomer):
    global ku
    global stage567
    global aceptadas, revealed, golosoval, jlabel, variants, variants_backup
    global active_567
    root.after_cancel(vopros_show)
    Klausimai = []
    root.knopki = []
    aceptadas = []
    revealed = []
    golosoval = []
    variants = set()
    variants_backup = set()
    count = 0
    sums = codecs.open('qbase' + str(nomer + 1) + '.txt', 'r', "utf_8_sig") #stage+1
    for line in sums:
        x = {}
        # cheq2 = []
        HUHA = line.rstrip("\n")
        x["Q"] = HUHA
        x["A"] = []
        x["C"] = []
        x["J"] = []
        test = []
        # cheq.append(x)
        for a in range(varnumb[nomer]):
            foo = sums.readline()
            foo = foo.rstrip('\n')
            x["A"].append(foo)
        for a in range(varcorr[nomer]):
            foo = sums.readline()
            foo = foo.rstrip('\n')
            x["C"].append(int(foo))
        if (nomer >= 4):
            foo = sums.readline()
            foo = foo.rstrip('\n')
            x["J"].append(int(foo))
        # test.append(x)
        Klausimai.append(x)
        count += 1
        # Preguntas.question.append (HUHA)
        # Respuestas.correct.append(Respuestas)
        # Respuestas.clear()
    sums.close()
    pygame.mixer.music.load("sounds/greed_back"+str(nomer+1)+".mp3")
    pygame.mixer.music.play(-1)
    # Text = open('output.txt', 'w') #'w'
    # for a in range(len(Klausimai)):
    #     Text.write(Klausimai[a]["Q"] + "\n")
    #     for b in range(varnumb[nomer]):
    #         Text.write(Klausimai[a]["A"][b])
    #     for b in range(varcorr[nomer]):
    #         Text.write((str(Klausimai[a]["C"][b]) + '\n'))
    #     if (nomer >= 4):
    #         Text.write((str(Klausimai[a]["J"][0]) + '\n'))
    # Text.close()
    root.pytania = Klausimai.copy()
    t_v_otbor.place (relx = 0.01, rely = 0.8, width=444, height=100)
    global index_voprosa
    index_voprosa = randint(0, len(root.pytania)-1)
    vopros_otbora.set(root.pytania[index_voprosa]["Q"])
    root.otbor_corr_field.place(relx=0.1, rely=0.77, width=69, height=16)
    qual_corr.set(str(money[nomer+1]))
    log.write("Вопрос "+str(stage+1)+" ("+str(money[nomer+1])+")"+"\n")
    log.write(root.pytania[index_voprosa]["Q"] + "\n")
    for a in range (varnumb[nomer]):
        global uno
        uno = tk.Button(root, text = root.pytania[index_voprosa]["A"][a], width = 50, height=1, bg="#00007f", fg="#ffffff", command = lambda dos = a: callback(dos)) #fg="#ffffff"
        root.knopki.append(uno)
        aceptadas.append(False)
        revealed.append(False)
        golosoval.append (False)
    for a in range (varnumb[nomer]):
        root.knopki[a].place(x=510, y=10+32*a)
        log.write(str(a + 1) + ". " + root.pytania[index_voprosa]["A"][a] + "\n")
    root.state = h.unpicked
    if (nomer<=3):
        root.title (IgrokiDummy[4-stage]["Name"]+', выберите ответ')
        light_player(4-nomer)
    elif (nomer<7):
        global freebied
        freebied = False
        global active_567
        active_567 = len(IgrokiDummy)
        global freebie
        hravci.place(x=610, y=360)
        if (nomer == 4):
            jlabel = tk.Label(image=joker_image)
            jlabel.image = joker_image  # keep a reference!
            jlabel.place(relx=0.50, rely=0.77)
        if (freebie == True):
            light_player(0)
            if tkinter.messagebox.askyesno("Джокер", "Будете использовать джокер?"):
                jlabel.place_forget()
                freebie = False
                tkinter.messagebox.showinfo("Джокер", "Уберите один неверный ответ")
                root.knopki[(root.pytania[index_voprosa]["J"][0])-1]["text"] = ""
                joker_sound = pygame.mixer.Sound("sounds/greed_joker.wav")
                joker_sound.play()
                freebied = True
                log.write('Капитан использует джокер. Убирается ответ '+root.pytania[index_voprosa]["A"][root.pytania[index_voprosa]["J"][0]-1] + "\n" )
            else:
                pass
        stage567 = _567.priem
        log.write("Ответы игроков: "+'\n')
        # global _5to1 #dopisat'
        ku = 0
        root._5to1 = root.after(10, accept)
    elif (nomer == 7):
        freebied = False
        #global active_567
        if (freebie == True):
            freebie = False
            light_player(0)
            tkinter.messagebox.showinfo("У вас остался джокер", "Уберите один неверный ответ")
            joker_sound = pygame.mixer.Sound("sounds/greed_joker.wav")
            joker_sound.play()
            root.knopki[(root.pytania[index_voprosa]["J"][0]) - 1]["text"] = ""
            freebied = True
            log.write('Капитан использует джокер. Убирается ответ ' + root.pytania[index_voprosa]["A"][
                root.pytania[index_voprosa]["J"][0] - 1] + "\n")
            jlabel.place_forget()
        else:
            pass
        stage567 = _567.priem
        log.write("Ответы игроков: "+'\n')
        # global _5to1 #dopisat'
        ku = 0
        root._5to1 = root.after(10, accept)


def light_player(index):
    if (index == -1): #это потушит всё
        for a in range(5):
            hravci.itemconfig(mistsya_hravciv[a], fill="#ff9f00")
    else:
        for a in range(5):
            if (IgrokiDummy[index]["Occupied"] == a):
                hravci.itemconfig(mistsya_hravciv[a], fill="#ffffff")
            else:
                hravci.itemconfig(mistsya_hravciv[a], fill="#ff9f00")

def svet_term(index):
    if (index == -1): #это потушит всё
        for a in range(5):
            hravci.itemconfig(mistsya_hravciv[a], fill="#9f0000")
    else:
        for a in range(5):
            if (IgrokiDummy[index]["Occupied"]==a):
                hravci.itemconfig(mistsya_hravciv[a], fill="#ffffff")
            else:
                hravci.itemconfig(mistsya_hravciv[a], fill="#9f0000")









def read_q0():
    base_0 = codecs.open ('otbor.txt', 'r', "utf_8_sig")
    for line in base_0:
        HUHA = line.rstrip("\n")
        cheq = Record_voprosy(Question = HUHA, Answer = int(base_0.readline()))
        base_otbor.append(cheq)
    base_0.close()
    t_v_otbor.place (relx = 0.01, rely = 0.8, width=444, height=100)
    global index_voprosa
    index_voprosa = randint(0, len(base_otbor)-1)
    vopros_otbora.set(base_otbor[index_voprosa].Question)
    log.write(base_otbor[index_voprosa].Question + '\n')
    root.otbor_corr_field = tk.Label(root, justify=tkinter.LEFT, bg=yellow, textvariable=qual_corr, wraplength = 330)
    root.otbor_corr_field.place(relx=0.1, rely=0.77, width=69, height=16) # to be rectified
    # следующая часть нужна только для отладки
    # for a in range (len(base_otbor)):
    #     print(base_otbor[a].Question)
    #     print(base_otbor[a].Answer)
    # print(base_otbor[index_voprosa].Answer)



def doSomething():
    if tkinter.messagebox.askyesno("Exit", "Do you want to quit the application?"):
        log.close()
        root.destroy()

def testVal(inStr, acttyp):
    if acttyp == '1':
        if not inStr.isdigit():
            return False
    return True

def apribojimas (*args):
    length = user_name.get()
    if len(length) > 4:
        user_name.set(length[:4])

def q_q(a):
    global Qual_Field
    if Qual_Field:
        pass
    else:
        Qual_Field = True
        global active_qual
        #print('active_qual = '+str(active_qual))
        #print('stands len = ' + str(len(qualifying_round_stands)))
        light_qual(active_qual)
        root.title (ImenaIgrokov[active_qual]+", введите ответ")
        root.begin = datetime.now()


def light_qual(mmm):
    global canvas, qualifying_round_stands
    for we in range(6):
        if (we == mmm):
            canvas.itemconfig(qualifying_round_stands[we], fill = "#ffffff")
        else:
            canvas.itemconfig(qualifying_round_stands[we], fill="#ff9f00")

def after_otbor():
    root.after_cancel(root.komanda) # root.komanda (?)
    global counter, result, label_w_names
    qualans_sound=pygame.mixer.Sound("sounds/greed_qualifying_answer.wav")
    a = ""
    if (counter == 0):
        tkinter.messagebox.showinfo("Капитан", "Кто капитан команды?") #надо
        xx, yy, xx1, yy1 = canvas.coords(qualifying_round_stands[root.XYZ[0]['Original']])
        #print(xx, yy, xx1, yy1)
        result = canvas.create_text(xx+44, yy-22, text=str(root.XYZ[0]['Otvet']), fill="#ffff00", width=80)
        canvas.tag_raise(result)
        root.title ("Капитан команды - " + root.XYZ[0]["Name"] + ", ответ: "+str(root.XYZ[0]["Otvet"]))
        qualans_sound.play()
        log.write(root.XYZ[0]["Name"] + " (" +str(root.XYZ[0]["Otvet"]) + ") - капитан" +  "\n")
        root.otbor_corr_field.place_forget()
        t_v_otbor.place_forget()
        #dopisat'
    if (counter < 5):
        #canvas.delete(label_w_names[root.XYZ[counter]['Original']])
        counter +=1
    if (1 <= counter <= 4):
        tkinter.messagebox.showinfo("Следующий игрок", "Кто игрок №" + str(counter)+" ?") #надо
        canvas.delete(result)
        canvas.delete(label_w_names[root.XYZ[counter-1]['Original']])
        xx, yy, xx1, yy1 = canvas.coords(qualifying_round_stands[root.XYZ[counter]['Original']])
        #print(xx, yy, xx1, yy1)
        result = canvas.create_text(xx+44, yy-22, text=str(root.XYZ[counter]['Otvet']), fill="#ffff00", width=80)
        canvas.tag_raise(result)
        qualans_sound.play()
        root.title ("Игрок №" + str(counter) + " - " + root.XYZ[counter]["Name"] + ", ответ: "+str(root.XYZ[counter]["Otvet"]))
        if (counter == 1):
            a = "первый"
        elif(counter == 2):
            a = "второй"
        elif (counter == 3):
            a = "третий"
        elif(counter == 4):
            a = "четвёртый"
        log.write(root.XYZ[counter]["Name"] + " (" +str(root.XYZ[counter]["Otvet"]) + ") - " + a + " игрок"+" \n")
        root.komanda = root.after(100, after_otbor)
    else:
        tkinter.messagebox.showinfo("Выбывший", "Кто покидает игру?") #надо
        canvas.delete(result)
        canvas.delete(label_w_names[root.XYZ[counter-1]['Original']])
        qualans_sound.play()
        root.title ("Выбывший игрок" + " - " + root.XYZ[counter]["Name"] + ", ответ: "+str(root.XYZ[counter]["Otvet"]))
        xx, yy, xx1, yy1 = canvas.coords(qualifying_round_stands[root.XYZ[counter]['Original']])
        #print(xx, yy, xx1, yy1)
        result = canvas.create_text(xx+44, yy-22, text=str(root.XYZ[counter]['Otvet']), fill="#ffff00", width=80)
        canvas.tag_raise(result)
        log.write(root.XYZ[counter]["Name"] + " (" +str(root.XYZ[counter]["Otvet"]) + ") "+ "\n")
        tkinter.messagebox.showinfo("Начинаем!", "Команда готова, мы начинаем игру") # дописать
        canvas.delete('all')
        label_w_names = []
        canvas.place_forget()
        pygame.mixer.music.stop()
        #pygame.mixer.music.load("sounds/greed_cue.mp3")
        #pygame.mixer.music.play(0)
        for i in range (5):
            aux["Name"] = root.XYZ[i]["Name"]
            aux["Share"] = 1
            aux["Sgor"] = 0
            aux["Nesgor"] = 0
            aux["Occupied"] = i
            X = aux.copy()
            IgrokiDummy.append(X)
        Igroki.place(relx=0.03, rely=0.03)
        for x in range(5):
            if (x == 0):
                viens = Image.open("Objects/target_colored.png")
            else:
                viens = Image.open("Objects/target_back.png")
            viens.thumbnail((20, 20), Image.ANTIALIAS)
            root.tkimage = ImageTk.PhotoImage(viens)
            images.append(root.tkimage)
        for a in range (5):
            root.test = tk.Label(Igroki, compound=tk.BOTTOM, text=IgrokiDummy[a]["Name"], image=images[a])
            dadc.append(str(2520 // (a + 1)))
            eax.append(tk.Label(Igroki, text=str(IgrokiDummy[a]["Sgor"]+IgrokiDummy[a]["Nesgor"])))
            nuotraukos.append(root.test)
            nuotraukos[a].place(x=15, y=5 + 55 * a)
            eax[a].place(x=79, y=5 + 55 * a)
            #eax[a]["text"] = str(int(eax[a]["text"]) - 1)
            #global vopros
        hravci.place(x=610, y=360)
        for a in range(5):
            if (a == 0):
                p = hravci.create_rectangle((210, 200), (290, 260), fill="#ff9f00")
            else:
                p = hravci.create_rectangle((15 + 89 * (a - 1), 10), (95 + 89 * (a - 1), 70), fill="#ff9f00")
            mistsya_hravciv.append(p)
            #print(hravci.coords(mistsya_hravciv[a]))
            x, y, x1, y1 = hravci.coords(mistsya_hravciv[a])
            # p = canvas.create_polygon(())
            # p = canvas.create_polygon(())
            pvp = next((i for i, item in enumerate(IgrokiDummy) if item["Occupied"] == a), None)
            pp = hravci.create_text((x + x1) // 2, (y + y1) // 2, text=IgrokiDummy[pvp]["Name"], fill="#00007f", width=45)
            label_w_names.append(pp)
        global stage
        global vopros_show
        global stage
        vopros_show = root.after(1000, lambda p = stage: read_12345678(p))


def showcorr():
    root.after_cancel(otbor_waitforcorr)
    qual_corr.set(base_otbor[index_voprosa].Answer)
    log.write("Правильный ответ: "+str(base_otbor[index_voprosa].Answer)+'\n') #Дописать
    log.write("Результаты: "+'\n')
    root.XYZ = sorted(Players, key = lambda i: (i['Distance'], i["Vremya"]))
    global komanda
    root.komanda = root.after(100, after_otbor)





    #root.otbor_corr_field = tk.Label(root, justify=tkinter.LEFT, bg=yellow, textvariable=qual_corr, wraplength = 330) #HERE!
   # root.otbor_corr_field.place(relx=0.1, rely=0.77, width=37, height=16) # to be rectified



def otbor_next():
    global T
    root.after_cancel(root.T)
    global active_qual
    if active_qual <= 4: #должно быть 4
        active_qual +=1
        name_entry["state"] = "normal"
        light_qual(active_qual)
        root.title (ImenaIgrokov[active_qual]+", введите ответ")
    else:
        for spam in range(6):
            canvas.itemconfig(qualifying_round_stands[spam], fill="#ff9f00")
        visi_atsake = pygame.mixer.Sound("sounds/greed_qualifying_round_time_end.wav")
        visi_atsake.play()
        name_entry.place_forget()
        root.title ("Какой же ответ правильный?")
        global otbor_waitforcorr
        otbor_waitforcorr = root.after (500, showcorr) #1500



def q_a(*args):
    length = user_name.get()
    if len(length)==0:
        pass
    elif (int(length)==0):
        pass
    else:
        root.end = datetime.now() - root.begin
        #print(str(root.end)) #debug
        P ["Name"] = ImenaIgrokov[active_qual]
        P ["Otvet"] = int(user_name.get())
        P ["Vremya"] = root.end
        P ["Distance"] = abs(P ["Otvet"] - base_otbor[index_voprosa].Answer)
        P ["Original"] = active_qual
        DICR = P.copy()
        Players.append(DICR)
        root.begin = datetime.now()
        user_name.set("")
        name_entry["state"]= "disabled"
        root.Qual_Field = False
        root.T = root.after(500, otbor_next) #1500


def kwalif():
    global canvas, qualifying_round_stands, qualifying_showans, label_w_names
    for a in range(len(vardas_variable)):
        if vardas_variable[a].get()=="":
            tkinter.messagebox.showwarning("Имена", "По меньшей мере у одного из игроков пустое имя. Исправьте")
            break
    else:
        for b in range(6):
            ImenaIgrokov.append(vardas_variable[b].get())
        tkinter.messagebox.showinfo("Отбор", "Внимание, вопрос отборочного тура!")
        log.write ("Отборочный тур"+'\n')
            # дописать
        greed.place_forget()
        for x in range (6):
            pole_imya[x].place_forget()
        read_q0()
        # canvas = tk.Canvas(root, width=600, height=300, bg='#cfcfcf')
        # canvas.place(x=400, y=210)
        # a = canvas.create_oval(40, 80, 70, 110, fill="#00ff7f")
        # canvas.place_forget()
        canvas.place(relx=0.05, rely=0.12)
        # canvas.delete(a)
        # qualifying_round_stands = []
        # qualifying_showans = []
        # label_w_names = []
        for count in range(6):
            h = canvas.create_rectangle(17 + 97 * count, 150, 17 + 97 * count + 88, 240, fill="#ff9f00")
            qualifying_round_stands.append(h)
            xx, yy, xx1, yy1 = canvas.coords(qualifying_round_stands[count])
            h1 = canvas.create_rectangle(17 + 97 * count, 115, 17 + 97 * count + 88, 146, fill="#3f3f3f")
            qualifying_showans.append(h1)
            h2 = canvas.create_text(xx + 44, yy + 44, text=ImenaIgrokov[count], fill="#000000", width=80)
            label_w_names.append(h2)
        name_entry.place(relx= OTBOR_X, rely=OTBOR_Y)
        name_entry.bind("<Button-1>", q_q(active_qual))
        name_entry.bind("<Return>", q_a)


pygame.mixer.music.load("sounds/greed_back0.mp3")
pygame.mixer.music.play(-1)


# root = tk.Tk()
# root.geometry ("600x450")
# root.title ("Greed")
Igroki = ttk.LabelFrame(root, text = 'Игроки', width=150, height=330)
log = open ('log.txt', 'a')
log.write('\n')
user_name = tk.StringVar()
user_name.trace('w', apribojimas)
vopros_otbora = tk.StringVar()
qual_corr = tk.StringVar()
termotvet = tk.StringVar()
mainmenu = tk.Menu(root)
root.config (menu = mainmenu)
# mainmenu.add_command(label = 'Новая игра', command = newgame)
mainmenu.add_command(label = 'Выход', command = doSomething)
greed = tk.Button(root, text="Начать игру", command=kwalif, width = 7, height = 5)
greed.place(relx=0.3, rely=0.3)
vardas_variable=[] #текст имен игроков
pole_imya = [] #поле для ввода имен игроков
for x in range(6):
    dummy = tk.StringVar()
    dummy.set("Игрок "+str(x+1))
    vardas_variable.append(dummy)

for x in range(6):
    vardas = ttk.Entry(root, textvariable =vardas_variable[x])
    pole_imya.append(vardas)

for x in range (6):
    pole_imya[x].place(width = 125, relx=0.05, rely = 0.05+(0.15*x))

#play_accept_otbor = threading.Thread(target = otbor_accept, name = "otbor_accept")
#back01 = threading.Thread (target = back, name="back")
t_v_otbor = tk.Label(root, justify=tkinter.LEFT, bg="#8492ee", textvariable=vopros_otbora, wraplength = 330) #padx = 0.12, pady=0.01
name_entry = ttk.Entry(root, width=15, textvariable=user_name, validate="key")
name_entry['validatecommand'] = (name_entry.register(testVal), '%P', '%d')
#name_entry.place(relx=OTBOR_X , rely=OTBOR_Y) #nado vernut'
name_entry.place_forget()
#name_entry.bind("<Button-1>", q_q(active_qual))
#name_entry["state"] = 'hidden' попытался скрыть
root.protocol('WM_DELETE_WINDOW', doSomething)  # root is your root window
root.bind('<KeyPress>', onKeyPress)
vvod = tk.Entry(textvariable = termotvet)
vvod.bind("<Return>", accepted_in_terminator)

#T = Timer(1.5, otbor_next)


root.mainloop()
