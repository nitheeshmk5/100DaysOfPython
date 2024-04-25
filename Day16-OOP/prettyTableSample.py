from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Students",["Nitheesh","Dharshan","Kalyan"])
table.add_column("Course",["BSc IT",'BCA','BCom'])

print(table)