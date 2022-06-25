#pip install selenium
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import random
import time

#scarica i driver di google in base alla tua versione di chrome
PATH = r"C:\Users\Emanuele\Desktop\chromedriver.exe" #metti il path del tuo driver di google
driver = webdriver.Chrome(PATH)

immagini = 'https://images.google.com'
nrand = str(random.randint(1,9))

argomenti = ['Giacomo Leopardi', 'Scapigliatura', 'Carducci', 'Naturalismo', 'Verismo', 'Giovanni Verga', 'Decadentismo', 'Simbolismo', 'Giovanni Pascoli', 'Luigi Pirandello', 'Italo Svevo', 'Giuseppe Ungaretti', 'Primo Levi', 'Belle epoque', 'Italia Giolittiana', 'Prima guerra mondiale', 'Fascismo', 'Totalitarismi',
             'Crisi del 29', 'Seconda guerra mondiale', 'Germania nel primo dopoguerra', 'American Independence war', 'Victorian Age', 'Charles Dickens', 'Oscar Wilde and Dorian Grey', 'George Orwell Animal Farm', 'George Orwell 1984', 'Brave new World', 'Geometria Solida', 'Calcolo Combinatorio', 'Probabilita', 'Vlan', 'Crittografia', 'Certificati Digitali', 'Wireless e Crittografia Wireless', 'Ftp', 'Dns', 'InterVlan Routing', 'Database', 'mysql', 'php']

valore = random.choice(argomenti)
print(valore)
driver.maximize_window()
driver.get(immagini)
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div').click()
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(valore)
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button/div').click()
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div['+nrand+']/a[1]/div[1]/img').click()
 
#avvia il bot e lascia che faccia tutto da solo, se non funziona chiudi e fai Ctrl + C nel terminale. Re runna il bot 
