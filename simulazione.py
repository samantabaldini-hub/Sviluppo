import random
import pandas as pd
from datetime import datetime

# =========================================================
# PARAMETRI GLOBALI SISTEMA
# =========================================================

TEMPO_LINEA = 480
NUM_PRODOTTI = 3
GIORNI = 5

# strategie possibili
STRATEGIA = "domanda"  
# opzioni: "tempo", "domanda", "bilanciata"


# =========================================================
# GENERAZIONE PRODOTTI
# =========================================================

def genera_prodotti(n):

    prodotti = {}

    for i in range(1, n + 1):
        prodotti[f"Prodotto_{i}"] = {
            "tempo_unitario": round(random.uniform(2, 10), 2),
            "capacita": random.randint(120, 400)
        }

    return prodotti


# =========================================================
# DOMANDA GIORNALIERA VARIABILE
# =========================================================

def genera_domanda(prodotti):

    domanda = {}

    for nome, dati in prodotti.items():
        domanda[nome] = random.randint(80, dati["capacita"])

    return domanda


# =========================================================
# LOGICA PRIORITÀ PRODUZIONE
# =========================================================

def ordina_prodotti(prodotti, domanda):

    if STRATEGIA == "tempo":
        return sorted(prodotti.items(), key=lambda x: x[1]["tempo_unitario"])

    if STRATEGIA == "domanda":
        return sorted(prodotti.items(), key=lambda x: domanda[x[0]], reverse=True)

    if STRATEGIA == "bilanciata":
        return sorted(prodotti.items(), key=lambda x: domanda[x[0]] / x[1]["tempo_unitario"], reverse=True)


# =========================================================
# SIMULAZIONE GIORNATA
# =========================================================

def simula_giorno(prodotti, giorno):

    tempo_residuo = TEMPO_LINEA
    domanda = genera_domanda(prodotti)

    risultati = []

    ordine = ordina_prodotti(prodotti, domanda)

    for nome, dati in ordine:

        tempo_unit = dati["tempo_unitario"]
        capacita = dati["capacita"]

        max_producibile = int(tempo_residuo / tempo_unit)
        quantita = min(domanda[nome], capacita, max_producibile)

        tempo_usato = quantita * tempo_unit
        tempo_residuo -= tempo_usato

        risultati.append({
            "Giorno": giorno,
            "Prodotto": nome,
            "Domanda": domanda[nome],
            "Prodotto realizzato": quantita,
            "Tempo unitario": tempo_unit,
            "Tempo utilizzato": round(tempo_usato,2),
            "Soddisfazione domanda %": round((quantita/domanda[nome])*100 if domanda[nome] else 0,2),
            "Tempo residuo linea": round(tempo_residuo,2)
        })

        if tempo_residuo <= 0:
            break

    return risultati


# =========================================================
# SIMULAZIONE COMPLETA
# =========================================================

def simulazione():

    print("\n=== SIMULAZIONE SISTEMA PRODUTTIVO ===\n")

    prodotti = genera_prodotti(NUM_PRODOTTI)

    print("CONFIGURAZIONE PRODOTTI:")
    for n,d in prodotti.items():
        print(f"{n} | tempo={d['tempo_unitario']} | capacità={d['capacita']}")

    risultati_tot = []

    for giorno in range(1, GIORNI + 1):
        risultati_tot.extend(simula_giorno(prodotti, giorno))

    df = pd.DataFrame(risultati_tot)

    # KPI SISTEMA
    totale_prodotti = df["Prodotto realizzato"].sum()
    tempo_tot = df["Tempo utilizzato"].sum()
    saturazione = (tempo_tot / (TEMPO_LINEA * GIORNI)) * 100

    riepilogo = pd.DataFrame([{
        "Giorno": "—",
        "Prodotto": "TOTALE",
        "Domanda": "—",
        "Prodotto realizzato": totale_prodotti,
        "Tempo unitario": "—",
        "Tempo utilizzato": tempo_tot,
        "Soddisfazione domanda %": "—",
        "Tempo residuo linea": "—"
    }])

    df = pd.concat([df, riepilogo], ignore_index=True)

    # salvataggio
    nome = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    df.to_csv(nome, sep=";", index=False)

    print("\nStrategia:", STRATEGIA)
    print("Saturazione linea:", round(saturazione,2), "%")
    print("Output totale:", totale_prodotti)
    print("File salvato:", nome)
    print("\n", df)

    return df


# =========================================================
# AVVIO
# =========================================================

if __name__ == "__main__":
    simulazione()
