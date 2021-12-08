
with open("input.md", "r", encoding='utf-8') as ifile:
    text = ifile.read()


parts = text.replace('\r', '').replace('\t', '  ').split('```')
##print(parts)
editor_code = parts[1]
launch_code = parts[3]

tab = '{tab-set}'
tab_item = '{tab-item}'

final_code = f'''
::::{tab}
:::{tab_item} Éditeur
```logo{editor_code}```
:::

:::{tab_item} Champ de saisie
```logo{launch_code}```
:::
::::
'''

with open("output.md", "w", encoding='utf-8') as ofile:
    ofile.write(final_code)
    
print(final_code)