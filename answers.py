#result for 1

this_dict = {
    'name' : 'yonatan',
    'age' : '18',
    'birthdate' : '22/08/2003'}


#result for 2
this_dict = {
    'name' : 'Yonatan',
    'age' : '18',
    'birthdate' : '22/08/2003'}
this_dict['last name'] = 'Idlis'

#result for 3
this_dict = {
    'name' : 'Yonatan',
    'age' : '18',
    'birthdate' : '22/08/2003'}
this_dict['hobbies'] = ['video games', 'sports']


#result for 4
def key_is_name():
    my_dict = {
    'name' : 'yonatan',
    'age' : '18',
    'birthdate' : '22/08/2003'
    }
    if 'name' in my_dict:
        return True
    else:
        return False

#ressult for 5
def value_is_six(dict):
    for i in dict:
        if dict[i] == 6:
            return True
    return False

#result for 6
def same_values(dict):
    list(dict.values())
    my_values = list(dict.values())

    return checkDuplicate(my_values)

def checkDuplicate(user):
    if len(set(user)) < len(user):
        return True
    return False

#result for 7
def same_value(dict1, dict2):
    for i in dict1:
        for j in dict2:
            if i == j:
                return i
    return false
print (same_value('red' 'blue', 'red' 'yelow'))