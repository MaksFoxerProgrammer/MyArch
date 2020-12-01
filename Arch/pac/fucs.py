import time, random
import os

def p1(fille):
	try:		
		f = open(fille + ".txt")
		print(f.read())
		print("==============")
		print("Файл прочитан")

	except FileNotFoundError:

		ind = 1
		print("Упс, файла нет... ")
		while(ind == 1):
			try:
				var = int(input("Хотите создать новый? (1 - да, 2 - нет) "))
				if var ==  1:
					f = open (fille + ".txt", "w")
					ind = 0
				elif var == 2:
					print("Окей, операция отменина")
					ind = 0
				else:
					print("Вы ввели недопустимое значение... ")

			except ValueError:			
				print("Это вообще не цифры... Ну ты даешь... ")
			
	else:
		f.close()
		print("Ошибок не было, файл закрыт")
	pass

def p2(fille):

	ind = 1
	f = 0
	var = 1

	while ind == 1:
		print("Вы хотите Перезаписать файл, или добавить записи?")
		print("1 - ПЕРЕзаписать")
		print("2 - ДОполнить")
		var = int(input())

		if var == 1:
			print("Перезаписываем... ")
			f = open(fille + ".txt", "w")
			ind = 0

		elif var == 2:
			print("Дополняем... ")
			f = open(fille + ".txt", "a")
			ind = 0

		else:
			print("Такого варианта нет -_- ")
		pass

	text = input("Что напишем?) ")
	f.write(text + "\n")
	print("Запись прошла успешно, закрываю файл")
	f.close	
	pass

def p3(fille):
	f = open(fille + ".txt", "r")
	l = [line.strip() for line in f]
	print(l)
	pass

def p4():
	with open('newfile.txt', 'w', encoding='utf-8') as g:
		d = int(input())
		print('1 / {} = {} '.format(d, 1 / d), file=g)
		pass


def p5():
	print(random.random())
	pass

def p6():
	

	pass