#!/usr/bin/python
# -*- coding: utf-8 -*-

from googlesearch import search

print("""

███████╗░██████╗░█████╗░░█████╗░███╗░░██╗
██╔════╝██╔════╝██╔══██╗██╔══██╗████╗░██║
█████╗░░╚█████╗░██║░░╚═╝███████║██╔██╗██║
██╔══╝░░░╚═══██╗██║░░██╗██╔══██║██║╚████║
██║░░░░░██████╔╝╚█████╔╝██║░░██║██║░╚███║
╚═╝░░░░░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝
""")


print("Welcome To FSCAN - Developed By Feqtico.")
  
word = input(" Dork To Scan: ")

arama = word
  
for j in search(arama, tld="com", num=30, stop=30, pause=2):
    print(j)
