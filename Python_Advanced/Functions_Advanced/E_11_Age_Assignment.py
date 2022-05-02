def age_assignment(*names, **kwargs):
    fin_dict = {}
    for k, v in kwargs.items():
        for name in names:
            if k == name[0]:
                fin_dict[name] = v
    return fin_dict


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
