def is_unique(line):
    for i in line:
        if line.count(i) > 1:
            print(f"{i} in string \"{line}\" is not unique.")
            return
    print(f"the string \"{line}\" is all unique.")

def check_permutation(line1, line2):
    for i in line1:
        if line1.count(i) == line2.count(i):
            pass
        else:
            print(f"the strings \"{line1}\" and \"{line2}\" are NOT permutations.")
            return(False)
    print(f"the strings \"{line1}\" and \"{line2}\" ARE permutations.")
    return(True)

def URLify(line):
    line = line.replace(" ", "%20")
    print("Modified string:", line)

def palindrome_permutation(line):
    line = line.lower()
    catch = 0  
    for i in line:
        if i != " ":
            if line.count(i) % 2 == 0:
                pass
            else:
                #print("the letter", i, "is in here an odd amount of times")
                catch += 1
    if catch > 1:
        print(f"the string \"{line}\" is NOT a permutation of a palindrome.")            
    else:
        print(f"the string \"{line}\" IS a permutation of a palindrome.")    

def test_driver():
    print("\nIs Unique tests: ")
    is_unique("here is a test")
    is_unique("The quick brown fox jumped over the lazy dog")
    is_unique("abcdefghijklmnopqrstuvwxyz")
    is_unique("1234567890")
    is_unique("1112345567")

    print("\nCheck Permutation tests: ")
    check_permutation("here is a test", "here is another test")
    check_permutation("here is a test", "test a is here")
    check_permutation("my name is dallin", "nillad si eman ym")
    check_permutation("1234560", "654321")

    print("\nURLify tests: ")
    URLify("here is a test")
    URLify("numbers: 412 11231 1251 ")

    print("\npalindrome_permutation tests: ")
    palindrome_permutation("Test")
    palindrome_permutation("taco cat")
    palindrome_permutation("Tact Coa")
    palindrome_permutation("Hannah")
    palindrome_permutation("nnahh")

test_driver()

