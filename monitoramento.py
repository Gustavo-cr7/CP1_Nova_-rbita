from kit_dados import modulos
from kit_dados import leituras_ambientais
from kit_dados import mapa_base


limites_o2 = (19.5, 23.5)
limites_temp = (18.0, 27.0)
limites_pressao = (95.0, 105.0)
limite_co2 = 1000


def calcular_media(valores):
    total = 0

    for valor in valores:
        total = total + valor

    return total / len(valores)


def classificar_leitura(leitura):
    problemas = 0

    if leitura["o2_pct"] < limites_o2[0] or leitura["o2_pct"] > limites_o2[1]:
        problemas = problemas + 1

    if leitura["co2_ppm"] > limite_co2:
        problemas = problemas + 1

    if leitura["temp_c"] < limites_temp[0] or leitura["temp_c"] > limites_temp[1]:
        problemas = problemas + 1

    if leitura["pressao_kpa"] < limites_pressao[0] or leitura["pressao_kpa"] > limites_pressao[1]:
        problemas = problemas + 1

    if problemas == 0:
        return "NORMAL"

    if problemas == 1:
        return "ATENCAO"

    return "CRITICO"


def contar_areas_mapa(mapa):
    livres = 0
    ocupadas = 0
    restritas = 0

    for linha in mapa:
        for area in linha:
            if area == 0:
                livres = livres + 1
            elif area == 1:
                ocupadas = ocupadas + 1
            else:
                restritas = restritas + 1

    return livres, ocupadas, restritas


valores_o2 = []
valores_co2 = []
valores_temp = []

for leitura in leituras_ambientais:
    valores_o2.append(leitura["o2_pct"])
    valores_co2.append(leitura["co2_ppm"])
    valores_temp.append(leitura["temp_c"])


media_o2 = calcular_media(valores_o2)
media_co2 = calcular_media(valores_co2)
media_temp = calcular_media(valores_temp)
maior_co2 = max(valores_co2)

ultima_leitura = leituras_ambientais[-1]
status_atual = classificar_leitura(ultima_leitura)

capacidade_total = 0
ocupacao_total = 0

for modulo in modulos:
    capacidade_total = capacidade_total + modulo["capacidade"]
    ocupacao_total = ocupacao_total + modulo["ocupacao"]

vagas_total = capacidade_total - ocupacao_total

livres, ocupadas, restritas = contar_areas_mapa(mapa_base)


print("NOVA ORBITA")
print("SEGURANCA AMBIENTAL DA BASE")
print()
print("MODULO MONITORADO", ultima_leitura["modulo"])
print()
print("MEDIA O2", round(media_o2, 2))
print("MEDIA CO2", round(media_co2, 2))
print("MEDIA TEMPERATURA", round(media_temp, 2))
print("MAIOR CO2", maior_co2)
print()
print("O2 ATUAL", ultima_leitura["o2_pct"])
print("CO2 ATUAL", ultima_leitura["co2_ppm"])
print("TEMPERATURA ATUAL", ultima_leitura["temp_c"])
print("PRESSAO ATUAL", ultima_leitura["pressao_kpa"])
print()
print("STATUS", status_atual)
print()
print("CAPACIDADE TOTAL", capacidade_total)
print("OCUPACAO TOTAL", ocupacao_total)
print("VAGAS TOTAIS", vagas_total)
print()
print("AREAS LIVRES", livres)
print("AREAS OCUPADAS", ocupadas)
print("AREAS RESTRITAS", restritas)
print()

if status_atual == "NORMAL":
    print("RECOMENDACAO")
    print("MANTER O MONITORAMENTO NORMAL")
elif status_atual == "ATENCAO":
    print("RECOMENDACAO")
    print("VERIFICAR O SISTEMA DE SUPORTE A VIDA")
else:
    print("RECOMENDACAO")
    print("RETIRAR A TRIPULACAO E VERIFICAR O MODULO")
