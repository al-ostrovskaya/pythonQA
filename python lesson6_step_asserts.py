# Assert_1

expected_result=11
actual_result=15
# ваша реализация, напишите assert и сообщение об ошибке
assert expected_result == actual_result, \
f"expected {expected_result}, got {actual_result}"


#Assert_2
s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')

#Assert_3

full_string="fulltext"
substring="some_value"
def test_substring():
    assert substring in full_string, \
    f"expected {substring} to be substring of {full_string}"

# assert_4
def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"

if __name__ == "__main__":
    test_abs1()
    test_abs2()
    print("Everything passed")


