from pathlib import Path
from config_upload_csv_to_db import user, password, host, port, database
import pandas as pd
from data_field import DFModel
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.pool import NullPool

DB_URL = f'postgresql+psycopg2://{user}:{password}@{host}/{database}'


def read_data_from_scv(filepath: Path) -> pd.DataFrame:
    df = pd.read_csv(filepath, sep=',')
    return df.drop(df.columns[0], axis=1)


def load_df_to_db(dataframe: pd.DataFrame, frame_name: str, engine: Engine) -> None:
    try:
        dataframe.to_sql(
            frame_name,
            con=engine,
            if_exists='replace',
            index=False,
            dtype=DFModel.fields)
        print(f'Данные из файла "{frame_name}" успешно загружены в базу данных')
    except:
        print(f'Ошибка вставки данных из {frame_name} в базу данных')


def main():
    engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}/{database}', poolclass=NullPool)
    events_path = Path('events.csv')
    installs_path = Path('installs1.csv')
    events_df = read_data_from_scv(events_path)
    installs_df = read_data_from_scv(installs_path)
    load_df_to_db(events_df, 'events', engine)
    load_df_to_db(installs_df, 'installs1', engine)


if __name__ == '__main__':
    main()
