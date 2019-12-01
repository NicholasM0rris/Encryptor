import sys
import time

def main(arglist):
    if len(sys.argv) == 1:
        input_required = input("Enter filename? (Y/N) ")
        if input_required == 'Y' or input_required == 'y' or input_required == 'yes' or input_required == 'Yes':
            input_file = input("Enter name of file to decrypt: (Remember to include path and extension) ")
        else:
            print("No file to decrypt specified... ! Closing program...")
            time.sleep(3)
            sys.exit("No file to decrypt specified... !")
        if 'input_file' in locals():
            print('decrypting ', input_file, '...')
            file = input_file
        else:
            file = arglist[0]
    else:
        file = arglist[0]
    # Open file
    try:
        f = open(file, 'r')
    except:
        print("File not found or error finding file! ")
        time.sleep(3)
        sys.exit("File not found or error finding file! ")

    text = f.readlines()
    paragraphs = list(text)
    decrypted_list = []
    for paragraph in paragraphs:
        # print('paragraph', list(paragraph))
        decrypted_text = decrypt(list(paragraph))
        decrypted_list.append(decrypted_text)

    f.close()
    if 'input_file' in locals():
        f = open(input_file, "w+")
        for someparagraph in decrypted_list:
            for someletter in someparagraph:
                f.write("%s" % someletter)
    else:
        f = open(arglist[0], "w+")
        for someparagraph in decrypted_list:
            for someletter in someparagraph:
                f.write("%s" % someletter)
    # f.write("\n\n%s" % "EL PSY CONGROO")
    print("Decryption complete! \n EL PSY CONGROO ")
    time.sleep(3)
    sys.exit("Decryption complete! \n EL PSY CONGROO ")

def decrypt(text):
    """
    Takes a list of paragraphs and decrypts it, returning the decrypted list of characters
    :param text: Takes a list of paragraphs
    :return: list of characters as decrypted text
    """
    for i in range(len(text)):
        """
        Change every even +3
        Change every odd -2
        Change every third letter +index%10
        Change every fifth letter -index%10 + 2
        Change every eleventh letter to +(index * 2)%7
        """

        if text[i] != ' ' and text[i] is not '\n':
            if i % 11 == 0:
                text[i] = chr(ord(text[i]) + ((i * 2) % 4))
            if i % 5 == 0:
                text[i] = chr(ord(text[i]) + ((i % 6) + 2))
            if i % 3 == 0:
                text[i] = chr(ord(text[i]) - (i % 4))
            if i % 2 != 0:
                text[i] = chr(ord(text[i]) + 2)
            if i % 2 == 0:
                text[i] = chr(ord(text[i]) - 3)
    return text


if __name__ == '__main__':
    main(sys.argv[1:])
