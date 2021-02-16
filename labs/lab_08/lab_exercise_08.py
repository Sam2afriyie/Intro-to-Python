import csv

# START LAB EXERCISE 08
print('Lab Exercise 08 \n')

# PROBLEM 1 (5 Points)
def read_csv_file(input_filepath, delimiter=','):
    """
    This function reads a .csv file and parses it into a list of dictionaries,
    where each dictionary is formed from the data on one line of the .csv file.

    Parameters:
        filepath (str): The location of the file to read and parse.
        delimiter (str): delimiter that overrides the default

    Returns:
        list: A list of dictionaries, where each dictionary is one row from the
            input file.
    """
    with open(input_filepath, 'r', encoding='utf-8') as file_obj:
        data = []
        reader = csv.DictReader(file_obj, delimiter=delimiter)
        for row in reader:
            data.append(row)
        return data

# PROBLEM 2 (5 Points)
def hci_database_urls(library_list):
    """
    This function takes a list of library data and returns a new dictionary of databases in the HCI category.
    only the name of the database and the link to the database will be included.

    Parameters:
        library_list (list): A list of dictionaries, where each dictionary contains the
            information on a specific databas.

    Returns:
        dict: A dictionary where the keys are the name of the HCI database and its permalink
    """
    {'Category': 'African Studies',
    'Name': 'Africa Bib',
    'Format': 'Database',
    'Type': 'Article Index',
    'Description': 'Indexes over 500 journals related to Africa'
    }
    data = {}
    for database in library_list:
        if database['Category'] == "Human Computer Interaction":
            name =  database['Name']
            link = database['Permalink']
           # data[database['Name']] = database['Permalink']
           # data['Africa Bib'] = database['Permalink']
            data[name] = link

    return data


# PROBLEM 3 (5 Points)
def write_csv_file(output_filepath, dict_to_write, header):
    """
    Writes a .csv file using the < csv > module.

    Parameters:
        output_filepath (str): The file path to the new file being created.
        dict_to_write (dict): The information to include in the file being created.
        header (list): The header row in the table.

    Returns:
        None
    """
    #open csv writer
    with open(output_filepath, 'w', encoding='utf-8') as file_obj:
        #get csv writer
        writer = csv.writer(file_obj)
        #use the writer to write the header
        writer.writerrow(header)

        for k, v in dict_to_write.items():
            row = (k, v)
            #row = [k, v]
            #write the row
            writer.writerrow(row)

# PROBLEM 4 (5 Points)
def main():
    """
    Entry point for the program. This function will process the library data.

    Parameters:
        None

    Returns:
        None
    """
    data = read_csv_file('library_databases.csv', delimiter=',')
    print(data)
    data_dict = hci_database_urls(data)
    print(data_dict)
    header = ['Name', 'Permalink']
    write_csv_file("library_hci_databases.csv", data_dict, header)

if __name__ == '__main__':
    main()
