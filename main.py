def show_menu():
    print("\n=== Movie Recommendation CLI ===")
    print("1. Search Movies")
    print("2. View Favorite Movies")
    print("3. Exit")
    
def search_movie():
    title = input("Enter movie title to search: ")
    # Dummy data simulating API response
    dummy_results = [
        {"title": "The Matrix", "year": 1999, "rating": 8.7},
        {"title": "Matrix Reloaded", "year": 2003, "rating": 7.2},
        {"title": "Matrix Revolutions", "year": 2003, "rating": 6.8},
        {"title": "The Matrix Resurrections", "year": 2021, "rating": 5.7},
        {"title": "Inception", "year": 2010, "rating": 8.8}
    ]
    
    print("\nSearch results for '{}':".format(title))
    for i, movie in enumerate(dummy_results[:5],start=1):
        print("{}. {} ({}) - Rating: {}".format(i, movie['title'], movie['year'], movie['rating']))
    
def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            search_movie()
        elif choice == "2":
            print("Feature coming soon: View Favorite Movies")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()