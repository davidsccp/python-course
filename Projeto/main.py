
import pandas as pd
from src.data_clean import DataClean
from src.utils import create_db
from src.transform import calc_horas, classifica_turno
from sqlalchemy import create_engine

# 1. Carregar dados e metadados
df = pd.read_csv(
    "https://raw.githubusercontent.com/JackyP/testing/master/datasets/nycflights.csv",
    index_col=0)
metadata = pd.read_excel("assets/metadado.xlsx", index_col=None)

# Criar a coluna date_time a partir de year, month, day e dep_time
df['dep_time'] = df['dep_time'].apply(lambda x: f"{int(x):04d}" if not pd.isna(x) else "0000")
df['hour'] = df['dep_time'].str[:2].astype(int)
df['minute'] = df['dep_time'].str[2:].astype(int)
df['date_time'] = pd.to_datetime(df[['year', 'month', 'day', 'hour', 'minute']])

# 2. Limpeza de dados
cleaner = DataClean(df, metadata)
cleaner.select_cols()
cleaner.rename_cols()
cleaner.select_nnull_cols()
cleaner.select_nneg_cols()
cleaner.data_type()
df_limpo = cleaner.return_data()

# 3. Transformações adicionais
df_limpo['tempo_voo_horas'] = calc_horas(df_limpo['tempo_voo'])
df_limpo['turno'] = classifica_turno(df_limpo['data_hora'])

# 4. Conexão com banco de dados e criação da tabela
engine = create_engine("sqlite:///meu_banco.db")
create_db(engine)

# 5. Inserção no banco
df_limpo.to_sql('flights', con=engine, if_exists='replace', index=False)

print("Pipeline finalizada com sucesso.")
