from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

from tkinter import *
from tkinter import messagebox

import openpyxl
import requests
import bs4
from openpyxl  import load_workbook
from openpyxl import Workbook
from openpyxl.utils import get_column_letter, column_index_from_string

import re

import urllib.request
import phonenumbers
from Level_1 import myCurrentURL


try:
	r = requests.head(myCurrentURL)
	if r.status_code == 200:
		print("works")
		execfile('Level_1.py')
	else:
		top = Tk()

		top.geometry("100x100")

		messagebox.showwarning("Warning", "Status code is not 200. Could fail.")

		top.withdraw()
		exit()
		top.mainloop()

    # prints the int of the status code. Find more at httpstatusrappers.com :)
except requests.ConnectionError:
	top = Tk()

	top.geometry("100x100")

	messagebox.showerror("error", "Please, verify your URL.")

	top.withdraw()
	exit()
	top.mainloop()