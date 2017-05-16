import requests
import json
def  get_hw_results():
    response = requests.get('http://54.201.47.219:8080/api/v1/hw_results/')
    json_object = response.json()
    return json_object
def get_tests_results():
    response = requests.get('http://54.201.47.219:8080/api/v1/test1_results/')
    json_object = response.json()
    return json_object
def get_weight():
    response = requests.get('http://54.201.47.219:8080/api/v1/test1_weights/')
    print(response)
    json_object = response.json()
    lst_of_weight = [x for x in json_object['test1_weights']]
    return lst_of_weight

def get_all_students():
    response = requests.get('http://54.201.47.219:8080/api/v1/students')
    json_object = response.json()
    return (json_object['students'])

def get_student_by_id(id):
    response = requests.get('http://54.201.47.219:8080/api/v1/students/' + str(id))
    print(response)
    json_object = response.json()
    return json_object['student']
def update_student(id,what_u_want_to_update,updating_object):
    response = requests.get('http://54.201.47.219:8080/api/v1/students/' + str(id))
    print(response)
    json_object = response.json()
    response = requests.put('http://54.201.47.219:8080/api/v1/students/' + str(id),
                    json=json.dumps({what_u_want_to_update:updating_object}))
    print(response)

def add_student(id,fullname,email,github,rank):
    dictionary= {}
    dictionary['id'] = id
    dictionary['fullname'] = fullname
    dictionary['email'] = email
    dictionary['github'] =github
    dictionary['rank'] = rank
    response = requests.post('http://54.201.47.219:8080/api/v1/students/',json.dumps(dictionary))
    print(response)
    print(response.content)

def count_and_update_students():
    group = get_all_students()
    hw_results = get_hw_results()
    test1_results = get_tests_results()
    lst_of_weight = get_weight()
    for elem in group:
        lst_of_hm = []
        lst_of_id = []
        test_results = []
        lst_of_id.append(elem['id'])
        for elem in hw_results:
            if elem['id'] == lst_of_id[0]:
                lst_of_hm = (elem['task_completion'])
        for elem in test1_results:
            if elem['id'] == lst_of_id[0]:
                lst_of_test_r = (elem['task_completion'])
        for x in range(0,len(lst_of_weight)):
            result = lst_of_weight[x] * lst_of_test_r[x]
            test_results.append(result)
            rank = sum(test_results) + sum(lst_of_hm)
        response = requests.put('http://54.201.47.219:8080/api/v1/students/' + str(lst_of_id[0]),
                                json=json.dumps({"rank": rank}))
        return response

def print_students_info(dict, sorted_by,reverse_yes_or_no):
    group = get_all_students()
    if reverse_yes_or_no == 'yes':
        for elem in sorted(group, key=lambda value: value.get(sorted_by),reverse=True):
             print("-----------------------------------------"
                                    ": ID: %d:"
                                   " :.......................................:"
                                   " : Full"
                                    "name: %s"
                                    ": Email: %s"
                                    ": Github: %s"
                                    ": Rank: %d:"
                " -----------------------------------------"%(
                 elem['id'],elem['fullname'],elem['email'],elem['github'],elem['rank']))
    else:
        for elem in sorted(group,key=lambda value :value.get(sorted_by)):
            print("-----------------------------------------"
                  ": ID: %d:"
                  " :.......................................:"
                  " : Full"
                  "name: %s"
                  ": Email: %s"
                  ": Github: %s"
                  ": Rank: %d:"
                  " -----------------------------------------" % (
                  elem['id'], elem['fullname'], elem['email'], elem['github'], elem['rank']))

if __name__ =='__main__':
    #print(get_all_students())
    #print(get_student_by_id(1025))
    #print(count_an_update_students())
    #print(get_hw_results())
    #print(get_tests_results())
    #print(get_weight())
    print_students_info(get_all_students,'rank','yes')
    update_student(1025,'rank',100)
