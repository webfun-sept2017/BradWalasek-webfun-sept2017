
def stars(arr):

    for count in range(0,len(arr)):
        # print arr[count]
        starNumber = ""
        if isinstance(arr[count], int) == True:
            for altcount in range(0, arr[count]):
                starNumber += "*"
            print starNumber
        else:
            for altcount in range(0, len(arr[count])):
                l = arr[count][0].lower()
                starNumber += l
            print starNumber
# x = [4, 6, 1, 3, 5, 7, 25]

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
stars(x)
