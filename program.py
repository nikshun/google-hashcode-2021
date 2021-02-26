import statistics


def solve(fileObj, libComparator):
    # foreach library - sort the books
    libraries = fileObj.libraries

    for lib in libraries:
        lib.booksIds = sorted(lib.books, key=lambda b: -b.score)

    # sort the libraries
    libraries = sorted(libraries, key=lambda lib: -libComparator(lib))

    # keep track of processed books
    finished = [False] * fileObj.nbOfBooks

    # create the solution object
    for lib in libraries:
        for book in lib.books:
            if not finished[book.id]:
                finished[book.id] = True
                lib.scannedBooks.append(book)

    # don't include libraries that don't have books to scan
    libraries = list(filter(lambda lib: len(lib.scannedBooks) > 0, libraries))

    return libraries

###################### Library comparison functions ######################
# if the library's score is high, then it will be processed early


def libScoreCombined(lib):
    bookMean = statistics.mean([book.score for book in lib.books])
    return bookMean / lib.signUpTime


def libScoreReversedSignup(lib):
    return 1 / lib.signUpTime


def libScoreNaive(lib):
    mean = statistics.mean([book.score for book in lib.books])
    scanTime = len(lib.books) / lib.scanningPower
    return mean / (lib.signUpTime + scanTime)