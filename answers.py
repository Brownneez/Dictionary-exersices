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
    for i in dict1.keys():
        if i in dict2.keys():
            return i
    return False

#result for 8
def return_list(dict1, dict2):
    my_list = []
    for i in dict1.keys():
        if i in dict2.keys():
            my_list.append(i)
    return my_list+i
#result for 9
def dict_and_par (my_dict, par):
    for i in my_dict.keys():
        if i == par:
            return  i

#result for 10
def value_equals_par (my_dict, par):
    for i in my_dict.values():
        if i == par:
            return i

#result for 11
def return_ordered_list(my_dict):
    my_list = []
    for i in my_dict.values():
        my_list.append(i)
    my_list.sort()
    return  my_list


#result for 12
def update_dict(my_dict, par1, par2):
    a = par2
    b = par1
    for i in my_dict.keys():
        if i == par1:
            my_dict.update({'': a})
        else:
            my_dict.update({b:a})
    return my_dict
#result for 13
def get_two_lists(list1, list2):
    if len(list1) == len(list2):
       my_dict = dict(zip(list1, list2))
    return my_dict
    return none
#result for 14






