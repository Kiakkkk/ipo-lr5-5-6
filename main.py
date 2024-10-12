file = open("text.txt", "r") #открывается файл для чтения
s = file.read() #массив = текст из файла
s = s.replace('o', 'a') #о заменяются на а
with open("output.txt", "w+") as file: #output.txt открывает файл с возможностью изменения
    file.write(s) #в output.txt записывается изменённая строка 