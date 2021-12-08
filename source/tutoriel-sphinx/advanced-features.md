(advanced-features)=

# Fonctionnalités avancées

## Encadrés

````{sidebar} Encadré mis en évidence

Ceci est un encadré qui sort du fil du texte (on dit que cet encadré et
"flottant", car il flotte sur le texte principal).

La directive Sphinx `sidebar` permet d'insérer certaines informations dans un
encadré (dans le PDF) et dans une sorte de panneau flottant dans la version
HTML.

```{math}

f(x) = 2x^2 + 1
```

Il faut commencer par placer le `sidebar` dans le code Markdown et ensuite
placer le contenu qui viendra se placer à gauche de la page.

````

Paragraphe est écrit de manière normale, au fil du texte.

- On pourrait remplir avec du contenu .... mais ce contenu n'est pas très
  intéressant. Ce contenu peut faire plusieurs lignes dans le fichier Markdown.
  C'est tout de même un peu long.

```{warning}

Il ne faut pas trop abuser des "sidebars", car le placement n'est pas du tout le même sur la version HTML en ligne et dans la version PDF.

Il vaut éviter également de mettre trop de contenu dans les `sidebar`.
```

## Direction `raw`

```{tip}
La directive `raw` permet de différencier le contenu présenté dans la version HTML et celui présent dans la version PDF. Elle permet également d'insérer du contenu tel quel pour profiter de toutes les fonctionnalités du format cible (par exemple le HTML ou le LaTeX).
```

Parfois, il est utile d'inclure un certain contenu (images, vidéos, ...) dans la
version HTML en ligne, mais de ne pas inclure ce contenu dans la version PDF.
C'est typiquement le cas pour des vidéos ou d'autres éléments interactifs.

:::{raw} html

Tout le conenu dans la directive <code>raw</code> sera copié directement tel quel dans la sortie HTML. Ce contenu n'apparaîtra pas dans le LaTeX.

<p>Ce contenu ne sera visible que sur le site HTML</p>
<iframe src="https://webtigerjython.ethz.ch/" width="100%" height="600"></iframe>

:::

:::{raw} latex

En revanche, ce contenu n'apparaîtra que dans le LaTeX et pas dans le HTML.

:::

:::{tip}

L'avantage de la directive `raw` est de pouvoir insérer n'importe quel code
HTML, aussi exotique soit-il.

:::
