#!/usr/bin/python
 # -*- coding: utf-8 -*-
# Squad Insurgent Arty Calculator-Script
# by /u/r4ff4_ello| [GER] raffa_ello
# by /u/Maggiefix | [GER] Maggiefix
########################################
# Packages                             #
########################################
import math
import os
########################################
# Functions                            #
########################################
clear = lambda: os.system('cls')
def correct_input(u_input,description):
    # control the user inputs
    try:
        # Letters for X-axis
        letter_list = ["No", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        # Numbers for Y-axis
        number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
 
        if description == description_1:
            u_input = float(u_input)
            return u_input
 
        #Get Postions
        #Check First A-P
        var_1 = u_input[0]
        if var_1 in letter_list:
            x_grid = var_1
        #Search the K'S
        var_2 = [pos for pos, char in enumerate(u_input) if char == "K"]
        #If Grid is a K
        if var_2[0] == 0:
            var_2 = var_2[1:len(var_2)]
        #print(var_2)
        # extract y_grid and keypad
        # without subsetting like A1K1
        if len(u_input) > 5 and len(var_2) == 1:
            print("test")
            raise # raise error if you put something like A1K11 (K 1 to 9)
        if len(var_2) == 1 and int(u_input[1:var_2[0]]) in number_list:
            y_grid = int(u_input[1:var_2[0]])
            keypad = int(u_input[var_2[0]+1])
            sub_keypad_x = int(5)
            sub_keypad_y = int(5)
        # with subsetting like A1K7KX x = (1 to 9)
        elif int(u_input[1:var_2[0]]) in number_list and int(u_input[var_2[0]+1:var_2[1]]) in number_list[1:10]:
            y_grid = int(u_input[1:var_2[0]])
            keypad = int(u_input[var_2[0]+1:var_2[1]])
            sub_keypad = str(u_input[var_2[1] + 1:len(u_input) + 1])
            sub_keypad = int(sub_keypad[0])
            # Sub-keypad 1
            if sub_keypad == 1:
                sub_keypad_x = -5
                sub_keypad_y = 15
            # Sub-keypad 2
            elif sub_keypad == 2:
                sub_keypad_x = 5
                sub_keypad_y = 15
            # Sub-keypad 3
            elif sub_keypad == 3:
                sub_keypad_x = 15
                sub_keypad_y = 15
            # Sub-keypad 4
            elif sub_keypad == 4:
                sub_keypad_x = -5
                sub_keypad_y = 5
            # Sub-keypad 5
            elif sub_keypad == 5:
                sub_keypad_x = 5
                sub_keypad_y = 5
            # Sub-keypad 6
            elif sub_keypad == 6:
                sub_keypad_x = 15
                sub_keypad_y = 5
            # Sub-keypad 7
            elif sub_keypad == 7:
                sub_keypad_x = -5
                sub_keypad_y = -5
            # Sub-keypad 8
            elif sub_keypad == 8:
                sub_keypad_x = 5
                sub_keypad_y = -5
            # Sub-keypad 9
            elif sub_keypad == 9:
                sub_keypad_x = 15
                sub_keypad_y = -5
            # Sub-keypad if you are stupid
            else:
                sub_keypad_x = 5
                sub_keypad_y = 5
        return x_grid, y_grid, keypad, sub_keypad_x, sub_keypad_y
    except:
        if description == description_2 or description == description_3:
            print(" 错误输入, 使用 A1K1 或者 A10K9 或者 A1K1K55!")
        else:
            print(" 输入比例尺例如 : 135!")
        u_input = str(input(description)).upper()
        return correct_input(u_input,description)
def get_input_string(input_tuple):
    # Function to return User Input for Output Statement
    x_grid, y_grid, keypad, sub_keypad_x, sub_keypad_y = input_tuple
    user_string = str(x_grid) + str(y_grid) + "K" +str(keypad)
    # Sub-keypad 1
    if sub_keypad_x == -5 and sub_keypad_y == 15:
        user_string += "K1"
    # Sub-keypad 2
    elif sub_keypad_x == 5 and sub_keypad_y == 15:
        user_string += "K2"
    # Sub-keypad 3
    elif sub_keypad_x == 15 and sub_keypad_y == 15:
        user_string += "K3"
    # Sub-keypad 4
    elif sub_keypad_x == -5 and sub_keypad_y == 5:
        user_string += "K4"
    # Sub-keypad 5
    elif sub_keypad_x == 5 and sub_keypad_y == 5:
        user_string += "K5"
    # Sub-keypad 6
    elif sub_keypad_x == 15 and sub_keypad_y == 5:
        user_string += "K6"
    # Sub-keypad 7
    elif sub_keypad_x == -5 and sub_keypad_y == -5:
        user_string += "K7"
    # Sub-keypad 8
    elif sub_keypad_x == 5 and sub_keypad_y == -5:
        user_string += "K8"
    # Sub-keypad 9
    elif sub_keypad_x == 15 and sub_keypad_y == -5:
        user_string += "K9"
    # Sub-keypad if you are stupid
    else:
        user_string += "K5"
    return user_string.upper()
def get_coordinates_from_input(input_tuple):
    x_grid, y_grid, keypad, sub_keypad_x, sub_keypad_y = input_tuple
    # Letters for X-axis
    letter_list = ["No","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    # Numbers for Y-axis
    number_list = [0   ,1  ,2  ,3  ,4  ,5  ,6  ,7  ,8  ,9  ,10 ,11 ,12 ,13 ,14 ,15 ,16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26 ]
    # Keypad coffsets
    keypad_list_x = [0   ,2.0  ,5.0  ,8.0  ,2.0  ,5.0  ,8.0  ,2.0  ,5.0  ,8.0]
    keypad_list_y = [0   ,8.0  ,8.0  ,8.0  ,5.0  ,5.0  ,5.0  ,2.0  ,2.0  ,2.0]
    # Sub keypad offsets
    sub_keypad_list_x = [0, -0.5, 0.5, -0.5, 0.5 ]
    sub_keypad_list_y = [0, 0.5 , 0.5, -0.5, -0.5]
 
    #Calculate X|Y Values
    for i in [i for i,x in enumerate(letter_list) if x == x_grid]:
        x_var = (i - 1) * 9
        # Get x-keypad offset
        for i in [i for i, x in enumerate(keypad_list_x) if i == keypad]:
              x_var = x_var + keypad_list_x[i]
              # Get x-sub_keypad offset
              if sub_keypad_x > 5:
                  x_var = x_var + (sub_keypad_x * 0.1 - 0.5)
              if sub_keypad_x < 5:
                  x_var = x_var - (0.5 - sub_keypad_x * 0.1)
    for i in [i for i,x in enumerate(number_list) if x == y_grid]:
        y_var = (i -1) * 9
        # Get y-keypad offset
        for i in [i for i, x in enumerate(keypad_list_y) if i == keypad]:
              y_var = y_var + keypad_list_y[i]
              # Get y-sub_keypad offset
              if sub_keypad_y > 5:
                 y_var = y_var + (sub_keypad_y * 0.1 - 0.5)
              if sub_keypad_y < 5:
                 y_var = y_var - (0.5 - sub_keypad_y * 0.1)
    return x_var, y_var
def get_vektor(x1,y1,x2,y2):
    #Verbindungsvektor berechnen
    x_bind_vek = x1 - x2
    y_bind_vek = y1 - y2
    #Länge des Verktors berechnen
    distance = math.sqrt(x_bind_vek**2 + y_bind_vek**2)
    return distance
def get_angle(x1,y1,x2,y2):
    #Build north vektor on arty-position
    nv_x = x1 - x1
    nv_y = (y1-1) - y1
    abs_nv = math.sqrt((nv_x ** 2) + (nv_y ** 2))
    #Build Targetvektor
    tv_x = x2 - x1
    tv_y = y2 - y1
    abs_tv = math.sqrt((tv_x ** 2) + (tv_y ** 2))
    #Skalar between nv and tv
    skalar = nv_x * tv_x + nv_y * tv_y
 
    if x1 != x2 or y1 !=y2:
        angle = math.degrees(math.acos(skalar/(abs_nv*abs_tv)))
    # Shoot NE - QI
    if x2 > x1 and y2 < y1:
        angle = angle
        #print("q1")
    # Shoot NW - QII
    elif x2 < x1 and y2 < y1:
        angle = 360 - angle
        #print("q2")
    # Shoot SW - QIII
    elif x2 < x1 and y2 > y1:
        angle = 360 - angle
        #print("q3")
    # Shoot SE - QIV
    elif x2 > x1 and y2 > y1:
        angle = angle
        #print("q4")
    # Schoot direct North
    elif x2 == x1 and y2 < y1:
        angle = 0
    # Schoot direct South
    elif x2 == x1 and y2 > y1:
        angle = 180
    # Schoot direct East
    elif x2 > x1 and y2 == y1:
        angle = 90
    # Schoot direct West
    elif x2 < x1 and y2 == y1:
        angle = 270
    # Fail
    else:
        angle = 666
    return angle
def get_clicks(distance):
    # Dictonary with approximate number of 'W' keystrokes to press for a given distance
    keystrokes_dic = {50  : "1579",
                      100 : "1558",
                      150 : "1538",
                      200 : "1517",
                      250 : "1496",
                      300:  "1475",
                      350 : "1453",
                      400 : "1431",
                      450 : "1409",
                      500 : "1387",
                      550 : "1364",
                      600 : "1341",
                      650 : "1317",
                      700 : "1292",
                      750 : "1267",
                      800 : "1240",
                      850 : "1212",
                      900 : "1183",
                      950 : "1152",
                      1000: "1118",
                      1050: "1081",
                      1100: "1039",
                      1150: "988",
                      1200: "918",
                      1250: "800"}
    diff_old = 10000
    for key, value in keystrokes_dic.items():
        diff_new = abs(distance - key)
        if distance < 50:
            click = "小于有效距离 (50m - 1250m)!"
        elif distance > 1250:
            click = "大于有效距离 (50m - 1250m)!"
            break
        elif diff_new < diff_old:
            diff_old = diff_new
            click = value
    return click
 
description_1   = " 地图比例尺        : "
description_2   = " 迫击炮位置       : "
description_3   = " 敌方位置      : "
########################################
# Inputs                               #
########################################
# User console-inputs
print("########################################################")
print("#             Squad Mortar Calculator v1               #")
print("#                   by Maggiefix                       #")
print("#               丝瓜迫击炮计算器                       #")
print("# 汉化      by CG-mEnacE =O.W.L.S.=BBKING              #")
print("########################################################")
print("# - 输入坐标例如                 : A8K1 or c10k1k9     #")
print("# - 不需要使用精确坐标例如 A1K7 就已经足够精确了       #")
print("########################################################")
print("")
 
#Test-Mode for faster testing with scripted input
#i1 = 300
#input_big_grid = correct_input(i1,description_1)
#i2 = "a1k1"
#input_arty = correct_input(i2.upper(),description_2)
#i3 = "a5k1"
#input_target = correct_input(i3.upper(),description_3)
 
#User-Input Mode with variable user input
i1 = input(description_1)
input_big_grid = correct_input(i1,description_1)
i2 = input(description_2)
input_arty = correct_input(i2.upper(),description_2)
i3 = input(description_3)
input_target = correct_input(i3.upper(),description_3)
 
while True:
 
 
    x1, y1 = get_coordinates_from_input(input_arty)
    x2, y2 = get_coordinates_from_input(input_target)
    angle  =  int(get_angle(x1, y1, x2, y2))
    distance = int(get_vektor(x1, y1, x2, y2) * input_big_grid / 9)
    click = get_clicks(distance)
    clear()
    print(description_1 + str(input_big_grid))
    print(description_2 + str(get_input_string(input_arty)))
    print(description_3 + str(get_input_string(input_target)))
    print(" 迫击炮坐标 X|Y : {} {}".format(x1, y1))
    print(" 敌方位置 X|Y : {} {}".format(x2, y2))
    print("################################################")
    print("       距离  = {} m".format(distance))
    print("       仰角 = {} mil".format(click))
    print("       方位角   = {} °".format(angle))
    print("################################################")
 
    while True:
        print("输入 = 数字以实现下列选项")
        print("  1   = 新迫击炮坐标")
        print("  2   = 新地图")
        print("  3   = 退出")
        go_on = str(input())
        # Enter = New Target
        if go_on == "":
            clear()
            big_grid = input_big_grid
            print(description_1 + str(big_grid))
            print(description_2 + " {}".format(get_input_string(input_arty)))
            input_arty = input_arty
            input_target = correct_input(input(description_3).upper(), description_3)
            break
        # 1   = New Mortar Position | Target.
        elif go_on == "1":
            clear = lambda: os.system('cls')
            clear()
            big_grid = input_big_grid
            print(description_1 + str(big_grid))
            input_1 = str(input(description_2))
            if not input_1:
                input_arty = input_arty
            else:
                input_arty = correct_input(input_1.upper(), description_2)
            input_target = correct_input(input(description_3).upper(), description_3)
            break
        # 2   = New Map
        elif go_on == "2":
            clear = lambda: os.system('cls')
            clear()
            print(" 新的计算")
            input_big_grid = float(input(description_1))
            input_arty = correct_input(input(description_2).upper(), description_2)
            input_target = correct_input(input(description_3).upper(), description_3)
            break
        # 3   = Exit
        elif go_on == "3":
            quit(" Bye")