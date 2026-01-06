"""
Autore: [Il tuo nome]
Data: Ottobre 2025
Descrizione: Simulazione di un processo produttivo nel settore secondario.
Obiettivo: generare dati casuali su tempi e quantità produttive
           e creare un report CSV finale.
"""



import random
import pandas as pd
from datetime import datetime

# ==============================
# CONFIGURAZIONE DI BASE
# ==============================

# Funzione per generare casualmente i parametri dei prodotti
def genera_prodotti(num_prodotti=3):
    """Genera prodotti con parametri casuali (tempo unitario e capacità giornaliera)."""
    prodotti = {}
    for i in range(1, num_prodotti + 1):
        nome = f"Prodotto_{i}"
        tempo_unitario = round(random.uniform(2.0, 10.0), 2)  # minuti per unità
        capacita_giornaliera = random.randint(100, 400)
        prodotti[nome] = {
            "tempo_unitario": tempo_unitario,
            "capacita_giornaliera": capacita_giornaliera
        }
    return prodotti


# Funzione per generare casualmente le quantità da produrre per ogni prodotto
def genera_quantita(prodotti):
    """Genera quantità casuali rispettando la capacità giornaliera."""
    quantita = {}
    for nome, info in prodotti.items():
        qta = random.randint(50, info["capacita_giornaliera"])
        quantita[nome] = qta
    return quantita


# Funzione per simulare la produzione giornaliera
def simula_produzione_giornaliera(prodotti, giorno):
    """Simula un giorno di produzione e restituisce i risultati in lista di dizionari."""
    quantita = genera_quantita(prodotti)
    risultati = []

    for nome, qta in quantita.items():
        tempo_unitario = prodotti[nome]["tempo_unitario"]
        tempo_totale = round(tempo_unitario * qta, 2)
        risultati.append({
            "Giorno": giorno,
            "Prodotto": nome,
            "Quantità prodotta": qta,
            "Tempo unitario (min)": tempo_unitario,
            "Tempo totale (min)": tempo_totale
        })
    return risultati


# Funzione per creare un report finale sicuro 
def genera_report(risultati):
    """Crea un report Pandas e aggiunge la riga Totale in modo sicuro."""
    df = pd.DataFrame(risultati)

    # Calcolo dei totali
    totale_quantita = df["Quantità prodotta"].sum()
    totale_tempo = df["Tempo totale (min)"].sum()

    # Riga dei totali
    totale_row = {
        "Giorno": "—",
        "Prodotto": "Totale",
        "Quantità prodotta": totale_quantita,
        "Tempo unitario (min)": "—",
        "Tempo totale (min)": totale_tempo
    }

    # Concatenazione 
    df = pd.concat([df, pd.DataFrame([totale_row])], ignore_index=True)
    return df


# ==============================
# SIMULAZIONE PRINCIPALE
# ==============================

def simula_processi(num_giorni=5):
    print("=== SIMULAZIONE PROCESSO PRODUTTIVO ===\n")

    #  Generazione casuale dei prodotti e dei loro parametri
    prodotti = genera_prodotti()
    print("Parametri generati per ciascun prodotto:\n")
    for nome, p in prodotti.items():
        print(f"- {nome}: tempo unitario = {p['tempo_unitario']} min, capacità giornaliera = {p['capacita_giornaliera']} unità")
    print("\n-------------------------------------------\n")

    #  Simulazione per più giorni
    risultati_complessivi = []
    for giorno in range(1, num_giorni + 1):
        print(f"Giorno {giorno} in corso...")
        risultati_giorno = simula_produzione_giornaliera(prodotti, giorno)
        risultati_complessivi.extend(risultati_giorno)

    #  Generazione del report finale
    report_finale = genera_report(risultati_complessivi)

    #  Salvataggio su file CSV
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"report_produzione_{timestamp}.csv"
    report_finale.to_csv(file_name, index=False, sep=";")

    #  Output a video
    print("\n Simulazione completata con successo!")
    print(f" Report salvato come: {file_name}\n")
    print(report_finale)

    # Restituisce il tempo complessivo dell’intero lotto
    tempo_totale = report_finale.iloc[-1]["Tempo totale (min)"]
    print(f"\n⏱ Tempo di produzione complessivo dell’intero lotto: {tempo_totale} minuti")

    return report_finale


# ==============================
# ESECUZIONE
# ==============================
if __name__ == "__main__":
    simula_processi()

