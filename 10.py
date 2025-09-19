 
def is_substring_present(main_string, sub_string): 
    if sub_string in main_string: 
        return True 
    else: 
        return False 
# Test the function 
main_string = "Hello, welcome to the world of programming!" 
sub_string = "welcome" 
result = is_substring_present(main_string, sub_string) 
if result: 
    print("The substring is present in the main string.") 
else: 
    print("The substring is not present in the main string.")
