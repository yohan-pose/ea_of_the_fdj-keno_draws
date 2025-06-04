import marimo

__generated_with = "0.13.6"
app = marimo.App(width="medium")


@app.cell
def _():
    # -*- coding: utf-8 -*-
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns
    from sklearn.linear_model import LinearRegression

    # Entrée : "2020-10_to_2025-06_keno_df_clean.csv"
    # Description : On effectue une analyse exploratroire du DataFrame entrant
    return pd, plt


@app.cell
def _(pd):
    df = pd.read_csv("2020-10_to_2025-06_keno_df_clean.csv", sep=";")
    df
    return (df,)


@app.cell
def _(df, pd):
    # Reclassification des types des colonnes datetime du DF
    # print(df.dtypes)
    df['date_de_tirage'] = pd.to_datetime(df['date_de_tirage'], format="%d/%m/%Y")

    # Liste des colonnes à exclure de l'analyse numérique
    col_not_num_a_exclure = [
        'date_de_tirage',
        'heure_de_tirage',
        'numero_jokerplus'
    ]

    col_num = df.select_dtypes(include='number').columns
    col_utils = [col for col in col_num if col not in col_not_num_a_exclure]
    return (col_utils,)


@app.cell
def _(col_utils, df):
    eda_df=df[col_utils].describe()
    eda_df
    return


@app.cell
def _(df, pd):
    # Rassembler tous les numéros tirés dans une seule série
    boules = pd.concat([df[f'boule{i}'] for i in range(1, 21)])

    # Compter la fréquence de chaque numéro
    frequence_boules = boules.value_counts().sort_index()
    couleurs_freq_boules = ['#838eff' if count > 995 else '#83bcff' for count in frequence_boules]
    return couleurs_freq_boules, frequence_boules


@app.cell
def _(couleurs_freq_boules, frequence_boules, plt):
    ## Tracé du graphique
    plt.figure(figsize=(12, 5))
    frequence_boules.plot(kind='bar', color=couleurs_freq_boules)
    plt.title("Fréquence des numéros tirées")
    plt.xlabel("Numéro")
    plt.ylabel("Nombre d'apparitions")
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
