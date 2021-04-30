from selenium import webdriver
import time
import xlrd
import openpyxl
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('--headless')

file = 'dados.xlsx'
index = 4
coluna = "E"

def get_infos():
    linhas = []
    tabela = xlrd.open_workbook(file).sheet_by_index(0)
    qtd_linhas = tabela.nrows
    for i in range(0, qtd_linhas - 1):
        atual = i + 1
        linhas.append(
            {
                'Linha': atual,
                'Logradouro': tabela.row(atual)[0].value,
                'Bairro': tabela.row(atual)[1].value,
                'CEP': tabela.row(atual)[2].value,
                'Cidade': tabela.row(atual)[3].value,
            }
        )

    return linhas

def writefile(coord,text):
    xfile = openpyxl.load_workbook(file)

    xfile["Planilha1"][coord] = text

    xfile.save(file)

def tem_cep(cep):
    driver.find_element_by_xpath(
        '/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input').send_keys(
        cep)
    driver.find_element_by_xpath(
        '/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div/input').send_keys(
        "IFPB Campina Grande")
    time.sleep(10)
    try:
        driver.find_element_by_xpath(
            '/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/button[1]').click()
    except:
        driver.find_element_by_xpath(
            '/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]').click()
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="section-directions-trip-details-msg-0"]').click()
    time.sleep(5)
    dist = driver.find_element_by_xpath(
        '/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[3]/div[1]/h1/span[1]/span[2]/span').text
    print(str(i + 2) + " - CEP - " + dist + " - CG")
    writefile(coluna + str(i + 2), tratamento(dist))
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[1]/button').click()

def n_tem_cep(logradouro,cidade):
    driver.find_element_by_xpath(
        '/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input').send_keys(
        logradouro + ', ' + cidade)
    driver.find_element_by_xpath(
        '/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div/input').send_keys(
        "IFPB Campina Grande")
    time.sleep(10)
    try:
        driver.find_element_by_xpath(
            '/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/button[1]').click()
    except:
        driver.find_element_by_xpath(
            '/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]').click()
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="section-directions-trip-details-msg-0"]').click()
    time.sleep(5)
    dist = driver.find_element_by_xpath(
        '/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[3]/div[1]/h1/span[1]/span[2]/span').text
    print(str(i + 2) + " - SEM CEP - " + dist + " - CG")
    writefile(coluna + str(i + 2), tratamento(dist))
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[1]/button').click()

def search_bairro(bairro,cidade):
    driver.find_element_by_xpath(
        '/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input').send_keys(
        bairro + ', ' + cidade)
    driver.find_element_by_xpath(
        '/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div/input').send_keys(
        "IFPB Campina Grande")
    time.sleep(10)
    try:
        driver.find_element_by_xpath(
            '/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/button[1]').click()
    except:
        driver.find_element_by_xpath(
            '/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]').click()
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="section-directions-trip-details-msg-0"]').click()
    time.sleep(5)
    dist = driver.find_element_by_xpath(
        '/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[3]/div[1]/h1/span[1]/span[2]/span').text
    print(str(i + 2) + " - SEM CEP - " + dist + " - CG")
    writefile(coluna + str(i + 2), tratamento(dist))
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[1]/button').click()

def erro(bairro,logradouro,cidade):
    driver.find_element_by_xpath(
        '/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input').send_keys(
        Keys.CONTROL, 'a')
    driver.find_element_by_xpath(
        '/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input').send_keys(
        Keys.BACKSPACE)
    if cep == '-':
        print("Logradouro não encontrado")
        try:
            search_bairro(bairro, cidade)
        except:
            print("Bairro não encontrado")
            writefile(coluna + str(i + 2), "-")
    else:
        try:
            print("Cep não encontrado")
            n_tem_cep(logradouro, cidade)
        except:
            print("Logradouro não encontrado")
            driver.find_element_by_xpath(
                '/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input').send_keys(
                Keys.CONTROL, 'a')
            driver.find_element_by_xpath(
                '/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input').send_keys(
                Keys.BACKSPACE)
            try:
                search_bairro(bairro, cidade)
            except:
                print("Bairro não encontrado")
                writefile(coluna + str(i + 2), "-")


def tratamento(text):
    aux = text.split()
    try:
        saida = aux[0].replace(",",".")
    except:
        saida = aux[0]

    return saida

infos = get_infos()

driver = webdriver.Firefox(executable_path='Caminho no seu PC/SearchDistance/geckodriver')
driver.get("https://www.google.com.br/maps")
time.sleep(10)
driver.find_element_by_xpath('//*[@id="searchbox-directions"]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]/div[1]/button/img').click()

for i in range(len(infos)):

    logradouro = str(infos[i]['Logradouro'])
    bairro = str(infos[i]['Bairro'])
    cep = str(infos[i]['CEP'])
    cidade = str(infos[i]['Cidade'])
    time.sleep(5)

    if cidade=="Campina Grande - PB":
        try:
            if cep == '-':
                n_tem_cep(logradouro,cidade)

            else:
                tem_cep(cep)
        except:
            erro(bairro,logradouro,cidade)

    else:
        try:
            if cep == '-':
                n_tem_cep(logradouro,cidade)

            else:
                tem_cep(cep)
        except:
            erro(bairro,logradouro,cidade)

driver.quit()