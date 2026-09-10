# KIT DE DADOS — RESIDENCIA E BASE
# Bases para projetos de habitat, capacidade, suporte a vida e distribuicao de tripulacao.

modulos = [
    {"id": "HB-01", "nome": "Habitat Alpha", "capacidade": 6, "ocupacao": 4, "energia_kw": 18},
    {"id": "HB-02", "nome": "Laboratorio", "capacidade": 4, "ocupacao": 3, "energia_kw": 15},
    {"id": "HB-03", "nome": "Dormitorio", "capacidade": 8, "ocupacao": 6, "energia_kw": 14},
    {"id": "HB-04", "nome": "Modulo Medico", "capacidade": 3, "ocupacao": 1, "energia_kw": 12},
    {"id": "HB-05", "nome": "Modulo Reserva", "capacidade": 5, "ocupacao": 0, "energia_kw": 9},
    {"id": "HB-06", "nome": "Comunicacoes", "capacidade": 2, "ocupacao": 1, "energia_kw": 11}
]

leituras_ambientais = [
    {"ciclo": 1, "modulo": "HB-01", "o2_pct": 20.8, "co2_ppm": 690, "temp_c": 22.4, "pressao_kpa": 101.1, "umidade_pct": 42},
    {"ciclo": 2, "modulo": "HB-01", "o2_pct": 20.7, "co2_ppm": 720, "temp_c": 22.8, "pressao_kpa": 101.0, "umidade_pct": 43},
    {"ciclo": 3, "modulo": "HB-01", "o2_pct": 20.6, "co2_ppm": 810, "temp_c": 23.0, "pressao_kpa": 100.9, "umidade_pct": 44},
    {"ciclo": 4, "modulo": "HB-01", "o2_pct": 20.5, "co2_ppm": 890, "temp_c": 23.4, "pressao_kpa": 100.7, "umidade_pct": 45},
    {"ciclo": 5, "modulo": "HB-01", "o2_pct": 20.4, "co2_ppm": 960, "temp_c": 23.8, "pressao_kpa": 100.5, "umidade_pct": 46},
    {"ciclo": 6, "modulo": "HB-01", "o2_pct": 20.3, "co2_ppm": 1080, "temp_c": 24.1, "pressao_kpa": 100.2, "umidade_pct": 47}
]

tripulacao = [
    {"id": "TR-01", "funcao": "Comandante", "modulo": "HB-01", "turno": "A"},
    {"id": "TR-02", "funcao": "Engenheira", "modulo": "HB-01", "turno": "A"},
    {"id": "TR-03", "funcao": "Geologo", "modulo": "HB-02", "turno": "B"},
    {"id": "TR-04", "funcao": "Medica", "modulo": "HB-04", "turno": "A"},
    {"id": "TR-05", "funcao": "Tecnico", "modulo": "HB-03", "turno": "B"},
    {"id": "TR-06", "funcao": "Pesquisadora", "modulo": "HB-02", "turno": "B"}
]

consumo_modulos = [
    {"modulo": "HB-01", "agua_l_dia": 52, "energia_kwh_dia": 410},
    {"modulo": "HB-02", "agua_l_dia": 31, "energia_kwh_dia": 360},
    {"modulo": "HB-03", "agua_l_dia": 68, "energia_kwh_dia": 330},
    {"modulo": "HB-04", "agua_l_dia": 18, "energia_kwh_dia": 290},
    {"modulo": "HB-05", "agua_l_dia": 7, "energia_kwh_dia": 145},
    {"modulo": "HB-06", "agua_l_dia": 5, "energia_kwh_dia": 180}
]

# 0 = livre | 1 = ocupado | 2 = acesso restrito
mapa_base = [
    [1, 1, 0, 0, 2, 2],
    [1, 1, 1, 0, 0, 2],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 0],
    [2, 0, 0, 1, 1, 1],
    [2, 2, 0, 0, 1, 1]
]

# Referencias NASA para o ambiente lunar.
ambiente_lunar = {
    "gravidade_relativa_terra": 1 / 6,
    "temperatura_sol_c": 127,
    "temperatura_escuridao_c": -173
}

# Referencia historica NASA: permanencia e atividade extraveicular nas missoes Apollo.
historico_apollo_superficie = [
    {"missao": "Apollo 11", "horas_superficie": 21.5, "numero_evas": 1, "horas_eva": 2.5},
    {"missao": "Apollo 12", "horas_superficie": 31.5, "numero_evas": 2, "horas_eva": 7.8},
    {"missao": "Apollo 14", "horas_superficie": 33.5, "numero_evas": 2, "horas_eva": 9.4},
    {"missao": "Apollo 15", "horas_superficie": 67.0, "numero_evas": 3, "horas_eva": 19.1},
    {"missao": "Apollo 16", "horas_superficie": 71.0, "numero_evas": 3, "horas_eva": 20.2},
    {"missao": "Apollo 17", "horas_superficie": 75.0, "numero_evas": 3, "horas_eva": 22.1}
]
