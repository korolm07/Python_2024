from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes

x = table = ColorTable(theme=Themes.OCEAN)
x.add_column("Pokemon name",["Pikachu","Squirtle","Cgarmander"]) 
x.add_column("Type", ["Electric", "Water","Fire"])
x.align = "l"
print(x)