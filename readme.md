# Simulazione Sistema Produttivo Industriale

Questo progetto implementa una simulazione di una linea produttiva multiprodotto a capacità limitata sviluppata in Python.

## Descrizione
Il modello rappresenta un sistema industriale in cui più prodotti competono per l’utilizzo di una stessa linea produttiva con tempo disponibile limitato. La simulazione consente di analizzare il comportamento del sistema in funzione di diversi parametri operativi e strategie decisionali.

## Funzionamento
Per ogni giorno simulato:
- vengono generati i prodotti con parametri casuali
- viene generata la domanda giornaliera
- viene stabilito un ordine di produzione
- la linea produce finché il tempo disponibile non si esaurisce

## Strategie di produzione
È possibile scegliere tra tre logiche decisionali modificando la variabile `STRATEGIA` nel codice:

- `tempo` → priorità ai prodotti più veloci
- `domanda` → priorità ai prodotti più richiesti
- `bilanciata` → priorità al miglior rapporto domanda/tempo

## Parametri modificabili
Nel file Python è possibile configurare:

- tempo totale linea
- numero prodotti
- giorni simulazione
- strategia produttiva

## Output generato
Il programma restituisce:
- tabella risultati
- indicatori di performance
- file CSV automatico con report

## Requisiti
Python 3 + libreria pandas

## Autore
Inserire nome
