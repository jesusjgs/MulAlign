from FUNReader import read_fun_file_as_list_of_lists
from VARReader import read_var_file_as_dictionary

def main():
    fun = read_fun_file_as_list_of_lists("Resources/FUN.BB12044.tsv")
    var = read_var_file_as_dictionary("Resources/VAR.BB12044.tsv")
    dictionary_list = []
    main_dictionary = ()
    count = 0
    for i in var:
        x = fun[count]
        main_dictionary[x]=i
        dictionary_list.append(main_dictionary)
        count += 1

