from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('Praca', 'Gourmet')
bebida_suco = Bebida("Suco de Melancia", 5.0 , "grande")
prato_pao =  Prato("Pao Frances", 0.80, "Pao frances amanteigado") 
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_pao)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == "__main__":
    main()