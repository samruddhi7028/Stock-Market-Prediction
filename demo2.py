
movies = {
    "Action": ["Avengers", "John Wick", "Mission Impossible"],
    "Comedy": ["The Mask", "3 Idiots", "PK"],
    "Drama": ["Forrest Gump", "The Shawshank Redemption", "Titanic"],
    "Sci-Fi": ["Interstellar", "Inception", "The Matrix"],
    "Horror": ["Conjuring", "IT", "Annabelle"]
}

print("Available genres:")
for genre in movies:
    print("-", genre)

user_choice = input("\nEnter your preferred genre: ").title()

if user_choice in movies:
    print("\nRecommended movies for you:")
    for movie in movies[user_choice]:
        print("•", movie)
else:
    print("\nSorry, genre not found. Please try again.")