#! /usr/bin/python3                                     #changed python to python3

int_var1 = [1,2,3,4]
str_var1 = "This is a string"                           #deleted ' and added " to match the other one
flt_var1 = 123.445                                      #deleted the ' ' so that the initalized datatype is not a string
tup_var1 = tuple(int_var1)

sumflt = flt_var1 + int_var1[0]                         #changed int_var0 to int_var1[0] to reference the first item in the list
sumflt = sumflt + int_var1[1]                           #changed int_var1 to int_var1[1] to reference the second item in the list
sumflt = sumflt + int_var1[2]                           #changed int_var2 to int_var1[2] to reference the third item in the list
sumflt = sumflt + int_var1[3]                           #changed int_var3 to int_var1[3] to reference the fourth item in the list

                                                        #removed tup_var[0] = 2 because tuple is immutable

print("sum is: " + str(sumflt))                         #changed sumflt to a string datatype so that it can be added together
print(str_var1 + " " + str(flt_var1))                   #changed flt_var1 into a string so that it can be added togetther
print("str_var1 * 4 " + str_var1 * 4)                   #nothing was changed because this syntax is correct
print("str_var1 + 4 " + str_var1 + str(4))              #changed 4 to a string datatype so that it can be added with the other string
