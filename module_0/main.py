import numpy as np
def game_core(number):
    count = 1
    predict = np.random.randint(1,101)
    while number != predict:
        count+=1
        if number > predict: 
            while number > predict:
                count+=1
                predict += 10
                while number < predict:
                    count+=1
                    predict -= 1
        elif number < predict: 
            while number < predict:
                count+=1
                predict -= 10
                while number > predict:
                    count+=1
                    predict += 1
    return(count) 
def score_game(game_core):
    count_ls = []
    np.random.seed(1)  
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")