#Once I have the functions defined in a specific file, I need to create a main module 

from identify_functions import *
# translate =  apartir do diretorio . ponto e o separador e logo em seguida voce coloca o nome do arquivo 
# ou seja eu mostro qual e o diretorio pra depois mostrar o arquivo onde estao definidas as funcoes

mylist = []
print("filling out...")
fillInventory(mylist)
print("Viewing")
showInventory(mylist)

print("researching....")
searchItemInInventory(mylist)
print("modifying...")
depreciationForItem(mylist)

print("Delete it....")
ExclusionSerial(mylist)

print("resuming...")
Resumevalues(mylist)