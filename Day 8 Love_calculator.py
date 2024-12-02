def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()

#TODO: Calculate the count of letters in "TRUE"
    true_count = combined_names.count('t') + combined_names.count('r') + combined_names.count(
        'u') + combined_names.count('e')

#TODO: Calculate the count of letters in "LOVE"
    love_count = combined_names.count('l') + combined_names.count('o') + combined_names.count(
        'v') + combined_names.count('e')

#TODO: Combine the counts to form the love score
    love_score = int(f"{true_count}{love_count}")
    print(love_score)
calculate_love_score("Alisha", "Tuba")  # Should output 42
