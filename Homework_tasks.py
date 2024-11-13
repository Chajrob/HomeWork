# food = ['apple', 'banana', 'coconut']
# print(food)
# print(food[1])
# food[1] = 'watermelon'
# print(food)
# food.append(True)
# print(food)
# food.extend([   666, 'funny'])
# print(food)
# food.append(food[0:5:2])
# print(food)
# food.remove(food[1])
# print(food)
# print('666' in food)
# print(666 in food)
# print('coconut' not in food)

tuple_ = 1, 2, 3, True, 'string'
#tuple_2 = (1, 2, 3, 4)
#tuple_3 = tuple([1, 2, 3, 4])
#tuple_[4] = 5
#print(type(tuple_))
#print(tuple_[4])
# list = [1, 2, 3, True, 'string']
# print(tuple_, tuple_.__sizeof__())
# print(list, list.__sizeof__())
# tuple_2 = [1, 2], 3
# print(tuple_2)
# tuple_2 [0] [0] = 5
# print(tuple_2)
tuple_ = (1, 2) + (3, 4)
tuple_2 = tuple_ + (5, 6)
tuple_3 = tuple_ + tuple_2
print(tuple_)
print(tuple_2)
print(tuple_3)
tuple_4 = tuple_ * 3
print(tuple_4)