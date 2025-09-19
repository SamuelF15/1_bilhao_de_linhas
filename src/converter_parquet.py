import duckdb

print("Iniciando a conversão do arquivo CSV para Parquet...")
# Comando para converter o arquivo CSV para Parquet
duckdb.sql("""
    COPY (
        SELECT 
            ESTACAO, 
            TEMPERATURA::DECIMAL(3,1) AS TEMPERATURA 
        FROM read_csv(
            'data/measurements.txt', 
            AUTO_DETECT=FALSE, 
            sep=';', 
            columns={'ESTACAO': VARCHAR, 'TEMPERATURA': VARCHAR}
        )
    ) TO 'data/measurements.parquet' (FORMAT 'parquet');
""")

print("Conversão concluída. O arquivo measurements.parquet foi criado.")