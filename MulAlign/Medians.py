from statistics import median


def create_seq_with_values_on_median_files(dictionaries: dict):
    items_to_median = dictionaries.items()
    strike_list = []
    tc_list = []
    sp_list = []
    for item in items_to_median:
        strike_list.append(item[0])
        tc_list.append(item[1])
        sp_list.append(item[2])
    strike_median = median(strike_list)
    tc_median = median(tc_list)
    sp_median = median(sp_list)

    strike_median_seqs_to_print = []
    tc_median_seqs_to_print = []
    sp_median_seqs_to_print = []
    for key, value in dictionaries:
        if value[0] == strike_median:
            strike_median_seqs_to_print.append(key)
        if value[1] == tc_median:
            tc_median_seqs_to_print.append(key)
        if value[2] == sp_median:
            sp_median_seqs_to_print.append(key)

    strike_file = open("Resources/median_strike_seq.txt", 'w')
    strike_file.write(strike_median_seqs_to_print)
    strike_file.close()
    tc_file = open("Resources/median_tc_seq.txt", 'w')
    tc_file.write(tc_median_seqs_to_print)
    tc_file.close()
    sp_file = open("Resources/median_sp_seq.txt", 'w')
    sp_file.write(sp_median_seqs_to_print)
    sp_file.close()
    strike_file_value = open("Resources/median_strike_value.txt", 'w')
    strike_file_value.write(strike_median)
    strike_file_value.close()
    tc_file_value = open("Resources/median_tc_value.txt", 'w')
    tc_file_value.write(tc_median)
    tc_file_value.close()
    sp_file_value = open("Resources/median_sp_value.txt", 'w')
    sp_file_value.write(sp_median)
    sp_file_value.close()
