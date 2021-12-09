# Insérer du code

```{admonition} Objectifs de cette page
Cette page montre comment insérer du code Python, HTML ou Javascript dans la documentation.
```

:::{admonition} Remarque
---
class: error
---

Ma nouvelle remarque

:::

## Insertion simple

Le plus simple pour insérer du code dans la documentation est d'utiliser les outils natifs mis à disposition par Markdown pour cela. Cela ne laisse cependant que peu de marge de manoeuvre de personnalisation.

```python
from math import pi

def foo(a, b):
    return a + b

print(foo(10, 20))
```

```js
let maVariable = 3;

```

```html
<html>
    <body>
    </body>
</html>
```



`````{admonition} Code Markdown
````markdown
```python
from math import pi

def foo(a, b):
    return a + b

print(foo(10, 20))
```
````
`````

## Plus de flexibilité

On peut également utiliser la direction Sphinx `code-block` pour insérer du code de manière plus sophistiquée, avec de la numérotation automatique, des lignes mises en évidence et des tas d'autres options (voir)

```{code-block} python
---
emphasize-lines: 3-4
linenos: true
---
from math import pi

def foo(a, b):
    return a + b
```

`````{admonition} Code Markdown
````markdown
```{code-block} python
---
emphasize-lines: 1
linenos: true
---
from math import pi

def foo(a, b):
    return a + b
```
````
`````

## Insérer du code depuis un fichier externe

Il est également possible d'inclure du code dans la documentation depuis un fichier externe, au lieu d'avoir à écrire copier le code directement dans le fichier `.md`.

```{literalinclude} src/exemple.py
---
language: python
emphasize-lines: 1
linenos: true
---
```

### Titre 2 

#### Titre 3
