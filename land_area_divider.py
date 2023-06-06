from point_on_side import point_on_sid

try:
    n = int(input("Enter the number of person in which property distribution is to be done:")) 
except ValueError:
    n = -1
m = 1 # this number is used for indexing of mark point

res = point_on_sid(38.3, 51, 36, 60.5, 59.8, m, n)

for v in res:
    if v == res[-1]:
        print("Point on fix side => ",v)
    else:    
        print("Points on unfix side => ",v)

""""Start marking from 'D' to 'C'"""

"""Start marking from 'A' to 'B'"""