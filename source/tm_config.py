class TMConfig:

    title = u'titre du TM (à modifier dans tm_config.py)'
    prenom = 'Prénom'
    nom = 'Nom (à modifier dans tm_config.py)'
    author = f'{prenom} {nom}'
    year = u'2022'
    month = u'Janvier'
    seminary_title = u'Développement d’outils ou matériel d’enseignement de l’informatique'
    tutor = u"Cédric Donner"
    release = "Version intermédiaire"
    repository_url = "https://github.com/{your-docs-url}"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

tmconfig = TMConfig()