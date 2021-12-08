# Fonctionnement de la toolchain Sphinx

Avant de commencer, il faut comprendre le fonctionnement général de Sphinx. Il
s'agit d'une "toolchain", à savoir un ensemble d'outils qui permettent de
transformer des fichiers Markdown en documents formatés (soit HTML pour le Web
ou LaTeX pour produire un PDF).

Pour les personnes qui connaissent un peu le LaTeX, Sphinx est un système un peu
analogue: on écrit du code et un outil s'occupe de tout mettre en page et faire
la reliure de manière professionnelle. D'ailleurs, Sphinx permet de générer du
LaTeX pour générer un document PDF.

Au contraire de Microsoft Word, où l'on voit directement le résultat final
lorsqu'on écrit le contenu, Sphinx utilise un paradigme semblable à celui
utilisé en LaTeX: on écrit du code avec une syntaxe particulière qui est ensuite
transformé dans le résultat final par la toolchain.

```{figure} figures/make-html.png
---
align: center
width: 100%
---
Processus de génération du HTML avec Sphinx
```

```{figure} figures/make-tmpdf.png
---
align: center
width: 100%
---
Processus de génération du PDF avec Sphinx
```

## Les avantages de Sphinx par rapport à Word

Par rapport à Word, Sphinx présente les avantages suivants

- Sphinx est un outil Open-Source, ce qui signifie qu'on peut l'adapter sans
  problème à n'importe quel besoin. De plus, il n'y a aucun risque que le
  système ne soit tout-à-coup plus supporté, car une importante communauté s'occupe de le faire évoluer et de corriger les bugs détectés.

- On écrit de la documentation dans des fichiers qui ne contiennent que du
  texte, comme une sorte de "code source".

- On écrit le contenu dans Visual Studio Code ou un autre éditeur. On peut donc
  utiliser toute la puissance de tels éditeurs pour optimiser la rédaction du contenu.

- Le contenu est très facilement versionalisable (utilisation de git et Github).

- Permet d'intégrer très facilement les éléments suivants qui sont très courants
  dans un travail de maturité en informatique

  - Des mathématiques
  - Du code source
  - Des éléments interactifs (quiz, programmes qui s'exécutent directement dans
    le navigateur, etc. )

- À partir d'une seule source, on peut générer des documents pour différentes
  cibles (Site Web, Document PDF, e-book pour une liseuse, ...)

- Le système est extensible et facilement personnalisable

- Lorsqu'on écrit un document pour Sphinx, il n'est pas nécessaire de se
  préoccuper de la mise en page et de la mise en forme du contenu. On se
  contente d'écrire

## Les désavantages de Sphinx par rapport à Word

- L'utilisation de Sphinx est moins intuitive que celle de Word au début.

- Word est un traitement de texte de type "WYSIWYG" (What You See Is What You
  Get). Lorsqu'on écrit le contenu dans Word, on voit directement le résultat
  final. Sphinx est un système de rédaction de type "WYSIWYM" (What You See Is
  What You Mean). Comme on ne voit pas directement le résultat final, il faut
  être attentif lors de la relecture du résultat final. On peut parfois avoir de sacrées surprises, en raison d'une erreur de syntaxe par exemple.

- La correction orthographique est moins facile qu'en Word, car il n'existe pas
  d'outil parfaitement intégré qui permette de faire la correction de manière
  automatique. Il est toutefois possible de passer du Sphinx à Word (avec un rendu dégradé), pour utiliser le correcteur automatique de Microsoft Word.
