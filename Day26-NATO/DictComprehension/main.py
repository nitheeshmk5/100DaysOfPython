#Exercise 1
para = input("Enter some para : ")
new_dict = {x:len(x) for x in para.split()}
print(new_dict)

#Exercise 2
week_c = {'monday':20,'tuesday':23,'wednesday':98}

#f = c * (9/5) + 32
week_f = {x:(9/5 * y + 32) for (x,y) in week_c.items()}
print(week_f)