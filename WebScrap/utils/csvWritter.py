import pandas as pd

def guardaCsv(datos, archivo="resultados.csv"):
    df = pd.DataFrame(datos)
    df.to_csv("resultados.csv", index=False)