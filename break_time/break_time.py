#!/usr/bin/python
# -*- coding: utf-8 -*-
import webbrowser
import time
import turtle

#Para correr el programa use:  python break_time.py 
total_breaks = 1
break_count = 0
# urls = [1:,2:,3:,4:]
# def show_message():#say_something

print("El trabajo ha comenzado ahora " + time.ctime())
while (break_count < total_breaks):
    time.sleep(3)#Para una hora coloque 3600.
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=HgzGwKwLmgM")
    break_count = break_count + 1
    print("Toma un respiro! Hora de buena musica " + time.ctime())
