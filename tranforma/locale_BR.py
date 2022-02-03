import re
import json

with open("estados", encoding='utf-8') as file:
    estados = json.load(file)

with open("municipios", encoding='utf-8') as file:
    municipios = json.load(file)


with open("duplicados.json", encoding='utf-8') as file:
    duplicados = json.load(file)


lista_locais= []


for municipio in municipios:
    if not municipio['nome'] in [duplicado['name'] for duplicado in duplicados]:
        cada_estado = [estado['nome'] for estado in estados if municipio["codigo_uf"] == estado["codigo_uf"]]
        estado_uf = [estado['uf'] for estado in estados if municipio["codigo_uf"] == estado["codigo_uf"]]
        cada_estado = cada_estado[0]
        estado_uf = estado_uf[0]
        lista_locais.append({"codigo_ibge": municipio["codigo_ibge"], "municipio": municipio["nome"],
                        "latitude": municipio["latitude"], "longitude": municipio["longitude"], "estado": cada_estado,
                       "uf": estado_uf, "nation": "BR"})

with open('../locale_BR.json', 'w', encoding='utf-8') as output:
    json.dump(lista_locais, output, ensure_ascii=False, indent=4)
