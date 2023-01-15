class TMConfig:

    title = u"Création du site Web déstiné au Comité Etudiant Humanitaire du Collège du Sud" 
    first_name = 'Capucine'
    last_name = 'Böhning'
    author = f'{first_name} {last_name}'
    year = u'2023'
    month = u'Janvier'
    seminary_title = u'Développement Web'
    tutor = u"Cédric Donner et Johan Jobin"
    release = "Version intermédiaire"
    repository_url = "https://github.com/capucineboh/site-candide"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

tmconfig = TMConfig()