import os #для вывода окна

file_in_name = "meow.txt"
file_out_name = "результат.bin"

#key = 225
key = b"meow" 
#rb - read bytes, wb -write bytes
with open(file_in_name, "rb") as file: #открываю файл и считываю байты
    data = file.read()
#encrypted_data = bytes([b^key for b in data])
encrypted_data = bytes([data[i]^key[i%len(key)]for i in range(len(data))])#беру по индексу i и перебираю для всей длины слова
with open(file_out_name, "wb") as file:
    file.write(encrypted_data)
print ("Текст успешно зашифрован/расшфрован в файле", file_out_name)
os.startfile(file_out_name)