def calculateFinalScore(inputObj, libs):
    currentDay = 0
    score = 0
    scanned = [False] * inputObj.nbOfBooks

    for lib in libs:
        currentDay += lib.signUpTime

        # exit if the sign took too long
        if currentDay > inputObj.nbOfDays:
            break

        for i, book in enumerate(lib.scannedBooks):
            # exit if the due date has been reached
            if (currentDay + i // lib.scanningPower) > inputObj.nbOfDays:
                break

            # add the score of the book, if it hasn't been scanned yet
            if not scanned[book.id]:
                scanned[book.id] = True
                score += book.score

    return score