import duckdb
import time 

def select():
    duckdb.sql(""" 
            SELECT 
                ESTACAO,
                MIN(TEMPERATURA) AS MIN_TEMPERATURA,
                AVG(TEMPERATURA) :: DECIMAL(3,1) AS MEDIA_TEMPERATURA,
                MAX(TEMPERATURA) AS MAX_TEMPERATURA
            FROM read_csv("data/measurements.txt", 
                           AUTO_DETECT=FALSE, 
                           sep=';', 
                           columns={'ESTACAO': VARCHAR, 'TEMPERATURA': 'DECIMAL(3,1)'}
                         )
            GROUP BY ESTACAO
            ORDER BY ESTACAO
               """).show()
    

if __name__ == "__main__":
    tempo_ini = time.time()
    select()
    tempo_total = time.time() - tempo_ini
    print(f"Tempo do Duckdb: {tempo_total:.2f} sec")