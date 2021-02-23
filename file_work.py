'''
A module which helps user to orientate in the json file
'''
import json


def thinker(info):
    '''
    Determines the type of all elements in the data structure
    (dict,list)
    >>> print(thinker(['data','nums','info']))
    This <class 'list'> consist of such elements:
    1) Element:data; Its type:<class 'str'>
    2) Element:nums; Its type:<class 'str'>
    3) Element:info; Its type:<class 'str'>
    ([(), (), ()], ['data', 'nums', 'info'], 0)
    '''
    if isinstance(info,int):
        return None
    model = type(info)
    data = []
    res = []
    flag = 0
    print(f'This {model} consist of such elements:')
    for i,ele in enumerate(info):
        if isinstance(ele,dict):
            data = [(i,type(ele[i])) for i in list(ele.keys())]
            print(f'{i+1}) Dictionary; Its keys: {list(ele.keys())}')
            flag = 1
        elif type(ele) in (tuple,list):
            data = [(i,type(i))  for i in ele] + [i]
            print(f'{i+1}) List; Its elements and their types:{data}')
            flag = 1
        else:
            if isinstance(info,dict):
                print(f'{i+1}) Diction key:{ele}; Its type:{type(info[ele])}')
                data = [(ele,type(ele))]
            else:
                print(f'{i+1}) Element:{ele}; Its type:{type(ele)}')
        res.append(tuple(data))
    return res,info,flag


def get_info(index,source,order = 0,verbose=False):
    '''
    Gets necessary information from the data structure(dict,list)
    >>> get_info('data',{'data':123,'info':'name'})
    123
    '''
    if verbose:
        return source[order][index]
    return source[index]

def info_list(data_base,num):
    '''
    Creates a list from the information,
    which is contained in the data structure(dict,list)
    >>> info_list([(('entities', "<class 'dict'>"),\
    ('source', "<class 'str'>"))],0)
    ['entities', 'source']
    '''
    condition = []
    for string in data_base[num]:
        condition.append(string[0])
    return condition



def main(start_file):
    '''
    The main function of the module. Controls
    the work of other functions.
    >>> main(123)
    '''
    if isinstance(start_file,int):
        return None
    obj = start_file
    while True:
        data = thinker(obj)
        if data[0]:
            print(f'Firstly enter a number of an element (1-{len(obj)}).')
            while True:
                num = input('Enter here: ')
                if (int(num) < 1) or (int(num) > len(obj)):
                    print("It's incorrect! Try again. ")
                    continue
                break
            tip = input('Do you want to receive a tip(Yes/No):')
            if tip == 'Yes':
                print(data[0][int(num)-1])
            print('To continue searching, enter an specific element name.')
            while True:
                obj = input('Write here:')
                check = info_list(data[0],int(num)-1)
                if obj in check:
                    if data[2] == 1:
                        obj = get_info(obj,data[1],int(num)-1,True)
                    else:
                        obj = get_info(obj,data[1])
                    print(obj)
                    print("Is it's what you are searching?")
                    while True:
                        opt = input('Type here(Yes/No): ')
                        if opt not in ('Yes','No'):
                            print('Something went wrong! Try again.')
                            continue
                        break
                else:
                    print('Something went wrong! Try again.')
                    continue
                break
            if opt == 'No':
                if type(obj) in (int,str,bool):
                    print('This is endpoint element.\
 Returning to the original file.')
                    obj = start_file
                continue
            break

if __name__ == "__main__":
    file_name = input('Enter a name of the file: ')
    with open(file_name,'r',encoding='UTF-8') as js_file:
        decoded_fil = json.load(js_file)
    print(main(decoded_fil))
