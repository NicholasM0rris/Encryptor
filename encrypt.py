import sys
import time


def main(arglist):
    if len(sys.argv) == 1:
        input_required = input("Enter filename? (Y/N) ")
        if input_required == 'Y' or input_required == 'y' or input_required == 'yes' or input_required == 'Yes':
            input_file = input("Enter name of file to encrypt: (Remember to include path and extension) ")
        else:
            print("No file to encrypt specified... ! Closing program...")
            time.sleep(3)
            sys.exit("No file to encrypt specified... !")
        if 'input_file' in locals():
            print('encrypting ', input_file, '...')
            file = input_file
        else:
            file = arglist[0]
    else:
        file = arglist[0]
    # Open file
    start = time.time()
    try:
        f = open(file, 'r')
    except:
        print("File not found or error finding file! ")
        time.sleep(3)
        sys.exit("File not found or error finding file! ")
    # Read paragraphs

    text = f.readlines()
    # Makes list of paragraphs
    paragraphs = list(text)

    '''
    TESTING
    '''
    # print('text0: ', list(text[0]))
    # print('text: ', list(paragraphs))
    '''
    TESTING
    '''
    encrypted_list = []
    # encrypt
    for paragraph in paragraphs:
        # print('paragraph', list(paragraph))
        encrypted_text = encrypt(list(paragraph))
        encrypted_list.append(encrypted_text)

    # print('enlist', encrypted_list)
    # print('entxt', encrypted_text)
    # Print to file
    f.close()
    if 'input_file' in locals():
        f = open(input_file, "w+")
        for someparagraph in encrypted_list:
            for someletter in someparagraph:
                f.write("%s" % someletter)
    else:
        f = open(arglist[0], "w+")
        for someparagraph in encrypted_list:
            for someletter in someparagraph:
                f.write("%s" % someletter)

    print("Encryption complete in", -start + time.time(), 'seconds!')
    time.sleep(2)
    sys.exit("Successful encryption")


def encrypt(text):
    """
    Takes a list of paragraphs and encrypts it, returning the encrypted list of characters
    :param text: Takes a list of paragraphs
    :return: list of characters as encrypted text
    """

    for i in range(len(text)):
        """
        Change every even +3
        Change every odd -2
        Change every third letter +index%10
        Change every fifth letter -index%10 + 2
        Change every eleventh letter to +(index * 2)%7
        """
        # print('test', chr(ord('z') + 4))
        # print('here', text[i])

        if text[i] is not ' ' and text[i] is not '\n':
            if i % 2 == 0:
                text[i] = chr(ord(text[i]) + 3)

            if i % 2 != 0:
                text[i] = chr(ord(text[i]) - 2)

            if i % 3 == 0:
                text[i] = chr(ord(text[i]) + (i % 4))
            if i % 5 == 0:
                text[i] = chr(ord(text[i]) - ((i % 6) + 2))
            if i % 11 == 0:
                text[i] = chr(ord(text[i]) - ((i * 2) % 4))
    return text


if __name__ == '__main__':
    main(sys.argv[1:])
