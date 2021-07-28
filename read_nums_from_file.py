def read_nums_from_file(file, num_converter) -> list:
    return list(list(num_converter(x) for x in line.split()) for line in file)
