def is_palindrome(word):
    word = word.replace(" ", "").lower()
    if word == word[::-1]:
        return True
    else:
        return False
        input_word = input("Введіть слово: ")
        if is_palindrome(input_word)
            print("Це слово є паліндромом")
            else:
            print("Це слово не є паліндромом")
