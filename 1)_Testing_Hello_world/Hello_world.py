#t  --- Testing hellow world with python & gitclear
#n = "999"
#inter = 0

#while True:
#    str_num = str(n)
#    str_num_len = len(str_num)
#    new_num = 1
#    if str_num_len == 1:
#        break
#    else:
#        inter =  inter + 1
#        for i in range(0,str_num_len):
#            new_num = new_num * int(n[i])
#    n = str(new_num)

#print(inter)

#-----------------
#temp_string = "Hi my age is 32 years and 250 days12"
#print(temp_string)

#numbers = [int(temp)for temp in temp_string.split() if temp.isdigit()]

#print(numbers)
pin = "-34532"
num_list =[]
str_len = len(pin)
dig  = 0
new_str = ""
for i in range (0,str_len):
    if pin[i].isdigit() == True:
        num_list.append(pin[i])
print(num_list)