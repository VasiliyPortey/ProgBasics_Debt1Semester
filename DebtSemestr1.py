from random import randint

#Сдача задолженности по дисциплине "Основы программирования", первый семестр, вариант 6
#longestSequence - функция, которая находит наибольшую невозрастающую подпоследовательность в заданном массиве (параметр numList)
#Т.к. максимальная длина последовательности может быть у нескольких последовательностей внутри массива,
#я решил в качестве возвращаемого списка использовать именно последнюю из наибольших последователньостей

        
def longestSequence(numList):
    oldResultList = []
    endResultList = [numList[0]]
    endListStartIndex = 0
    index = 1
    while index<len(numList):
        if numList[index]<=numList[index-1]:
            endResultList.append(numList[index])
            index+=1
            continue
        else:
            if len(endResultList)>=len(oldResultList):
                endListStartIndex = index - len(oldResultList)
                oldResultList = endResultList
            endResultList = [numList[index]]
            index+=1
            continue    
    print('Последняя (!) из наибольших невозрастающих последовательностей: ', oldResultList, ' (начинается с ', endListStartIndex, '-го элемента стартового массива)')
    return oldResultList

listLength = int(input('Введите размер массива: '))
numbersList = []                #создаём и заполняем рандомными целыми числами от -10 до 10 список длины listLength
for i in range(listLength):
    numbersList.append(randint(-10, 10))    
print('Сгенерированный массив: ', numbersList)   
print(longestSequence(numbersList))