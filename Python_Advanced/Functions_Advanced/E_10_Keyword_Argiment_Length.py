def kwargs_length(**kwargs):
    return len(kwargs)

# here we have two opposite steps :
# first we unpack the dictionary with **dictionary**
# then we pack it again with **kwargs


dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))
