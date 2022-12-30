import sys

if __name__ == "__main__":
    if len(sys.argv) == 4:
        filename = sys.argv[1]
        numberOfTickets = int(sys.argv[2])
        parameter = int(sys.argv[3])
        with open(filename, 'r', encoding='UTF-8') as file:
            for line in file:
                student = line.rstrip()
                studentHash = hash(line.rstrip() + str(parameter))
                print(student + ": " + str(studentHash % numberOfTickets + 1))
    else:
        print("Wrong number of arguments")

