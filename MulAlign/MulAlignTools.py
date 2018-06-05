from FUNReader import read_fun_file_as_list_of_lists
from VARReader import read_var_file_as_dictionary
from BestsTool import create_best_fun_seq_files
from Medians import create_seq_with_values_on_median_files


def main():
    fun = read_fun_file_as_list_of_lists("Resources/FUN.BB12044.tsv")
    var = read_var_file_as_dictionary("Resources/VAR.BB12044.tsv")
    main_dictionary = {}
    count = 0
    for seq in var:
        main_dictionary.update({seq: fun[count]})
        count += 1
    create_best_fun_seq_files(main_dictionary)
    create_seq_with_values_on_median_files(main_dictionary)