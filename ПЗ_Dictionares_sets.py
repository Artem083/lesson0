my_dict = {'Darya': 2004, 'Anastasiya': 2006, 'Yana': 2013, 'Mariya': 2016}
my_dict.update({'Anton': 2025, 'Sergey': 2026})
print('Dict:', my_dict)
print('Existing value:', my_dict['Yana'])
print('Not existiing value:', my_dict.get('Kamila'))
Deleted_value = my_dict.pop('Anton')
print('Deleted value:', Deleted_value)
print('Modified dictionary:', my_dict)
my_set = {1, 2, 3, 4, 5, 6, 56.987, 21.777, 2, 3, 'Apple', 'Stone', False, 21.777, False, 'Stone'}
print('Set:', my_set)
my_set.add('Wood')
my_set.add('Metal')
my_set.remove(21.777)
print('Modified set:', my_set)
