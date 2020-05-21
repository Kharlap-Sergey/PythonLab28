from dormitory import Dormitory
from Operation import Operation
from datamanip import Datamainp

def main():
    inf = Datamainp.read_and_separate_information_by_string("in.txt")
    dorm = Operation.getDormitory(inf)
    ans = dorm.get_dormitory_level_duty(1) + "\n\n\n" + str(dorm)
    Datamainp.print_to_file("out.txt",ans)
main()


