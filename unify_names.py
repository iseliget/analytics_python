def unify_name(name_list):
    sorted_list = sorted(name_list, key=lambda name: len(name))
    for i in range(0,len(sorted_list)):
        sorted_list = [sorted_list[i] for x in sorted_list if sorted_list[i] in x]
    return sorted_list
