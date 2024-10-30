from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praca', 'Gourmet')
restaurante_praca.receber_avaliacao('Leo', '10')
restaurante_praca.receber_avaliacao('Ana', '5')

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()