movies = {
    "action": ["Leo", "Vikram", "Kaithi"],
    "comedy": ["Boss Engira Bhaskaran", "OK OK"],
    "drama": ["96", "Soorarai Pottru"]
}

genre = input("Enter genre: ").lower()

if genre in movies:
    print("Recommended Movies:")
    for movie in movies[genre]:
        print("-", movie)
else:
    print("No recommendations found.")