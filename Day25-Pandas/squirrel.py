# import pandas

# datas = pandas.read_csv('squirrel_data.csv')
# data = pandas.DataFrame(datas)
# fur_clr = data['Primary Fur Color'].to_list()

# gray,cinnamon,black = 0,0,0

# for color in fur_clr:
#     if color == 'Gray':
#         gray += 1
#     elif color == 'Black':
#         black += 1
#     elif color == 'Cinnamon':
#         cinnamon += 1

# df = {
#     'black' : black,
#     'cinnoman':cinnamon,
#     'gray':gray
# }
# op = pandas.DataFrame(df)
# print(op)

import pandas as pd
data = pd.read_csv('squirrel_data.csv')
color_counts = data['Primary Fur Color'].value_counts()

df = pd.DataFrame({
    'Count': color_counts
})
print(df)


