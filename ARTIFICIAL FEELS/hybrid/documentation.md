# hybrid 7.1 
## come creare skill per hy

1. apri il file `derivatore_json.py` le cui ultime righe sono tipo:

```python
intent_maker('reply_noreask_nodialgue_handler', ['niente', 'nulla', 'bene'], synsout=False, extraconts=['ah, va bene', "d'accordo", 'okk', 'ook'])
print('[*] Derivating...')
derivate(l_=['Reply_noreask_nodialgue_handlerIntent'])
```

andiamo allora ad esaminare queste 3 righe.

### nella prima riga c'è scritto:

```python
intent_maker('reply_noreask_nodialgue_handler', ['niente', 'nulla', 'bene'], synsout=False, extraconts=['ah, va bene', "d'accordo", 'okk', 'ook'])
```

ed è una chiamata alla funzione intent_maker().

> intent_maker() server per creare un nuovo intent nel file dataset.json tramite dei dumps da python objs a json objs.

adesso vediamo gli argomenti di intent_maker() generalizzati:

intent_maker() è strutturato così:

```python
def intent_maker(name:str, contents:list, synsout=True, extraconts=[])
```
> name -> il valore di indicizzazione, verrà usato anche per identificare la skill python

> contents -> questa lista sarà contenuta in una indicizzata con "samples", deve contenere le parole che se usate dall'utente attiveranno la skill

> synsout -> boolean, usa la stessa lista per input e output. se settata a False devi specificare un valore per extraconts

> extraconts -> una lista contenente gli output

usando questi valori un esempio facile sarebbe:

```python
x= input('>> ')
if x in contents:
    print(an_element_of(extraconts))
```
anche se il codice non funziona così.


per creare una skill che ad un insulto risponde con un altro insulto basterebbe scrivere questo:

```python
intent_maker('name', ['scemo', 'schifoso'])
#print('[*] Derivating...')
derivate(l_=['NameIntent'])
```

questo avrà modificato sia un file json che creato un file python.

nel file json è stato aggiunto questo sotto dict:

```json
"NameIntent": {
    "syns_out": 0,
    "name":"nome",
    "samples":[
        "scemo",
        "schifoso"
    ]
}
```
così se l'utente dirà una parola di ["NameIntent"]["samples"] eseguirà la skill che inizia con f(["NameIntent"]["name"])

quell' f() prima dell'indice del nome sarebbe la funzione lambda che ritorna il suo input ma con l'ultima lettera cambiata con una "a".