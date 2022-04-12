# import operator
from operator import itemgetter
d = {'banana': 3, 'orange': 5, 'apple': 5}

fruit = sorted(d.items(), key=itemgetter(0))
print(fruit)
print(sorted(fruit, key=itemgetter(1), reverse=True))
