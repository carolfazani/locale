import pycountry
import pandas as pd



def countries():
    countries = pd.DataFrame()
    data = []
    for country in pycountry.countries:
        try:
            current = {'alpha_2': country.alpha_2,
                        'name': country.name,
                        'official_name': country.official_name}
        except Exception as ex:
            current = {'alpha_2': country.alpha_2,
                        'name': country.name,
                        'official_name': None}
        data.append(current)

    countries = pd.DataFrame(data, columns = ['alpha_2', 'name', 'official_name'])
    return  countries

lista = pd.read_csv('todos_paises.csv', dtype={"teste": str})


#tradução e tranformação do todos_paises.csv em json feita em um site