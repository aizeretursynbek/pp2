import re


# 1. string that has an 'a' followed by zero or more 'b''s.
pattern1 = r"ab*"
text1 = "abb"
print("1:", bool(re.search(pattern1, text1)))


# 2. 'a' + 2-3 'b'
pattern2 = r"ab{2,3}"
text2 = "abbb"
print("2:", bool(re.search(pattern2, text2)))


# 3. lowercase + underscore + lowercase
pattern3 = r"[a-z]+_[a-z]+"
text3 = "hello_world test_case"
match3 = re.search(pattern3, text3)
print("3:", match3.group() if match3 else "No match")


# 4. одна заглавная + строчные
pattern4 = r"[A-Z][a-z]+"
text4 = "Hello World TEST"
match4 = re.search(pattern4, text4)
print("4:", match4.group() if match4 else "No match")


# 5. начинается с a и заканчивается b
pattern5 = r"^a.*b$"
text5 = "a123b"
print("5:", bool(re.search(pattern5, text5)))


# 6. заменить пробел, запятую, точку на :
pattern6 = r"[ ,.]"
text6 = "Hello, world. Test"
print("6:", re.sub(pattern6, ":", text6))


# 7. snake_case → camelCase
pattern7 = r"_([a-z])"
text7 = "hello_world_test"
print("7:", re.sub(pattern7, lambda m: m.group(1).upper(), text7))


# 8. split по заглавным
pattern8 = r"(?=[A-Z])"
text8 = "HelloWorldTest"
print("8:", re.split(pattern8, text8))


# 9. вставить пробел перед заглавными
pattern9 = r"([A-Z])"
text9 = "HelloWorldTest"
print("9:", re.sub(pattern9, r" \1", text9).strip())


# 10. camelCase to snake_case
text = "userNameTest"

snake = re.sub(r'([A-Z])', r'_\1', text).lower()

print(snake)