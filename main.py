import requests

API_KEY = "261c1e2701a652fe4cb9e22b5668ab43"
BASE_URL = "https://api.themoviedb.org/3/search/movie"

def show_menu():
    print("\n=== Movie Recommendation CLI ===")
    print("1. Search Movies")
    print("2. View Favorite Movies")
    print("3. Exit")
    
def search_movie():
    title = input("Enter movie title to search: ")
    # Dummy data simulating API response
    params = {
        "api_key": API_KEY,
        "query": title,
        "language": "en-US",
        "page": 1,
        "include_adult": False
    }
    
    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        print("Error fetching data from TMDb API")
        return
    
    data = response.json()
    results = data.get("results", [])
    
    if not results:
        print(f"No results found for '{title}'.")
        return
    
    print(f"\nSearch results for '{title}':")
    for i, movie in enumerate(results[:5], start=1):
        movie_title = movie.get("title", "N/A")
        release_date = movie.get("release_date", "N/A")
        rating = movie.get("vote_average", "N/A")
        print("{}. {} ({}) - Rating: {}".format(i, movie_title, release_date, rating))
    
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