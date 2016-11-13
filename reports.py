# Report functions


def count_games(file_name):
    with open(file_name, "r") as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def decide(file_name, year):
    if str(year) in open(file_name).read():
        return True
    else:
        return False


def get_latest(file_name):
    with open(file_name, "r") as f:
        maxYear = 0
        maxYearsGame = ""
        for line in f:
            name = line.split("\t")[0]
            year = line.split("\t")[2]

            if int(year) > int(maxYear):
                maxYear = year
                maxYearsGame = name

    # print(maxYearsGame + "," + maxYear)
    return maxYearsGame


def count_by_genre(file_name, genre):
    with open(file_name, "r") as f:
        i = 0
        for line in f:
            currentGenre = line.split("\t")[3]
            if genre == currentGenre:
                i = i + 1
    return i


def get_line_number_by_title(file_name, title):
    with open(file_name, "r") as f:
        i = 1
        for line in f:
            currentTitle = line.split("\t")[0]
            if title == currentTitle:
                print(currentTitle)
                return i
            else:
                i = i + 1
        raise ValueError("The requested title is not in the input file.")


def sort_abc(file_name):
    with open(file_name, "r") as f:
        titles = []
        for line in f:
            title = line.split("\t")[0]
            titles.append(title)
    sortedTitles = sorted(titles, key=lambda s: s.lower())
    return sortedTitles


def get_genres(file_name):
    with open(file_name, "r") as f:
        genres = []
        for line in f:
            genre = line.split("\t")[3]
            if not genre in genres:
                genres.append(genre)
    sortedGenres = sorted(genres, key=lambda s: s.lower())
    return sortedGenres


def when_was_top_sold_fps(file_name):
    with open(file_name, "r") as f:
        topFpsYear = 0
        topFpsCopiesSold = 0
        for line in f:
            genre = line.split("\t")[3]
            year = line.split("\t")[2]
            copiesSold = line.split("\t")[1]
            if genre == "First-person shooter":
                if float(copiesSold) > float(topFpsCopiesSold):
                    topFpsCopiesSold = copiesSold
                    topFpsYear = year
        return int(topFpsYear)
