def recommend_books_by_genre():
    """
    Reads a list of books and their genres from user input,
    then recommends books based on a genre input by the user.
    """
    books = []
    n = int(input("How many books do you want to enter? "))
    for i in range(n):
        title = input(f"Enter title of book {i+1}: ")
        genre = input(f"Enter genre of book {i+1}: ")
        books.append({"title": title, "genre": genre})

    user_genre = input("Enter genre to get recommendations: ")
    recommended = [book['title'] for book in books if book.get('genre', '').lower() == user_genre.lower()]
    if recommended:
        print("Recommended books for genre '{}':".format(user_genre))
        for title in recommended:
            print("-", title)
    else:
        print("No books found for genre '{}'.".format(user_genre))

if __name__ == "__main__":
    recommend_books_by_genre()


