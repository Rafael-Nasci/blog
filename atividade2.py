import requests



API_BASE = "http://api.olhovivo.sptrans.com.br/v2.1"
API_TOKEN = "" 
CODIGO_LINHA = 8750 


print(" Autenticando na API SPTrans...")

session = requests.Session()
login_url = f"{API_BASE}/Login/Autenticar?token={API_TOKEN}"

login_response = session.post(login_url)

if login_response.text.lower() != "true":
    raise Exception(" Erro ao autenticar na API. Verifique seu token.")

print(" Autenticado com sucesso!")



print(" Buscando paradas da linha...")

paradas_url = f"{API_BASE}/Parada/BuscarParadasPorLinha?codigoLinha={CODIGO_LINHA}"
paradas_response = session.get(paradas_url)

dados_paradas = paradas_response.json()

print(f"Encontrado {len(dados_paradas)} pontos de ônibus:")
for p in dados_paradas:
    print(f"- {p['np']} | {p['ed']} | Lat: {p['py']} Long: {p['px']}")
