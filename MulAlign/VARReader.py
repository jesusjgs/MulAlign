def read_var_file_as_dictionary(file_name:str):
    fasta_file = open(file_name, 'r')
    dictionaries_list = []
    main_dictionary_of_sequences = {}
    last_id = ""
    for line in fasta_file:
        if line[0] == '>':
            dictionaries_list.append(main_dictionary_of_sequences)
            blank_string = ""
            main_dictionary_of_sequences.update({line[1:]: blank_string})
            last_id = str.strip(line[1:])
        else:
            last_line = main_dictionary_of_sequences[last_id]
            updated_line = str.strip(last_line + line)
            main_dictionary_of_sequences.update({last_id: updated_line})
    dictionaries_list.appen(main_dictionary_of_sequences)
    dictionaries_list.pop(0)
    fasta_file.close()
    return main_dictionary_of_sequences
