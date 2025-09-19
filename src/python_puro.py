from csv import reader
from collections import defaultdict, Counter
from tqdm import tqdm
import time 
#Não recomendo o teste vai demorar em media 20 minutos
QTD_LINHAS = 100_000

def processar_temperaturas(path_do_csv):
    minimas = defaultdict(lambda:float('inf'))
    maximas = defaultdict(lambda:float('-inf'))
    somas = defaultdict(float)
    medicoes = Counter()

    with open(path_do_csv, 'r', encoding='utf-8') as a:
        _reader = reader(a, delimiter=';')
        # usando tqdm diretamente no iterador, isso mostrará a porcentagem de conclusão.
        for row in tqdm(_reader, total=QTD_LINHAS, desc="Paciencia...\n"):
            nome_da_station, temperatura = str(row[0]), float(row[1])
            medicoes.update = ([nome_da_station])
            minimas[nome_da_station] = min(minimas[nome_da_station], temperatura)
            maximas[nome_da_station] = max(maximas[nome_da_station], temperatura)
            somas[nome_da_station] += temperatura

    print("Carregamento concluido...")

    results = {}
    for station, qtd_medicoes in medicoes.items():
        media_temp = somas[station] / qtd_medicoes
        results[station] = (minimas[station], maximas[station], media_temp)
    
    ordenado = dict(sorted(results.items()))

    formatado = {station: f"{min_temp} / {md_temp} / {max_temp}" for station, (min_temp, md_temp, max_temp) in ordenado.items()}

    return formatado

if __name__ == "__main__":
    path_do_csv = "data/measurements.txt"

    print("Iniciado o precessamento do arquivo")
    start_time = time.time()

    resultados = processar_temperaturas(path_do_csv)

    end_time = time.time()

    for station, metrics in resultados.items():
        print(station, metrics, sep=': ')

    print(f"conclusão em: {start_time - end_time:.2f}")