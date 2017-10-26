#server_const.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()

# Сервер
port = 9090
sock.bind(('', port)) # '' - любой интерфейс сервера, 9090 порт.
print("Listening on {}".format(port))

# С помощью метода listen мы запустим для данного сокета режим прослушивания. 
# Метод принимает один аргумент — максимальное количество подключений в очереди.
sock.listen(5) #

# Принимаем подключение с помощью метода accept, который возвращает кортеж 
# с двумя элементами: новый сокет и адрес клиента.
conn, addr = sock.accept()
while True:

	print ("Connected: {}".format(addr[0]))

	# Теперь мы установили с клиентом связь и можем с ним «общаться».
	# Чтобы получить данные нужно воспользоваться методом recv, который в качестве 
	# аргумента принимает количество байт для чтения.
	# Мы будем читать порциями по 1024 байт (или 1 кб)
	while True:
	    data = conn.recv(1024)
	    if not data:
	       break
	#для наглядности мы что-то сделаем с полученными данными и отправим их обратно клиенту.
	    print ("Data recieved from {}: {}".format(addr[0], data))
	    conn.send(data.upper()) 

	conn.close()

	# Cервер готов. Он принимает соединение, принимает от клиента данные, возвращает их
	# виде строки в верхнем регистре и закрывает соединение.