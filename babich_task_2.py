sum_wh_div = 0 #sum of odd numbers in a cube
for odd_numbers in range(1,1000,2):
    odd_numbers = odd_numbers**3 # odd list in a cube
    print(odd_numbers)
    elem_odd = 0 #list items
    for num in str(odd_numbers):

        elem_odd = int(num)+elem_odd
    if elem_odd % 7 == 0:
        sum_wh_div = odd_numbers+sum_wh_div
print(sum_wh_div)
#further the same thing only plus 17
sum_wh_div_17 = 0
for odd_numbers_17 in range(1,1001,2):
    odd_numbers_17 = odd_numbers_17**3 + 17
    # print(odd_numbers_17)
    elem_odd_17 = 0
    for n in str(odd_numbers_17):

        elem_odd_17 = int(n)+elem_odd_17
    if elem_odd_17 % 7 == 0:
        sum_wh_div_17 = odd_numbers_17+sum_wh_div_17
print(sum_wh_div_17)
