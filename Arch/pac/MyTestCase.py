import unittest
import os 
import fun

class MyTestCase(unittest.TestCase):
	"""docstring for MyTestCase"""

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_1(self):
		os.system ('lsblk')

		ind = fun.inp(2, "Нужна разметка диска? \n" 
						"1 - да\n"
						"2 - нет\n"
						"Ваш выбор: ")
		if ind == 1:
			os.system ('lsblk')
			ind2 = input("Укажите диск (sda/sdb/sdc)")
			os.system ('cfdisk /dev/' + ind2)	
			os.system ('clear')
			os.system ('lsblk')

			root = input("Укажите ROOT раздел(sda/sdb 1.2.3.4 (sda5 например)): ")
			os.system('mkfs.ext4 /dev/' + root + ' -L root')
			os.system('mount /dev/' + root + ' /mnt')

			ind2 = fun.inp(2, "Нужен boot раздел? \n" 
						"1 - да\n"
						"2 - нет\n"
						"Ваш выбор: ")
			if ind2 == 1:
				boot = input("Укажите BOOT раздел(sda/sdb 1.2.3.4 (sda7 например)): ")
				os.system('mkfs.ext2  /dev/' + boot + ' -L boot')
				os.system('mkdir /mnt/boot')
				os.system('mount /dev/' + boot + ' /mnt/boot')