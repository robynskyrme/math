

def handle(chunk):

    for idspi in chunk:

        length = len(idspi)
        if length == 9:
            name(idspi)
        if length == 10:
            vessel(idspi)
        if length == 11:
            edition(idspi)




def name(idspi):
    print(f"ID {idspi} is a name")

    name = ["",""]
    cont = int(idspi[4:9])
    if cont > 17575:
        cont = cont % 17575
    name = deinterlace26(str(cont),name)
    name = deinterlace26(idspi[0:3],name)


    print(name,"\n")


def vessel(idspi):
    print("ID is a vessel")

def edition(idspi):
    print(f"ID {idspi} is an edition")

    year = idspi[0:2]
    index = idspi[2]
    initials = idspi[3:6]
    threechars = idspi[6:11]

    print (f"--{year}", index, deinterlace26(initials,["",""]), deinterlace26(threechars,[""]),"\n")

def deinterlace26(slab,columns):

    if columns == []:
        return

    colcount = len(columns)

    code = int(slab)
    index = 0

    while code:
        char = code % 26
        columns[(index % colcount)] = chr(char+64) + columns[(index % colcount)]
        code = (code - char) // 26
        index += 1

    return columns




def generate(iname,fname,title,year):
    title = title.upper()
    title = base26(title[0:3])

    initials = fname[0] + iname[0]
    initials = base26(initials)

    year = year % 100
    index = 1

    id = str(year) + str(index) + str(initials).zfill(3) + str(title).zfill(5)

    return id




def base26(slab):
    result = 0
    power = 0
    while slab:
        char = slab[-1]
        result += (ord(char)-64) * (26**power)
        slab = slab[:-1]
        power += 1
    return result



if __name__ == "__main__":
    handle(["112001078",
            "24154013053",
            "540005657",
            "25111204308",
            "24123713090",
            "237001033",
            "487007851",
            "270010544",
            "270028119"
            ])

    test = generate("Dillon","Ellen","Fare Thee Well Miss Carousel",2023)
    handle([test])

    test = generate("Marsh","Alex","Southease",2025)
    handle([test])

    test = generate("Cassels","Imogen","Chesapeake",2022)
    handle([test])
