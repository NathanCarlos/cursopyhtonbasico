from veiculo import Veiculo
from carro import Carro
caminhao_azul = Veiculo('azul', 'ford', 8, 70)
print("Cor: ", caminhao_azul.cor)
print("Marca: ", caminhao_azul.marca)
print("Tanque: ", caminhao_azul.tanque)

carro_azul = Carro('vermelho', 'ford', 4, 35)
print(" ")
print("Cor: ", carro_azul.cor)
print("Marca: ", carro_azul.marca)
print("Tanque: ", carro_azul.tanque)
carro_azul.abastecer(35)
print("Tanque: ", carro_azul.tanque)
carro_azul.abastecer(35)

