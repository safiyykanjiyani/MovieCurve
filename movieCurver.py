from filechooser import chooseInputFile, chooseOutputFile

def writeFile(output):
    documentationText = [
                    "The program works initially by sorting your list, then assigning scores to",
                    "your moves, and exporting them to a file. The distribution of score is as follows:",
                    "10/10 is given to the top 3%",
                    "9/10 is given to the top 5%",
                    "8/10 is given to the top 8%",
                    "7/10 is given to the top 11%",
                    "6/10 is given to the top 14%",
                    "5/10 is given to the top 18%",
                    "4/10 is given to the top 14%",
                    "3/10 is given to the top 11%",
                    "2/10 is given to the top 8%",
                    "1/10 is given to the top 5%",
                    "0/10 is given to the top 3%"
                    ]

    print("You will now be redirected to select the file to output to")
    while True:
        confirmation = input("Please say yes (Y) to confirm.\n")
        if confirmation == "Y":
            break

    while True:
        filename = chooseOutputFile()
        if filename != "":
            break
    f = open(filename, "w")

    for i in output:
        f.write(i[0] + "\t" + i[1] + "\t" + i[2] + "\n")


    while True:
        documentation = input("Would you like to learn more about the distribution? (Y or N)\n")
        if documentation == "N":
            print("Have a great day!")
            exit()
        elif documentation == "Y":
            for i in documentationText:
                print(i)
            exit()

def quickSort(arr):
    less = []
    pivotList = []
    more = []

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in range(len(arr)):
            while True:
                judge = input("Is " + arr[i][1] + " better than " +  pivot[1] + " or the same? (Y, N, or S)\n")
                if judge == "N":
                    less.append(arr[i])
                    break
                elif judge == "Y":
                    more.append(arr[i])
                    break
                elif judge == "S":
                    pivotList.append(arr[i])
                    break
                else:
                    print("Please respond yes (Y), no (N) or the same (S)")
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more

def normalize(movieDate, done):
    size = len(movieDate)
    placeholderIndex = 0
    sorted, distributionStandards = [None] * size, [
                                                    int(size / 33.33),
                                                    int(size / 20),
                                                    int(size / 12.5),
                                                    int(size / 9.09),
                                                    int(size / 7.14),
                                                    int(size / 5.55),
                                                    int(size / 7.14),
                                                    int(size / 9.09),
                                                    int(size / 12.5),
                                                    int(size / 20),
                                                    int(size / 33.33)
                                                    ]

    if done != True:
        print("The following process is time intensive and will ask you to \ncompare movies to sort them.")
        movieDate = quickSort(movieDate)


    for i in range(len(distributionStandards)):
        if i == 10:
            for j in range(placeholderIndex, size):
                sorted[j] = str(10 - i)
        else:
            for j in range(placeholderIndex, placeholderIndex + distributionStandards[i]):
                sorted[j] = str(10 - i)
            placeholderIndex += distributionStandards[i]

    output = []
    for i in range(size):
        output.append((movieDate[i][0], movieDate[i][1], sorted[i]))
    writeFile(output)


def dataCompiling(movieFile):
    movieList = movieFile.readlines()
    movieDate, date, movie = [], "", ""
    for i in movieList:
        i = i.strip()
        date = i[0:4]
        movie = i[5:len(i)]
        movieDate.append((date, movie))
    while True:
        normal = input("Is this properly ranked from best to worst? (Y or N)\n")
        if normal == "N":
            normalize(movieDate, False)
            break
        elif normal == "Y":
            while True:
                insert = input("Would you like to insert a movie to the list? (Y or N)\n")
                if insert == "Y":
                    date = input("What year?\n")
                    movie = input("What movie?\n")
                    while True:
                        nextTo = input("What movie is it next to?\n")
                        for i in range(len(movieDate)):
                            present = movieDate[i][1].find(nextTo)
                            if present != -1:
                                while True:
                                    compare = input("Was " + movie + " better than " + nextTo + "? (Y or N)\n")
                                    if compare == "Y":
                                        if len(movieDate) == i:
                                            movieDate.append((date, movie))
                                            normalize(movieDate, True)
                                        else:
                                            movieDate.insert(i + 1, (date, movie))
                                            normalize(movieDate, True)
                                    elif compare == "N":
                                        movieDate.insert(i, (date, movie))
                                        normalize(movieDate, True)
                                    else:
                                        print("Please only answer better (B) or worse (W).")
                        print("Couldn't find that film, please try again!")
                elif insert == "N":
                    normalize(movieDate, True)
                    exit()

        else:
            print("Choose Yes (Y) or No (N)")

def filePrep():
    introMessage = [
                    "This program works to assign a normal distribution to a list of movies.",
                    "The proper format of the input file will be publication date followed by",
                    "a tab space and the movie title. You will now be redirected to select",
                    "your movie file."
                   ]

    for i in introMessage:
        print(i)

    while True:
        confirmation = input("Please say yes (Y) to confirm.\n")
        if confirmation == "Y":
            break

    while True:
        filename = chooseInputFile()
        if filename != ():
            if filename != '':
                break

    movieFile = open(filename, "r")
    dataCompiling(movieFile)

if "__main__" == __name__:
    filePrep()
