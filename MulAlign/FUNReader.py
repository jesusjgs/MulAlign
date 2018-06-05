def read_fun_file_as_list_of_lists(file_name: str):
    fun_file = open(file_name, 'r')
    main_list = []
    secondary_list = []
    line = fun_file.readline()
    while line:
        # Create new list pair with this line as id
        read_values = str.strip(line).split(' ')
        for i in read_values:
            secondary_list.append(i)
        # Concatenate the line to the last value of the last list
        main_list.append(secondary_list)
    fun_file.close()
    return main_list
