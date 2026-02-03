import pyautogui
import time

def generate_random_mouse():
    print("Двигайте мышкой...")
    #coordinates = [] #тут будут храниться координаты
    result_num = 0
   #for _ in range(500): #делаю снимки координат и по совместительству тут считаю время
    #    x, y = pyautogui.position() #запиываю текущее положение курсора в х, y
        #print(x^y, end=" ", flush=True)
      #  print((x + y)% 2, end=" ", flush =True)
     ##   coordinates.append(x)
       ## coordinates.append(y)
     #   result_num = result_num ^ x ^ y
      #  time.sleep(0.01) #задержка

    last_x, last_y = pyautogui.position()
    count = 0 #счетчик снимков
    while count < 100: #прост ограничитель
    #while True: #пока рабоатт прогармма
        x, y = pyautogui.position()
        if (x, y) != (last_x, last_y):
           # print((x + y) % 2, end="", flush=True)
            #print("х равно ", x, "у равно", y, "и xor = ")
           # print(x^y, end=" ", flush=True)
          #  print(count, "x =", x, "y =", y, "|XOR x^y =", x^y, end=" ", flush=True)
            #print(f"#{count} x={x} y={y}|XOR x^y ={x^y}")
            result_num = result_num ^ x ^ y
            print(f"№ {count+1:<3} |x= {x:<5} |y= {y:<5}|XOR x^y= {x^y:<5} |XOR № {count:<3}^ № {count+1:<3} = {result_num:<5}")
            #print("|XOR", result_num)
            last_x, last_y = x, y
            count += 1
    return result_num
#обработка данныхg
# ^ побитовое сравнение ИЛИ
   ## random_result = 0
    ##for i in range(len(coordinates)):
    ##    random_result=random_result^coordinates[i]
   ## return random_result# % 256 #возвращаю в диапазоне 0-255

number = generate_random_mouse()
print("Результат: ", number)