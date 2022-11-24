class TMConfig:

    title = u'Titre du TM'
    first_name = 'Prénom'
    last_name = 'Nom'
    author = f'{first_name} {last_name}'
    year = u'2022'
    month = u'Décembre'
    seminary_title = u'Développement Web'
    tutor = u"Cédric Donner et Johan Jobin"
    release = "Version intermédiaire"
    repository_url = "https://github.com/{your-docs-url}"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

tmconfig = TMConfig()