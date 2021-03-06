from sqlalchemy import create_engine
import pandas as pd

if __name__ == '__main__':

    engine = create_engine('postgresql://postgres:Impossible2@localhost:5432/Aminer')
    conn = engine.connect()
    q = 'SELECT \"0\",\"1\",\"2\" FROM rt_df'
    res = conn.execute(q)

    rt_df = pd.DataFrame(res.fetchall())

    cascades = rt_df.groupby(0)

    all_times_fr = []

    for name,cascade in cascades:
        cascade[1].values.tolist()