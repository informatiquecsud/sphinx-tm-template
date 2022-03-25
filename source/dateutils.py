from datetime import date

months_fr = [
    u'Janvier',
    u'Février',
    u'Mars',
    u'Avril', 
    u'Mai', 
    u'Juin', 
    u'Juillet', 
    u'Août', 
    u'Septembre', 
    u'octobre', 
    u'novembre', 
    u'décembre', 
]

def get_month(d):
    return months_fr[d.month].capitalize()
        
def get_year(d):
    return str(d.year)
