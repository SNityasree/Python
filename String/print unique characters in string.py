def find_missing_characters(input_string):
     full_set = 'abcdefghijklmnopqrstuvwxyz0123456789'
      full_set_chars = set(full_set)
     input_chars = set(input_string)
      missing_chars = full_set_chars - input_chars
      missing_chars_sorted = ''.join(sorted(missing_chars))
    
    return missing_chars_sorted

def main():
    user_input = input("Enter the string: ")
   result = find_missing_characters(user_input)
    print("Missing characters:", result)
main()
