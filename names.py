from testing_code import get_formatted_name, get_formatted_midlle_name

# print("Enter 'q' at any time to quit.")
# while True:
#     first = input("\nPlease give me a first name: ")
#     if first == 'q':
#         break
#     last = input("Please give me a last name: ")
#     if last == 'q':
#         break
#
#     formatted_name = get_formatted_name(first, last)
#     print(f"\nNeatly formatted name: {formatted_name}")

def test_first_last_name():
    """Do names like 'Murodjon Gafforov' work?"""
    formatted_name = get_formatted_name('murodjon', 'gafforov')
    assert formatted_name == 'Murodjon Gafforov'

def test_first_last_middle():
    """Do names like 'Murodjon Gafforov Mukhiddin Ugli' work?"""
    formatted_name = get_formatted_midlle_name('murodjon', 'gafforov', 'mukhiddin ugli')
    assert formatted_name == 'Murodjon Mukhiddin Ugli Gafforov'