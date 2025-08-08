#  Sum of User-Entered Integers
print("\n--- Sum of Integers ---")
user_input = input("Enter integers separated by spaces: ")
int_list = [int(num) for num in user_input.split()]
total = sum(int_list)
print("Sum of the integers:", total)

#  Tuple of Favorite Fiction Books
print("\n--- Favorite Fiction Books ---")
favorite_books = ("Sherlock Holmes", "Dracula", "Frankenstein", "The Time Machine", "The Invisible Man")
print("Here are five of my favorite fiction books:")
for book in favorite_books:
    print(book)

#  Dictionary to Store Person Info
print("\n--- Personal Information ---")
person_info = {}
person_info["name"] = input("Enter your name: ")
person_info["age"] = input("Enter your age: ")
person_info["favorite_color"] = input("Enter your favorite color: ")
print("Person Information:", person_info)

#  Common Elements in Two Sets
print("\n--- Common Elements in Sets ---")
set1_input = input("Enter integers for Set 1 (space-separated): ")
set2_input = input("Enter integers for Set 2 (space-separated): ")
set1 = set(map(int, set1_input.split()))
set2 = set(map(int, set2_input.split()))
common_elements = set1.intersection(set2)
print("Common elements:", common_elements)

#  List Comprehension for Odd-Length Words
print("\n--- Words with Odd Number of Characters ---")
words_input = input("Enter words separated by spaces: ")
words = words_input.split()
odd_length_words = [word for word in words if len(word) % 2 != 0]
print("Words with odd number of characters:", odd_length_words)

