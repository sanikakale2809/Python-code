#Match case
inp="abc"
#inp="sun"
match inp:
    case "mon":
        print("Day num 1")
    case "tue":
        print("Day num 2")
    case "wed":
        print("Day num 3")
    case "thr":
        print("Day num 4")
    case "fri":
        print("Day num 5")
    case "sat":
        print("Day num 6")
    case "sun":
        print("Day num 7")
    case _: (
        print("Wrong Input"))