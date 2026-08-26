#Match Cases
match "MT":
    case "BI":
        print("Running BI code")
    case "MT":
        print("Running MT code")
    case "MS":
        print("Running MS code")
    case "CD":
        print("Running CD code")
    case "CW":
        print("Running CW code")
    case _: (
        print("Wrong Input"))