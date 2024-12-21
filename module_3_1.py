calls = 0

def count_calls():
    global calls
    print (calls)
def string_info(string):
    global calls
    calls += 1
    print(len(string), string.upper(), string.lower())
def is_contains(string, list_to_search):
    global calls
    calls += 1
    string = string.lower()
    list_ = (list(list_to_search))
    list_2 = []
    for i in range(len(list_to_search)):
        list_2.append(list_[i].lower())
    print(string in list_2)

string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
count_calls()

