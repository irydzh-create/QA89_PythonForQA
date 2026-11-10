# # def print_string_reverse(s):
# #     if s is None or s.strip() == "":
# #         print("Wrong String")
# #         return
# #     #else:
# #        #print (s[::-1])
# #     reversed_s = s[::-1]
# #     print(reversed_s)
# #
# # print_string_reverse("Shalom")
# # print_string_reverse(None)
# # print_string_reverse("")
# # print_string_reverse(" ")
# #
# #
# # #========2======
# # def is_isr_phone_number(phone):
# #     if phone is None or phone == "":
# #         return None
# #     if len(phone) != 10:
# #         return False
# #     if phone[0] != "0":
# #         return False
# #     if not phone.isdigit():
# #         return False
# #     return True
# # print(is_isr_phone_number("0521234567"))
# # print(is_isr_phone_number("521234567"))
# # print(is_isr_phone_number("05212345a7"))
# # print(is_isr_phone_number(""))
#
# #3
# def print_substring_reverse(s, start, finish):
#
#     if s is None or s.strip() == "":
#         print("Wrong args")
#         return
#
#     if start < 0 or finish >= len(s) or start > finish:
#         print("Wrong args")
#         return
#
#     beginning = s[:start]
#     middle_reverse = s[start:finish + 1][::-1]
#     end_reverse = s[finish + 1:]
#
#     print(beginning+middle_reverse+end_reverse)
#
# print_substring_reverse("Shalom", 1, 3)
# print_substring_reverse("Python", 1, 4)
# print_substring_reverse("", 1, 3)
# print_substring_reverse("Hello", 2, 10)
#
# # # User input
# # s = input("Enter a string: ")
# # start = int(input("Enter start index: "))
# # finish = int(input("Enter finish index: "))
# #
# # print_substring_reverse(s, start, finish)
#
# #4
#
# def get_words_reverse(s):
#     words = s.split()
#     reversed_words = words[::-1]
#     result = " ".join(reversed_words)
#     return result
#
#
# print(get_words_reverse("Hello my nice world"))
#
# # User input
# s = input("Enter a sentence: ")
# print(get_words_reverse(s))
#
def print_words_reverse_in_column(s):
    words = s.split()

    for word in words:
        reversed_word = word[::-1]
        print(reversed_word)


print_words_reverse_in_column("Hello my nice world")

