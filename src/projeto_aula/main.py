from projeto_aula.fatos import buscar_fato_aleatorio
from projeto_aula.sistema import obter_informacoes_sistema

def main():
    fato = buscar_fato_aleatorio()  
    info = obter_informacoes_sistema()
    resultado = {"fato": fato, **info}
    print(resultado)


if __name__ == "__main__":
    main()
