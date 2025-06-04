import marimo

__generated_with = "0.13.6"
app = marimo.App(width="medium")


@app.cell
def _():
    # -*- coding: utf-8 -*-
    import marimo as mo
    import numpy as np
    import pandas as pd

    # Entrée : "2020-10_to_2025-06_keno_df_not_clean.csv"
    # Description : On effectue un nettoyage complet du DataFrame entrant
    # Sortie : "2020-10_to_2025-06_keno_df_clean.csv"
    return (pd,)


@app.cell
def _(pd):
    # Chargement du Dataframe
    df = pd.read_csv("2020-10_to_2025-06_keno_df_not_clean.csv", sep=";")
    df
    return (df,)


@app.cell
def _(df):
    # Identification des colonnes à supprimer ou nettoyer dans le Dataframe
    col_val_manquante = df.isnull().sum()
    col_val_manquante = col_val_manquante[col_val_manquante>0]

    col_val_manquante
    return


@app.cell
def _(df):
    col_a_suppr = ['annee_numero_de_tirage','devise','Unnamed: 27','date_de_forclusion']
    new_df = df.drop(columns=[col for col in col_a_suppr if col in df.columns])
    new_df
    return (new_df,)


@app.cell
def _(new_df):
    new_df.to_csv("2020-10_to_2025-06_keno_df_clean.csv", index=False, sep=';')
    return


if __name__ == "__main__":
    app.run()
