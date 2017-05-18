import requests
import json
URL = 'http://54.201.47.219:8080/api/v1'
def  get_hw_results():
    response = requests.get(URL+'/hw_results/')
    json_object = response.json()
    return json_object

def get_tests_results():
    response = requests.get(URL+'/test1_results/')
    json_object = response.json()
    return json_object

def get_weights():
    response = requests.get(URL + '/test1_weights/')
    print(response)
    json_object = response.json()
    lst_of_weight = json_object['test1_weights'][:]
    return lst_of_weight

def get_all_students():
    response = requests.get(URL + '/students')
    json_object = response.json()
    return (json_object['students'])

def get_student_by_id(id):
    response = requests.get(URL+ '/students/' + str(id))
    print(response)
    json_object = response.json()
    return json_object['student']

def update_student(id, key, value):
    response = get_student_by_id(id)
    print(response)
    response = requests.put(URL+'/students/' + str(id),
                    json=json.dumps({key:value}))
    print(response)

def add_student(id,fullname,email,github,rank):
    student= {}
    student['id'] = id
    student['fullname'] = fullname
    student['email'] = email
    student['github'] =github
    student['rank'] = rank
    response = requests.post(URL+'/students/'+json.dumps(student))
    print(response)
    print(response.content)

def count_and_update_students():
    group = get_all_students()
    hw_results = get_hw_results()
    test1_results = get_tests_results()
    lst_of_weight = get_weights()
    rank = 0
    for elem in group:
        lst_of_hm = []
        lst_of_id = []
        lst_of_id.append(elem['id'])
        for elem in hw_results:
            if elem['id'] == lst_of_id[0]:
                lst_of_hm = (elem['task_completion'])
        for elem in test1_results:
            if elem['id'] == lst_of_id[0]:
                lst_of_test_r = (elem['task_completion'])
                test_results = [lst_of_weight[x] * lst_of_test_r[x] for x in range(0,len(lst_of_weight))]
                rank = sum(test_results) + sum(lst_of_hm)
        for elem in group:
            if elem['id'] == lst_of_id[0]:
                    update_student(elem['id'],'rank',rank)


def print_students_info(dict, sorted_by,reverse):
    group = get_all_students()
    for elem in sorted(group, key=lambda value: value.get(sorted_by),reverse=reverse):
         print("-----------------------------------------\n"
                                ": ID: %d:\n"
                               ":.......................................:"
                               " \n: Full"
                                "name: %s"
                                ": \nEmail: %s"
                                ": Github: %s\n"
                                ": Rank: %d\n:"
            " -----------------------------------------"%(
             elem['id'],elem['fullname'],elem['email'],elem['github'],elem['rank']))


if __name__ =='__main__':
    #print(get_all_students())
    #print(get_student_by_id(1025))
    count_and_update_students()
    #print(get_hw_results())
    #print(get_tests_results())
    #print(get_weights())
    print_students_info(get_all_students,'rank',True)
    #update_student(1030,'rank',2906)
