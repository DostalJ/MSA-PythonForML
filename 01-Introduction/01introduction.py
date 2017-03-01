print("Hello World") # vypis

####################################
# string, int, float, list, tuple, set, dict
####################################
my_str = "Ahoj" # support indexing
my_int = 4
my_float = 3.14
my_list = [1,2,3] # support indexing
my_tuple = (5, 6) # upport indexing, equivalent to 5,6
my_set = {1,1,2,2,2,3,3,3,6,8} # ponecha jen unikatni prvky, don't support indexing
my_dict = {'prvek_jedna': 1, 'prvek_dva': 2}

##########
# indexing
##########
my_list[0] # prvni prvek
my_list[2] # treti prvek
my_list[-1] # posledni prvek
my_list[-2] # predposledni prvek


######################
# if, for loop, while
######################
k = 5
if k%2 == 0 and k > 0:
    print("k je delitelne dvema a vetsi nez nula.")
elif k%3 == 0 and k < 0:
    print("k je delitelne trema a mensi nez nula.")
else:
    print("Netusim jake je k")

# i iterates through elements of my_list
for i in my_set:
    print(i)

# range(): neni list, ale ve for loop se chova jako list, je to iterable
for i in range(3):
    print(i)

i = 0
while i < 10:
    print("Zatim je i={}.".format(i)) # zpusob formatovani stringu
    # i = i + 1
    i += 1 # inkrementation


###########
# functions
###########
def f(x):
    y = x**2 # second power
    return y
