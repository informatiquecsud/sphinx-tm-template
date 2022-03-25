
from dateutils import *

class TMConfig:

    title = u'Titre du TM'
    school = "Collège du Sud"
    worktype = "Travail de maturité"
    first_name = 'Prénom'
    last_name = 'Nom'
    author = f'{first_name} {last_name}'
    year = get_year(date.today())
    month = get_month(date.today())
    seminary_title = u'Développement d’outils ou matériel d’enseignement de l’informatique'
    tutor = u"Cédric Donner"
    version_finale = True
    repository_url = "https://github.com/{your-docs-url}"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

tmconfig = TMConfig()