import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/genshin_weapons_v6.csv')
print(df["base_atk"].count())
print(df["base_atk"].mean())
print(df["base_atk"].value_counts())

plt.figure(figsize=(10, 6))  # Define o tamanho da figura
plt.hist(df["base_atk"].dropna(), bins=20, color='skyblue', edgecolor='black')  # Histograma
plt.title('Distribuição do Base ATK')  # Título
plt.xlabel('Base ATK')  # Rótulo do eixo X
plt.ylabel('Frequência')  # Rótulo do eixo Y
plt.grid(True)
plt.show()



def showVariableInfo(pd_variable):
    global df

    var = df[pd_variable]

    mean_var = var.mean()
    median_var = var.median()
    mode_var = var.mode()[0]
    std_var = var.std()

    # Imprimir os resultados
    print(f"Variable 1 - Mean: {mean_var}, Median: {median_var}, Mode: {mode_var}, Std Dev: {std_var}")