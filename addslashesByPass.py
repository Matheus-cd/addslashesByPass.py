#!/usr/bin/python

import sys

resultado=''

if len(sys.argv) != 2:
	print "\nModo de Uso: python addslashesByPass.py stringparaconversao\n"
	exit(0);

def split(word):
	return [char for char in word]

string1=sys.argv[1]
string2=split(string1)
length=len(string1)

for i in range(0,length):
	letra=string2[i]
	o=str(ord(letra))
	resultado = resultado+o+","

vazio = ""
result = resultado[:len(resultado)-1] + vazio
print '\nResultado: char('+result+')\n'


