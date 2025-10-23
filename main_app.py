#!/usr/bin/env python
import pygame as main_window
import tkinter as tk
from tkinter import messagebox
import sys
from photo_loader import getPhoto
from photo_loader import init
from get_path import path
PATH='Photos' #default path
PATH=path ()
init(PATH)
# Aici initializez window-ul pe care pun poza
WINDOW_SIZE = (800, 800)  # Default size, daca am eroare de exemplu
MASK_COLOR=(0, 0, 0, 255) # Culoarea mastii (negru sau alb, depinde de mod, default e negru)
main_window.display.set_caption("SARMALUTA REVEAL!!!")
final_width=0
final_height=0
image=main_window.image
mask=main_window.mask
main_window.init()
info = main_window.display.Info()
monitor_width_pixels=info.current_w-200
monitor_height_pixels=info.current_h-70
image_ratio=()
crt_photo_path=-1
paths=[]
index=0
new_path=getPhoto (PATH)
def nextPhoto ():
    global index
    index=(index+1)%len(paths)
def prevPhoto ():
    global index
    index=(index-1)%len(paths)
while new_path!=-1:
    paths.append (new_path)
    new_path=getPhoto (PATH)
def initializeScreen ():
    global final_height
    global final_width
    global screen
    global image
    global mask
    global image_ratio
    main_window.init()
    image = main_window.image.load(paths[index])
    image_ratio = image.get_rect()  # Asta imi da width + height aparent
    image_w, image_h = image.get_size()
    scale_w = monitor_width_pixels / image_w
    scale_h = monitor_height_pixels / image_h
    scale = min(scale_w, scale_h, 1)
    final_width = int(image_w * scale)
    final_height = int(image_h * scale)
    image = main_window.image.load(paths[index])
    image = main_window.transform.scale(image, (final_width, final_height))
    screen = main_window.display.set_mode((final_width+SIDEBAR_WIDTH, final_height))
    mask = main_window.Surface((final_width, final_height), main_window.SRCALPHA)
    mask.fill(MASK_COLOR)
def resetMask ():
    global mask
    mask = main_window.Surface((final_width, final_height), main_window.SRCALPHA)
    mask.fill(MASK_COLOR)
SIDEBAR_WIDTH=150
initializeScreen ()
COVERED=0
UNCOVERED=1
running = 1
drawing = 0
mode=COVERED
while running:
    for event in main_window.event.get():
        if event.type == main_window.QUIT: # ENUM ptr iesire ig
            if messagebox.askyesno ("Confirm", "Sigur sigur vrei sa inchizi programul sarmaluitor???"):
                running = 0
        elif event.type == main_window.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos=main_window.mouse.get_pos()
            if button2_rect.collidepoint (mouse_pos):
                resetMask ()
            elif button3_rect.collidepoint (mouse_pos):
                mode=1-mode
                if mode==UNCOVERED:
                    MASK_COLOR=(0, 0, 0, 0)
                else:
                    MASK_COLOR=(0, 0, 0, 255)
                mask.fill (MASK_COLOR)
            elif button4_rect.collidepoint (mouse_pos):
                prevPhoto ()
                initializeScreen ()
            elif button_rect.collidepoint (mouse_pos):
                nextPhoto ()
                initializeScreen ()
            else:
                drawing=1
        elif event.type == main_window.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = 0
    if drawing:
        mouse_pos = main_window.mouse.get_pos()
        brush_radius = 20
        main_window.draw.circle(mask, (0, 0, 0, 0), mouse_pos, brush_radius)
    sidebar_rect=main_window.Rect (final_width, 0, SIDEBAR_WIDTH, final_height)
    main_window.draw.rect (screen, (50, 50, 50), sidebar_rect)
    #Pt urmatoarea imagine, render button DECI BUTTON_RECT E PT NEXT BUTTON AAAAAAAAAAAAAA (end my suffering)
    button_rect=main_window.Rect (final_width+25, 50, 100, 40)
    main_window.draw.rect (screen, (255, 255, 191), button_rect)
    font=main_window.font.SysFont (None, 18)
    text=font.render ("Next Sarmaluta", True, (0, 0, 0))
    screen.blit(text, (final_width + 30, 65))
    #Pt prev imagine
    button4_rect=main_window.Rect (final_width+25, 100, 100, 40)
    main_window.draw.rect (screen, (255, 255, 191), button4_rect)
    text4=font.render ("Prev Sarmaluta", True, (0, 0, 0))
    screen.blit (text4, (final_width+30, 115))
    #Pt reset ecran negru, BUTTON2_RECT
    button2_rect=main_window.Rect (final_width+25, 150, 100, 40)
    main_window.draw.rect (screen, (255, 255, 191), button2_rect)
    text2=font.render ("Reset", True, (0, 0, 0))
    screen.blit(text2, (final_width + 30, 165))
    #Pt Mode
    button3_rect=main_window.Rect (final_width+25, 200, 100, 40)
    if mode==COVERED:
        main_window.draw.rect (screen, (170, 255, 0), button3_rect)
    else:
        main_window.draw.rect (screen, (255, 0, 0), button3_rect)
    text3=font.render ("Mode", True, (0, 0, 0))
    screen.blit (text3, (final_width+30, 215))
    #On screen
    screen.blit(image, (0, 0))
    screen.blit(mask, (0, 0))
    main_window.display.flip()
main_window.quit()