import time
# try:
#     a = 1200 / 0
# except ZeroDivisionError:
#     print("Nada é divisivel por 0")

# try:
#     a = 1200 / 0
# except:
#     print("Nada é divisivel por 0")

# try:
#     a = 1200 / 0
# except Exception as error:
#
#     print("Ocorre um erro ao realizar a solicitação: ", error)

def abre_arquivo():
    try:
        arquivo = open('arquivo2.txt')
        return True
    except Exception as err:
        print("Aconteceu algum erro: ", err)
        return False

while not abre_arquivo():
    abre_arquivo()
    print("Tentando abrir arquivo")
    time.sleep(5)

print('Finalmente Abriu o Arquivo')