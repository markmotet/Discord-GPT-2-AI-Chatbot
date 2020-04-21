import os
import sys

# def print_conversation(the_conversation):
#     print("<|startoftext|>")
#     if len(the_conversation) % 2 == 0:
#         for i in range(len(the_conversation)):
#             if i % 2 == 0:
#                 print("USER", the_conversation[i][4])
#             else:
#                 print("BOT", the_conversation[i][4])
#     else:
#         for i in range(len(the_conversation)):
#             if i % 2 == 0:
#                 print("BOT", the_conversation[i][4])
#             else:
#                 print("USER", the_conversation[i][4])
#     print("<|endoftext|>")

def print_conversation(the_conversation):
    print("<|startoftext|>")
    for index in range(len(the_conversation)):
        print(the_conversation[index])
    print("<|endoftext|>")

def are_adjacent(line_A, line_B):

    line_num_A = int(line_A[0][1:])
    line_num_B = int(line_B[0][1:])

    if abs(line_num_A - line_num_B) == 1:
        return True
    else:
        return False

def formatted_print(the_list):

    conversation = []

    for i in range(len(the_list) - 1):
        
        sentence = the_list[i][4]
        sentence = sentence.replace("&quot;", "\"")
        sentence = sentence.replace("<U>", "").replace("</U>", "").replace("<u>", "").replace("</u>", "")
        sentence = sentence.replace("<I>", "").replace("</I>", "").replace("<i>", "").replace("</i>", "")
        sentence = sentence.replace("<B>", "").replace("</B>", "").replace("<b>", "").replace("</b>", "")
        conversation.append(sentence)

        if not are_adjacent(the_list[i], the_list[i + 1]):
            print_conversation(conversation)
            conversation = []

    conversation.append(the_list[i + 1][4])
    print_conversation(conversation)


def to_list(the_file):
    lines_list = []
    for line in the_file:
        words = line.split("+++$+++")
        stripped_words = []
        for word in words:
            stripped_words.append(word.strip().replace("  ", " "))
        lines_list.append(stripped_words)
    return lines_list

def test():
    for i in range(10):
        i = i - 1
        print(i)

def main():
    os.system('cls')

    input_file = open(sys.argv[1], "r", encoding="utf-8", errors="ignore")

    input_list = to_list(input_file)
    formatted_print(input_list)

    input_file.close()

if __name__ == "__main__":
    main()