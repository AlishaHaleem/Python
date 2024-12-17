from prettytable import PrettyTable

table = PrettyTable()
table .add_column("Pokemon Name", ["Pikachu", "Squirtle", "Bulbasaur"])
table .add_column("Type", ["Electric", "Water" , "Fire"])
#print(table.align)
table.align = "l"
# TODO : alignment means change the written format style of this.
print(table)





