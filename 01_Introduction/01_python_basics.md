# Python Basics

## Variabili
Le variabili sono contenitori per memorizzare dati. Puoi pensare a esse come a etichette che fai affiggere a contenitori in cui metti informazioni. Ecco un esempio:

```python
# Dichiarazione di variabili
x = 10
y = "Ciao, mondo!"
```

## Tipi di Dati
Python supporta vari tipi di dati:
- **Interi**: numeri senza parte frazionaria. Esempio:
  ```python
  numero_intero = 5
  ```
- **Float**: numeri con parte frazionaria. Esempio:
  ```python
  numero_float = 5.5
  ```
- **Stringhe**: sequenze di caratteri racchiuse tra virgolette. Esempio:
  ```python
  stringa = "Questo è un esempio"
  ```
- **Liste**: raccolte ordinate di elementi. Esempio:
  ```python
  lista = [1, 2, 3, 4]
  ```
- **Dizionari**: raccolte non ordinate di coppie chiave-valore. Esempio:
  ```python
  dizionario = {"chiave": "valore"}
  ```

## Controllo di Flusso
Il controllo di flusso ti consente di eseguire il codice in modo condizionato.
### Istruzione `if`
```python
x = 10
if x > 5:
    print("x è maggiore di 5")
else:
    print("x non è maggiore di 5")
```

## Cicli
I cicli ti permettono di ripetere un blocco di codice. Due tipici tipi di cicli sono:
### Ciclo `for`
```python
for i in range(5):
    print(i)
```
### Ciclo `while`
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

## Funzioni
Le funzioni ti permettono di raggruppare codice in blocchi riutilizzabili.
### Dichiarazione di una Funzione
```python
def saluta(nome):
    return f"Ciao, {nome}!"
```
### Chiamata a Funzione
```python
messaggio = saluta("Alice")
print(messaggio)
```

## Esempi Pratici
### Esempio di Utilizzo delle Variabili
```python
# Calcolo dell'area di un rettangolo
lunghezza = 5
larghezza = 10
area = lunghezza * larghezza
print(f"L'area del rettangolo è: {area}")
```

### Esempio di Uso delle Funzioni
```python
def somma(a, b):
    return a + b

risultato = somma(3, 7)
print(f"La somma è: {risultato}")
```
Questa è una breve introduzione ai concetti di base di Python. Praticare e sperimentare con questi esempi aiuterà a comprendere meglio il linguaggio.