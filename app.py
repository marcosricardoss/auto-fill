import csv    

def app():
    # Abra o arquivo CSV para leitura
    with open('data.csv', 'r') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        # Itere pelas linhas do arquivo CSV e imprima os dados de cada linha
        for linha in leitor_csv:            
            print(f'{linha["City"]} - {linha["State"]}')            

if __name__ == "__main__":
    app()