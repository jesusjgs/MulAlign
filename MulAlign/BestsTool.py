def create_best_fun_seq_files(dictionaries: dict):
    best_strike = 0
    best_strike_seq = ""
    best_tc = 0
    best_tc_seq = ""
    best_sp = 0
    best_sp_seq = ""

    for key, values in dictionaries:
        if values[0] > best_strike:
            best_strike = values[0]
            best_strike_seq = key
        if values[1] > best_tc:
            best_tc = values[1]
            best_tc_seq = key
        if values[2] > best_sp:
            best_sp = values[2]
            best_sp_seq = key

    strike_file = open("Resources/Best_strike_seq.txt", 'w')
    strike_file.write(best_strike_seq)
    strike_file.close()
    tc_file = open("Resources/Best_tc_seq.txt", 'w')
    tc_file.write(best_tc_seq)
    tc_file.close()
    sp_file = open("Resources/Best_sp_seq.txt", 'w')
    sp_file.write(best_sp_seq)
    sp_file.close()
    strike_file_value = open("Resources/Best_strike_value.txt", 'w')
    strike_file_value.write(best_strike)
    strike_file_value.close()
    tc_file_value = open("Resources/Best_tc_value.txt", 'w')
    tc_file_value.write(best_tc)
    tc_file_value.close()
    sp_file_value = open("Resources/Best_sp_value.txt", 'w')
    sp_file_value.write(best_sp)
    sp_file_value.close()
