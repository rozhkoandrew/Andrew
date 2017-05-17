table = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
def print_table(table):
    for row in table:
        for elem in row:
            print(elem,end='\t')
        print()

def sort_by_row(table):
    final_lst = []
    count_n = 0
    for x in range(0,6):
        lst = []
        final_lst.append(lst)
        for row in table:
            #final_lst.append(lst)
            for idx in range(0,len(row)):
                if idx == count_n:
                    lst.append(row[idx])
        count_n += 1
    return final_lst

def sort_table(table):
    final_lst = []
    for idx in range(0,len(table)):
        lst = []
        final_lst.append(lst)
        if idx % 2 == 0:
            for row in sorted(table[idx], reverse=True):
                lst.append(row)
        else:
            for row in sorted(table[idx], reverse=False):
                lst.append(row)
    return final_lst

sorted1 = sort_table(table)
print_table(sort_by_row(sorted1))

