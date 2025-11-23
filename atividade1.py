import requests
import pandas as pd
import plotly.express as px
from datetime import datetime
import calendar

def dolar_por_periodo(mmyyyy):
    first_date = datetime.strptime(mmyyyy, "%m%Y")
    last_day = calendar.monthrange(first_date.year, first_date.month)[1]
    last_date = first_date.replace(day=last_day)

    data_inicial = first_date.strftime("%m-%d-%Y")
    data_final = last_date.strftime("%m-%d-%Y")

    url = (
        f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
        f"CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)"
        f"?@dataInicial='{data_inicial}'&@dataFinalCotacao='{data_final}'&$top=1000&$format=json"
    )

    r = requests.get(url)
    dados = r.json()["value"]

    df = pd.DataFrame(dados)
    df['dataHoraCotacao'] = pd.to_datetime(df['dataHoraCotacao'])
    df = df.sort_values("dataHoraCotacao")

    df = df.set_index("dataHoraCotacao").resample("D").ffill()

    fig = px.line(
        df,
        y="cotacaoCompra",
        title=f"Cotação do Dólar — {mmyyyy[:2]}/{mmyyyy[2:]}",
        labels={"cotacaoCompra": "Cotação (R$)"}
    )
    fig.show()

    return df

if __name__ == "__main__":
    dolar_por_periodo("082021")
