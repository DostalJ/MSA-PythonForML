print("Hello world")

a = 5 # int
b = 2.4 # float
my_list = [5, 2, 3]

my_list[0]
my_list[-1]

my_list.sort()

my_set = {1,2,3,4,4,4,4}
my_list_from_set = list(my_set)

my_dict = {'prvni_prvek': [11,23], 'druhy_prvek':60}
my_dict['prvni_prvek']
my_dict.keys()
my_dict.values()

a = [[1,2,3],
     [4,5,6]]

long_list = [1,2,3,4,5,6,7,8,9]
long_list[2:5]


def f(x):
    y = 6*x**2
    return y

c = f(7)

def f_print(x=3):
    y = 6*x**2
    print(y)


# and == &
# or |

x = -88.564938
if x == 55 or x == 6:
    print('x je 55 nebo 6')
elif x < 0:
    print('{:.3f} < 0'.format(x))
else:
    print('x neni 55')


long_list

for cislo in long_list:
    print(cislo)

list_of_strings = ['jedna', 'dva']
for slovo in list_of_strings:
    print(slovo)

for i in range(len(list_of_strings)):
    print(i)
    print(list_of_strings[i])
