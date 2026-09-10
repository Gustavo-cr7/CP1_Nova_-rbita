from kit_dados import modulos
from kit_dados import leituras_ambientais


limites_o2 = (19.5, 23.5)
limites_temp = (18.0, 27.0)
limites_pressao = (95.0, 105.0)
limite_co2 = 1000


def buscar_modulo(id_modulo):
    for modulo in modulos:
        if modulo["id"] == id_modulo:
            return modulo

    return None


def classificar_cenario(o2, co2, temperatura, pressao):
    problemas = 0

    if o2 < limites_o2[0] or o2 > limites_o2[1]:
        problemas = problemas + 1

    if co2 > limite_co2:
        problemas = problemas + 1

    if temperatura < limites_temp[0] or temperatura > limites_temp[1]:
        problemas = problemas + 1

    if pressao < limites_pressao[0] or pressao > limites_pressao[1]:
        problemas = problemas + 1

    if problemas == 0:
        return "NORMAL"

    if problemas == 1:
        return "ATENCAO"

    return "CRITICO"


ultima_leitura = leituras_ambientais[-1]

print("NOVA ORBITA")
print("SIMULADOR DE SEGURANCA AMBIENTAL")
print()
print("MODULOS DISPONIVEIS")

for modulo in modulos:
    print(modulo["id"], modulo["nome"])

print()

id_modulo = input("DIGITE O ID DO MODULO ")
novos_astronautas = int(input("DIGITE A QUANTIDADE DE NOVOS ASTRONAUTAS "))
ventilacao = input("A VENTILACAO ESTA FUNCIONANDO DIGITE SIM OU NAO ").upper()

modulo_escolhido = buscar_modulo(id_modulo.upper())

if modulo_escolhido is None:
    print()
    print("MODULO NAO ENCONTRADO")
else:
    nova_ocupacao = modulo_escolhido["ocupacao"] + novos_astronautas

    o2_simulado = ultima_leitura["o2_pct"] - novos_astronautas * 0.2
    co2_simulado = ultima_leitura["co2_ppm"] + novos_astronautas * 120
    temp_simulada = ultima_leitura["temp_c"]
    pressao_simulada = ultima_leitura["pressao_kpa"]

    if ventilacao == "NAO":
        o2_simulado = o2_simulado - 0.5
        co2_simulado = co2_simulado + 400
        temp_simulada = temp_simulada + 2

    status = classificar_cenario(
        o2_simulado,
        co2_simulado,
        temp_simulada,
        pressao_simulada
    )

    print()
    print("RESULTADO DA SIMULACAO")
    print()
    print("MODULO", modulo_escolhido["nome"])
    print("CAPACIDADE", modulo_escolhido["capacidade"])
    print("OCUPACAO ATUAL", modulo_escolhido["ocupacao"])
    print("NOVA OCUPACAO", nova_ocupacao)
    print()
    print("O2 SIMULADO", round(o2_simulado, 2))
    print("CO2 SIMULADO", round(co2_simulado, 2))
    print("TEMPERATURA SIMULADA", round(temp_simulada, 2))
    print("PRESSAO SIMULADA", round(pressao_simulada, 2))
    print()

    if nova_ocupacao > modulo_escolhido["capacidade"]:
        print("STATUS CRITICO")
        print("RECOMENDACAO")
        print("ENTRADA DE NOVOS ASTRONAUTAS NAO RECOMENDADA")
    elif status == "NORMAL":
        print("STATUS NORMAL")
        print("RECOMENDACAO")
        print("ENTRADA DE NOVOS ASTRONAUTAS AUTORIZADA")
    elif status == "ATENCAO":
        print("STATUS ATENCAO")
        print("RECOMENDACAO")
        print("ENTRADA AUTORIZADA COM MONITORAMENTO")
    else:
        print("STATUS CRITICO")
        print("RECOMENDACAO")
        print("ENTRADA DE NOVOS ASTRONAUTAS NAO RECOMENDADA")
