class Datamainp():
    """this class was disigned for file and data manipulation"""
    @staticmethod
    def print_to_file(filename, string):
        fout = open(filename, "w+")
        fout.write(string)
        fout.close()   

    @staticmethod
    def read_and_separate_information_by_string(filename):
        fin = open(filename)
        inf = fin.readlines()
        fin.close()
        return inf
