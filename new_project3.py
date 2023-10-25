dic = {'name':'python', 'age':1991, 'place':'US', 'name1':'python'}
print(dic.get('place'))
print(dic.keys()) #specific data
print(dic.values())
dic.clear()
print(dic)
dic.pop('name1')
print(dic)