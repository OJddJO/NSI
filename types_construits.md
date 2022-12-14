# Listes

Une liste est une séquence d'éléments

Pour définir une liste => [ ]
```
>>> liste = ['2nd', 1, [2, "hello"]]
>>> print(liste)
['2nd', 1, [2, "hello"]]
```

Pour avoir la valeur à la deuxième position
```
>>> liste = ['2nd', 1, [2, "hello"]]
>>> print(liste[0])
'2nd'
```

```
>>> liste = ['2nd', 1, [2, "hello"]]
>>> print(liste[4])
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    liste[4]
IndexError: list index out of range
```

Pour avoir les valeurs de la position 0 à la position 2 exclus
```
>>> liste = ['2nd', 1, [2, "hello"]]
>>> liste[0:2]
['2nd', 1]
```


```
>>> liste = ['2nd', 1, [2, "hello"]]
>>> liste[-1]
[2, 'hello']
>>> liste[-2]
1
```

```
>>> liste = ['2nd', 1, [2, "hello"]]
>>> liste[2][1]
'hello'
#retourne l'élément de la liste [2, "hello"] qui est elle même est dans la liste nommée "liste"
```

```
>>> [1, 2, 3] + [4, 5]
[1, 2, 3, 4, 5]
```

```
>>> liste = [1, 2, 3, 4]
>>> liste += [5, 6]
>>> print(liste)
[1, 2, 3, 4, 5, 6]
```

```
>>> liste = [1, 2, 3, 4]
>>> liste.append(5)
>>> print(liste)
[1, 2, 3, 4, 5]
```

```
>>> liste = [1, 2, 3]
>>> L = [4, 5]
>>> liste.extend(L)
>>> print(liste)
[1, 2, 3, 4, 5]
```

```
>>> liste = [1, 2, 3]
>>> liste.insert(2, "hello")
>>> print(liste)
[1, 2, 'hello', 3]
```

```
>>> liste = [1, 2, 3, 2, 5]
>>> liste.remove(2)
>>> print(liste)
[1, 3, 2, 5]
```

```
>>> liste = ["hello", "bonjour", "hi"]
>>> liste.pop(1)
"bonjour"
>>> print(liste)
["hello, "hi"]
```

```
>>> liste = [1, 2, 3, 4]
>>> liste.index(2)
3
```

```
>>> liste = ["bonjour, "hi", "hello", "bonjour"]
>>> liste.count("bonjour")
2
```

```
>>> liste = [1, 4, 5, 3, 2]
>>> liste.reverse()
>>> print(liste)
[2, 3, 5, 4, 1]
```

# Tuple

Les tuples (n-uplets en français) sont des séquences dont les valeurs sont immuables (qui ne peuvent pas être changées)

```
>>> tuple_1 = (1, "ok", 2)
>>> print(tuple_1)
(1, "ok", 2)
```

Créer un tuple avec une seule valeur
```
>>> c = (9, )
>>> print(c)
(9)
>>> print(type(c))
<class 'tuple'>
```

```
>>> c = (9)
>>> print(c)
9
>>> print(type(c))
<class 'int'>
```

```
def test(a, b):
    return a, b

>>> resultat = test(2, 3)
>>> print(resultat)
(2, 3)
>>> print(type(resultat))
<class 'tuple'>
```

**Attention, il n'existe pas de méthodes pour les tuples permettant de modifier les valeurs**
- `remove()`
- `append()`


Pour obtenir la valeur à la zéro-ième position de la tuple `tuple_2` 
```
>>> tuple_2 = ("hello", "bonjour")
>>> print((tuple_2[0])
"hello"
```

## Tuples en compréhension
```
>>> t = tuple(i for i in range(6))
>>> print(t)
(0, 1, 2, 3, 4, 5)
```

# Dictionnaires

```
>>> capitales = {"France": "Paris", "Allemagne": "Berlin"}
>>> print(capitales["France"])
"Paris"
```

```
>>> liste_capitales = [("France", "Allemagne"), ("Paris", "Berlin")]
>>> dict_capitales = dict(liste_capitales)
>>> print(dict_capitales)
{"France": "Paris", "Allemagne": "Berlin"}
>>> print(dict_capitales["France"])
"Paris"
```

Une clé est unique
```
>>> capitales = {"France": "Paris", "Allemagne": "Berlin", "France": "Marseille"}
>>> print(capitales)
{"Allemagne": "Berlin", "France": "Marseille"}
```

Pour entrer une valeur avec une clé particulière
```
>>> capitales = {"France": "Paris", "Allemagne": "Berlin"}
>>> capitales["Islande"] = "Reykjavik"
>>> print(capitales)
{"Allemagne": "Berlin", "France": "Paris", "Islande": "Reykjavik"}
```

Si la clé n'existe pas
```
>>> capitales["Italie"]
KeyError: "Italie"
```

Méthode `.get(key, error_text)`
```
>>> capitales.get("Italie", "La clé n'existe pas")
# .get("clé", "erreur retourné")
"La clé n'existe pas"
```

Modifier la valeur associer à une clé
```
>>> capitales["France"] = "Marseille"
>>> print(capitales)
{"Allemagne": "Berlin, "France": "Marseille"}
```

La clé et la valeur ne sont pas forcément des chaînes de caractères
```
coords = {("Paris", "France"): ["48° 51' N", "2° 21' E"]}
```

