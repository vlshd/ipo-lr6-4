a = input("Введите строку для поиска: ") # запрашивает строку
with open('text.txt', 'r', encoding='utf-8') as file: # открывает файл в режиме чтения
        b = file.readlines() # считывает все строки из файла в список b

c = [line.strip() for line in b if a in line] # создает список, который содержит строки из b с поодстрокой a
colvo = len(c) # количество строк в списке
c.sort(key=len) # сортирует строки от короткой к длинной
print("Найденные строки:")
for line in c: # перебирает строки в списке
    print(line) # выводит строку
    
print(f"Количество строк, содержащих '{a}': {colvo}") 