# -*- coding: utf-8 -*-
import random
from math import ceil

debug = True
class game:
    area = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]

##    def move(area, move):
##        global debug
##        original = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
##        area_c = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
##        for row in range(4):
##            original[row] = area[row].copy()
##            area_c[row] = area[row].copy()
##        c = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
##        if debug: print("area_c isn't empty: %s" % (area_c != c))
##        a_score = 0
##        if move == "up":
##            for row in range(4):
##                original[row] = area[row].copy()
##                area_c[row] = area[row].copy()
##            for x in range(len(area_c[0])):
##                col_m = 4
##                for y in range(col_m):
##                    if debug: print("original = %s" % original)
##                    unoccupied = 0
##                    if debug: print("c length is %s" % len(c))
##                    while (c[unoccupied][x] != 0) and (unoccupied < len(c)-1):
##                        unoccupied += 1
##                        if debug: print("unoccupied = %s" % unoccupied)
##                    if debug: print("area[%s][%s] = %s" % (y, x, area_c[y][x]))
##                    if area_c[y][x] == 0:
##                        if debug: print(" is 0")
##                        first_val = 0
##                        mem = (0, "")
##                        mem_val = 0
##                        mem_str = ""
##                        for i in range(y+1, col_m):
##                            if debug: print("  i = %s" % i)
##                            if debug: print("  x = %s\n  first_val = %s" % (x, first_val))
##                            if (area_c[i][x] != 0) and (first_val == 0):
##                                first_val = area_c[i][x]
##                                mem = (first_val, "first")
##                                c[i][x] = 0
##                                area_c[i][x] = 0
##                                if debug: print("c&area[%s][%s] set to 0 (ln: 48)" % (i, x))
##                            elif (area_c[i][x] != 0) and (first_val != 0):
##                                if first_val == area_c[i][x]:
##                                    c[unoccupied][x] = first_val + area_c[i][x]
##                                    area_c[unoccupied][x] = c[unoccupied][x]
##                                    a_score += c[unoccupied][x]
##                                    if debug: print("score set to %s (ln: 54)" % a_score)
##                                    if debug: print("c&area[%s][%s] set to %s (ln: 55)" % (unoccupied, x, first_val + area_c[i][x]))
##                                    c[i][x] = 0
##                                    area_c[i][x] = 0
##                                    if debug: print("c&area[%s][%s] set to 0 (ln: 58)" % (i, x))
##                                    mem = (0, "second")
##                                    first_val = 0
##                                    while (c[unoccupied][x] != 0) and (unoccupied < len(c)-1):
##                                        unoccupied += 1
##                                    break
##                                else:
##                                    mem = (0, "")
##                                    c[y][x] = area_c[y][x]
##                                    if debug: print("c&area[%s][%s] set to %s (ln: 67)" % (y, x, area_c[y][x]))
##                                    break
##                            if debug: print("c = %s" % c)
##                        c[y][x] = area_c[y][x]
##                        if debug: print("c&area[%s][%s] set to %s (ln: 71)" % (y, x, area_c[y][x]))
##                        mem_val, mem_str = mem
##                        temp_mem = mem_str
##                        if mem_str == "": temp_mem = "none"
##                        if debug: print("memory value = %s and memory string = %s" % (mem_val, temp_mem))
##                        if mem_str == "first":
##                            c[unoccupied][x] = mem_val
##                            area_c[unoccupied][x] = mem_val
##                            if debug: print("c&area[%s][%s] set to %s (ln: 79)" % (unoccupied, x, mem_val))
##                            while (c[unoccupied][x] != 0) and (unoccupied < len(c)-1):
##                                unoccupied += 1
##                            mem_val = 0
##                            mem_str = ""
##                            temp_mem = ""
##                            mem = (0, "")
##                            first_val = 0
##                    elif area_c[y][x] != 0:
##                        if debug: print(" isn't 0")
##                        for i in range(y+1, col_m):
##                            if debug: print("  i = %s" % i)
##                            if (area_c[i][x] != 0):
##                                if area_c[y][x] == area_c[i][x]:
##                                    c[y][x] = area_c[y][x] + area_c[i][x]
##                                    area_c[y][x] = c[y][x]
##                                    a_score += c[y][x]
##                                    if debug: print("score set to %s (ln: 96)" % a_score)
##                                    if debug: print("c&area[%s][%s] set to %s (ln: 97)" % (y, x, area_c[y][x] + area_c[i][x]))
##                                    c[i][x] = 0
##                                    area_c[i][x] = 0
##                                    if debug: print("c&area[%s][%s] set to 0 (ln: 100)" % (i, x))
##                                    while (c[unoccupied][x] != 0) and (unoccupied < len(c)-1):
##                                        unoccupied += 1
##                                else:
##                                    c[y][x] = area_c[y][x]
##                                    if debug: print("c&area[%s][%s] set to %s (ln: 105)" % (y, x, area_c[y][x]))
##                                    break
##                        c[y][x] = area_c[y][x]
##                        if debug: print("c&area[%s][%s] set to %s (ln: 108)" % (y, x, area_c[y][x]))
##        elif move == "right":
##            cf, r = game.move(game.rotate(area_c, 1), "up")
##            if r == "blocked":
##                return (cf, "blocked")
##            else:
##                c = game.rotate(cf, 3)
##        elif move == "down":
##            cf, r = game.move(game.rotate(area_c, 2), "up")
##            if r == "blocked":
##                return (cf, "blocked")
##            else:
##                c = game.rotate(cf, 2)
##        elif move == "left":
##            cf, r = game.move(game.rotate(area_c, 3), "up")
##            if r == "blocked":
##                return (cf, "blocked")
##            else:
##                c = game.rotate(cf, 1)
##        if area_c != original:
##            return_val = (c, a_score)
##            if debug:
##                print("c = %s" % c)
##                print("area_c = %s" % area_c)
##            return return_val
##        else:
##            if debug:
##                print("Blocked.")
##                print("c = %s\no = %s" % (c, original))
##                print("area_c = %s" % area_c)
##            if debug: print("returned while executing with move == up")
##            return (area_c, "blocked")

    @staticmethod
    def move(area, move):
        arr = []
        original = []
        arr.extend([x.copy() for x in area])
        reward = 0
        original.extend([x.copy() for x in area])
        if move == "right":
            max_ci = len(arr[0]) - 1
            col_num = len(arr[0])
            row_num = len(arr)
            curr_row_i = 0
            curr_col_i = 0
            redo = False
            while curr_row_i < row_num:
                curr_row = arr[curr_row_i]
                redo = False
                curr_col_i = 0
                while curr_col_i < col_num:
                    redo = False
                    curr_tile = arr[curr_row_i][curr_col_i]
                    if True not in [x != 0 for x in curr_row]:
                        break
                    if curr_tile == 0:
                        for tile_i in range(curr_col_i, max_ci):
                            arr[curr_row_i][tile_i] = arr[curr_row_i][tile_i+1]
                        arr[curr_row_i][max_ci] = 0
                        if not True in [x != 0 for x in curr_row[curr_col_i:]]:
                            redo = False
                            break
                        else:
                            redo = True
                    else:
                        redo = False
                        for tile_i in range(curr_col_i + 1, col_num):
                            tile = arr[curr_row_i][tile_i]
                            if tile == curr_tile:
                                arr[curr_row_i][curr_col_i] *= 2
                                arr[curr_row_i][tile_i] = 0
                                reward += arr[curr_row_i][curr_col_i]
                                break
                            elif (tile != 0) and (tile != curr_tile):
                                break
                    if not redo:
                        curr_col_i += 1
                if not redo:
                    curr_row_i += 1
        elif move == "up":
            cf, r = game.move(game.rotate(arr, 1), "right")
            if r == "blocked":
                return (cf, "blocked")
            else:
                arr = game.rotate(cf, 3)
                reward = r
        elif move == "left":
            cf, r = game.move(game.rotate(arr, 2), "right")
            if r == "blocked":
                return (cf, "blocked")
            else:
                arr = game.rotate(cf, 2)
                reward = r
        elif move == "up":
            cf, r = game.move(game.rotate(arr, 3), "right")
            if r == "blocked":
                return (cf, "blocked")
            else:
                arr = game.rotate(cf, 1)
                reward = r
        if arr != original:
            return (arr, reward)
        else:
            return (arr, "blocked")
    
    @staticmethod
    def rotate(array, num):
        res = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        arr = array.copy()
        for _ in range(num):
            for a in range(4):
                for b in range(4):
                    res[3-b][a] = arr[a][b]
            for x in range(4):
                arr[x] = res[x].copy()
        return res

    @staticmethod
    def is_stuck(area):
        arr = area.copy()
        bool_list = []
        bool_list.extend([0 in x for x in arr])
        if True in bool_list:
            return False
        empty_arr = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        if (game.move(arr, "up")[1] == "blocked") and (game.move(arr, "right")[1] == "blocked") and (game.move(arr, "down")[1] == "blocked") and (game.move(arr, "left")[1] == "blocked") and (arr != empty_arr):
            return True
        else:
            return False

    @staticmethod
    def new_random(area):
        arr = area.copy()
        row = round(random.random()*3)
        col = round(random.random()*3)
        bool_list = []
        bool_list.extend([0 not in x for x in arr])
        if True in bool_list:
            return arr
        while arr[row][col] != 0:
            row = round(random.random()*3)
            col = round(random.random()*3)
        val = 2
        if ceil(random.random()*10) == 10:
            val = 4
        arr[row][col] = val
        return arr

    @staticmethod
    def start():
        game.area = game.new_random(game.area)
        game.area = game.new_random(game.area)

    @staticmethod
    def reset():
        empty_arr = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        game.area = empty_arr.copy()
        game.score = 0
        game.start()
        return(game.area.copy(), 0)