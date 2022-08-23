from selenium import pyautogui as pyg
from time import sleep
def pesquisaNoGoogle():
    texto = pyg.prompt('Qual site você deseja pesquisar no Google!')
    while (texto == ''):
        pyg.alert('Por favor, insira algum texto!')
		texto = pyg.prompt('Qual site você deseja pesquisar no Google!')
        if (texto == None):
		exit()
pyg.press('win')
pyg.write('google', interval = 0.5)
pyg.press('Enter')
sleep(5)
pyg.write(texto, interval = 0.5)
pyg.press('Enter')
pesquisaNoGoogle()