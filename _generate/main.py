inp = """

#2b3634
#474848
#6e5f52
#a2856c
#a0a294
#dcb9a0
#f3dbc6
#fffefe
"""

palette = """:root.{} <
    --color1: {};
    --color2: {};
    --color3: {};
    --color4: {};
    --color5: {};
    --color6: {};
    --color7: {};
    --color8: {};
>"""

name = input('Name: ')
colors = [stripped for s in inp.splitlines() if (stripped := s.strip())]
print(palette.format(name, *colors).replace('<', '{').replace('>', '}'))
