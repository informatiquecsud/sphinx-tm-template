..  Travail de maturité - CSUD template
    sphinx-quickstart on Fri Nov 19 16:13:20 2021.
    You can adapt this file completely to your liking, but it should at least
    contain the root `toctree` directive.

Titre du travail de maturité
============================

..  toctree::
    :maxdepth: 2
    :caption: Table des matières

    introduction.md
    chapitre-01.md
    chapitre-02.md
    bibliography.rst

..  toctree::
    :maxdepth: 2
    :caption: Tutoriel Sphinx

    tutoriel-sphinx/index.rst



..
    Indices and tables
    ==================

    * :ref:`genindex`
    * :ref:`search`

..
    https://tex.stackexchange.com/questions/44589/how-to-split-bibliography-for-different-sections

..
    ..  raw:: latex

        \begin{filecontents}{sites.bib}
        @misc{A01,
        author = {Author, A.},
        year = {2001},
        title = {Alpha},
        }
        @misc{B02,
        author = {Buthor, B.},
        year = {2002},
        title = {Bravo},
        }
        @misc{C03,
        author = {Cuthor, C.},
        year = {2003},
        title = {Charlie},
        }
        \end{filecontents}

        \addbibresource{sites.bib}

        \nocite{*}
        \printbibliography[title={Livres}]

        \nocite{*}
        \printbibliography[title={Articles}]

..
    ..  bibliography:: refs.bib

        site1
        site2

..  raw:: latex



    \begin{sphinxthebibliography}{AMD88}

    \subsection*{Sites Web}

    \bibitem[AMD88]{index:id3}
    \sphinxAtStartPar
    AMD. Example website 2. \sphinxurl{file://wsl.localhost/Ubuntu20.04LTS/home/donnerc/dev/tm/sphinx-tm-template/tm-ecrit.pdf}, Décembre 1988. Consulté le 25 mars 2022.
    \bibitem[Int88]{index:id2}
    \sphinxAtStartPar
    Intel. Example website. \sphinxurl{http://example.com}, Décembre 1988. Consulté le 25 mars 2022.
    \end{sphinxthebibliography}

..
    ..  rubric:: Articles

    ..  bibliography:: refs1.bib

        site3
        site4

        
..
    ..  raw:: latex

        \begingroup
        \raggedright
        \begin{sphinxthebibliography}{AMD88}
        \bibitem[AMD88]{index:id3}
        \sphinxAtStartPar
        AMD. Example website 2. \sphinxurl{file://wsl.localhost/Ubuntu20.04LTS/home/donnerc/dev/tm/sphinx-tm-template/tm-ecrit.pdf}, Décembre 1988. Consulté le 25 mars 2022.
        \bibitem[Int88]{index:id2}
        \sphinxAtStartPar
        Intel. Example website. \sphinxurl{http://example.com}, Décembre 1988. Consulté le 25 mars 2022.
        \end{sphinxthebibliography}
        \endgroup
