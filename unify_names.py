def unify_name(name_list):
    sorted_list = sorted(name_list, key=lambda name: len(name))
    for i in range(0,len(sorted_list)):
        for j  in range(i+1,len(sorted_list)):
            if sorted_list[i] in sorted_list[j]:
                sorted_list[j] = sorted_list[i]
    return sorted_list
