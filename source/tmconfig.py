class TMConfig:

    title = u'Titre du TM'
    first_name = 'Prénom'
    last_name = 'Nom'
    author = f'{first_name} {last_name}'
    year = u'2021'
    month = u'Décembre'
    seminary_title = u'Développement d’outils ou matériel d’enseignement de l’informatique'
    tutor = u"Cédric Donner"
    release = "Version intermédiaire"
    repository_url = "https://github.com/{your-docs-url}"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

tmconfig = TMConfig()