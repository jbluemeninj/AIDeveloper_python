import pandas as pd

serie_1 = pd.Series([1, 2, 3, 4, 5])

#DataFrame
data = {'Nombre': ['Ana', 'Juan', 'Luis'],
        'Edad': [25, 30, 35],
        'Ciudad': ['Madrid', 'Barcelona', 'Valencia']}
df = pd.DataFrame(data)
df['Salario'] = [30000, 35000, None]
#df.drop('Salario', axis=1, inplace=True)

#print(df[df['Edad'] > 30])
#print(df.isnull())
df.fillna(0, inplace=True)
df.dropna(inplace=True)

def incrementar_edad(edad):
    return edad + 1

df['Edad'] = df['Edad'].apply(incrementar_edad)
print(df)