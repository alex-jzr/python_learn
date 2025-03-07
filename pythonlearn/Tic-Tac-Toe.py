#喜报：！！！Alex同学于2025.3.2完成tic-tac-toe!!!可喜可贺:)#
import os

#user = 1
item = ["#", "X", "O"]
user1 = []
user2 = []

def clear_screen():
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # macOS/Linux
    else:
        os.system('clear')

def chees_print():
    # 打印列标
    print("  0  1  2")
    
    for i in range(3):
        # 打印行标
        print(i, end=" ")
        
        for p in range(3):    
            if (i, p) in user1:   # in 可以检查元素是否在集合中
                print(item[1], " ", end="")  # end=""用于控制不换行
            elif (i, p) in user2:
                print(item[2], " ", end="")
            else:
                print(item[0], " ", end="")
        print()  # 换行

def user_input():
    #global user
    user = 1
    while True:
        try:
            # 获取用户输入的坐标，并将其拆分为整数
            x, y = map(int, input("Enter coordinates x,y (0-2): ").split(","))
            
            # 检查输入的坐标是否在合法范围内
            if not (0 <= x <= 2 and 0 <= y <= 2):
                print("Coordinates must be between 0 and 2. Please try again.")
                continue  # 如果坐标不合法，继续循环
            
            # 检查该位置是否已经被占用
            if (x, y) in user1 or (x, y) in user2:
                print("This position is already taken. Try again.")
                continue  # 如果位置已经被占用，继续循环
            
            # 根据当前玩家（user）来添加标记
            if user == 1:
                user1.append((x, y))
                user = 2  # 玩家1下完后轮到玩家2
            else:
                user2.append((x, y))
                user = 1  # 玩家2下完后轮到玩家1
            break  # 输入成功后跳出循环
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a comma.")
            # 如果输入不是有效的数字，提示错误并重新输入
    
    return user  # 返回当前玩家的标识

def win(user_positions):
    # 横向和纵向检查
    for i in range(3):
        # 横向连线检查
        if (i, 0) in user_positions and (i, 1) in user_positions and (i, 2) in user_positions:
            return True
        # 纵向连线检查
        if (0, i) in user_positions and (1, i) in user_positions and (2, i) in user_positions:
            return True
    
    # 斜线检查
    if (0, 0) in user_positions and (1, 1) in user_positions and (2, 2) in user_positions:
        return True
    if (0, 2) in user_positions and (1, 1) in user_positions and (2, 0) in user_positions:
        return True

    return False  # 如果没有找到连线，返回False

def draw(user1, user2):
    # 检查棋盘是否填满，如果是且没有获胜者，则为平局
    if len(user1) + len(user2) == 9 and not (win(user1) or win(user2)):
        return True
    return False

# 主循环：
while True:
    clear_screen()  # 每次打印棋盘之前先清空屏幕
    chees_print()
    user_input()

    if win(user1):
        print("user1 win !")
        break
    elif win(user2):
        print("user2 win !")
        break
    elif draw(user1, user2):  # 检查平局
        print("It's a draw!")
        break
