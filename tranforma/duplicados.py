import pandas as pd
from tabula.io import read_pdf
import pycountry

def muni_duplicados():
    path = r"indice.pdf"
    #Tranforma o PDF em DataFrame
    df = read_pdf(path, pages = 'all')
    #coloca a primeira linha como titulo de coluna
    df[0]= df[0].rename(columns=df[0].iloc[0]).drop(df[0].index[0])
    df = pd.concat(df)
    #ordena os valores por nome
    df.sort_values("NOME DO MUNICÍPIO", inplace = True)
    df["NOME DO MUNICÍPIO"] = (df["NOME DO MUNICÍPIO"].replace("'", ' ', regex=True)).astype(str)
    #reseta o index
    df.reset_index(inplace = True)
    #tira colunas e linhas desnecessárias
    df = df.drop(columns=['index'])
    df = df.drop(columns=['Unnamed: 0'])
    df = df.dropna(axis=0, how='all')
    #ve quais nomes se repetem
    dupli = df.duplicated('NOME DO MUNICÍPIO', keep =False)
    #adiciona a coluna "duplicated"
    df = pd.concat([dupli, df], axis=1)
    df = df.set_axis(['duplicated', 'uf', 'coduf', 'codmun', 'name', 'população'], axis='columns')

    #pesquisa nomes de cidade que contém nomes de estados
    Rondonia= df.loc[df['name'].str.contains('Alagoas', case=False)]
    Acre= df.loc[df['name'].str.contains('Acre', case=False)]
    Amazonas= df.loc[df['name'].str.contains('Amazonas', case=False)]
    Roraima= df.loc[df['name'].str.contains('Roraima', case=False)]
    Para= df.loc[df['name'].str.contains('Pará', case=False)]
    Amapa= df.loc[df['name'].str.contains('Amapá', case=False)]
    Tocantins= df.loc[df['name'].str.contains('Tocantins', case=False)]
    Maranhao= df.loc[df['name'].str.contains('Maranhão', case=False)]
    Piaui= df.loc[df['name'].str.contains('Piauí', case=False)]
    Ceara= df.loc[df['name'].str.contains('Ceará', case=False)]
    RioGrandedoNorte= df.loc[df['name'].str.contains('Rio Grande do Norte', case=False)]
    Paraiba= df.loc[df['name'].str.contains('Paraíba', case=False)]
    Pernambuco= df.loc[df['name'].str.contains('Pernanbuco', case=False)]
    Alagoas= df.loc[df['name'].str.contains('Alagoas', case=False)]
    Sergipe= df.loc[df['name'].str.contains('Sergipe', case=False)]
    Bahia= df.loc[df['name'].str.contains('Bahia', case=False)]
    MinasGerais= df.loc[df['name'].str.contains('Minas Gerais', case=False)]
    EspiritoSanto= df.loc[df['name'].str.contains('Espirito Santo', case=False)]
    RiodeJaneiro= df.loc[df['name'].str.contains('Rio de Janeiro', case=False)]
    SaoPaulo= df.loc[df['name'].str.contains('São Paulo', case=False)]
    Parana= df.loc[df['name'].str.contains('Paraná', case=False)]
    SantaCatarina= df.loc[df['name'].str.contains('Santa Catarina', case=False)]
    RioGrandedoSul= df.loc[df['name'].str.contains('Rio Grande do Sul', case=False)]
    MatoGrossodoSul= df.loc[df['name'].str.contains('Mato Grosso do Sul', case=False)]
    MatoGrosso= df.loc[df['name'].str.contains('Mato Grosso', case=False)]
    Goias= df.loc[df['name'].str.contains('Goías', case=False)]
    DistritoFederal= df.loc[df['name'].str.contains('Distrito Federal', case=False)]


    #tranforma em uma tabela só
    df2 = pd.concat([Rondonia, Acre, Amazonas, Roraima, Para, Amapa, Tocantins, Maranhao, Piaui, Ceara, RioGrandedoNorte,
                   Paraiba, Pernambuco, Alagoas, Sergipe, Bahia, MinasGerais, EspiritoSanto, RiodeJaneiro, SaoPaulo, Parana,
                   SantaCatarina, MatoGrossodoSul, MatoGrosso, Goias, DistritoFederal])

    df2['duplicated'] = 'True'

    #Une as duas tabelas. Aqui tudo que tem True é porque o nome se repete
    df.loc[df2.index] = df2

    #Pega todos false e gera uma lista
    df3= df[df['duplicated'] == False]

    #Pega todos True e gera uma lista
    df4= df[df['duplicated'] == True]
    dupli = df4.to_csv('duplicados.csv', sep='\t', encoding='utf-8')
    return print(df4)


#tive que tranformar pra csv e dps pra json, pois tranformando pra json direto o enconding não funciona.

if __name__ == "__main__":
   muni_duplicados()

