import sys
import time
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename


class menu_class:
    def __init__(self, window, filename=None):
        window.title("Encryptor")
        root_menu = tk.Menu(window)
        window.config(menu=root_menu)
        file_menu = tk.Menu(root_menu)  # it intialises a new sub menu in the root menu
        root_menu.add_cascade(label="File", menu=file_menu)  # it creates the name of the sub menu
        file_menu.add_command(label="Open files", command=self.get_file_name)
        file_menu.add_separator()  # it adds a line after the 'Open files' option
        file_menu.add_command(label="Exit", command=window.quit)

        tk.Button(window, text='Confirm', bg='light green', command=self.add_file_name).grid(row=2, column=2,
                                                                                             sticky=tk.W, pady=4)

        tk.Button(window, text='Encrypt', bg='red', command=self.set_encrypt).grid(row=7, column=1, sticky=tk.W, pady=4)
        tk.Button(window, text="Decrypt", bg='green', command=self.set_decrypt).grid(row=7, column=2, sticky=tk.W,
                                                                                     pady=4)

        tk.Button(window, text='Quit', bg='red', command=window.quit).grid(row=10, column=4, sticky=tk.W, pady=4)
        tk.Button(window, text="Start", bg='light green', command=self.crypt_process).grid(row=10, column=0,
                                                                                           sticky=tk.W, pady=4)
        tk.Label(window,
                 text="Enter file path/name").grid(row=2)

        self.e1 = tk.Entry(window)
        self.e1.grid(row=2, column=1)
        tk.Label(window,
                 text='File selected: ',
                 fg="black",
                 bg="light grey",
                 font="Verdana 10 bold").grid(row=6)
        self.window = window
        self.filename = filename
        # Decrypt is 0, encrypt is 1
        self.option = 1
        self.file_selected_text = tk.StringVar()
        self.file_selected_text.set('No file selected')
        self.label = tk.Label(self.window,
                              textvariable=self.file_selected_text,
                              fg="black",
                              bg="light grey",
                              font="Verdana 10 bold").grid(row=6, column=1)
        self.option_selected_text = tk.StringVar()
        self.option_selected_text.set("Encrypt selected")
        self.option_label = tk.Label(self.window,
                                     textvariable=self.option_selected_text,
                                     fg="red",
                                     bg="light grey",
                                     font="Verdana 10 bold")
        self.option_label.grid(row=8, column=1)

    def get_file_name(self):
        self.filename = askopenfilename()
        self.file_selected_text.set(self.filename)

    def add_file_name(self):
        self.filename = self.e1.get()
        self.file_selected_text.set(self.filename)

    def set_encrypt(self):
        self.option = 1
        self.option_label.config(fg="red")
        self.option_selected_text.set("Encrypt selected")

    def set_decrypt(self):
        self.option = 0
        self.option_label.config(fg="green")
        self.option_selected_text.set("Decrypt selected")

    def display_filename(self):
        return self.filename

    def crypt_process(self):
        """
        Process of crypting a file
        :param option: choose to encrypt or decrypt
        :param file: File to crypt
        :return: success or error
        """
        option = self.option
        file = self.filename
        start = time.time()
        try:
            f = open(file, 'r')
        except:
            messagebox.showerror('ERROR!', 'File not found or error finding file!')
            return 1
        # Read paragraphs

        text = f.readlines()
        # Makes list of paragraphs
        paragraphs = list(text)

        crypted_list = []
        # encrypt
        if option == 1:
            for paragraph in paragraphs:
                # print('paragraph', list(paragraph))
                crypted_text = encrypt(list(paragraph))
                crypted_list.append(crypted_text)
        else:
            for paragraph in paragraphs:
                crypted_text = decrypt(list(paragraph))
                crypted_list.append(crypted_text)

        # Print to file
        f.close()

        f = open(file, "w+")
        for someparagraph in crypted_list:
            for someletter in someparagraph:
                f.write("%s" % someletter)
        f.close()
        messagebox.showinfo('Complete!', ('Cryption complete in', -start + time.time(), 'seconds!'))

        return 0


def encrypt(text):
    """
    Takes a list of paragraphs and encrypts it, returning the encrypted list of characters
    :param text: Takes a list of paragraphs
    :return: list of characters as encrypted text
    """

    for i in range(len(text)):

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


def decrypt(text):
    """
    Takes a list of paragraphs and decrypts it, returning the decrypted list of characters
    :param text: Takes a list of paragraphs
    :return: list of characters as decrypted text
    """
    for i in range(len(text)):

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


def main(arglist):
    window = tk.Tk()
    # creating a root menu to insert all the sub menus
    menu = menu_class(window)
    window.mainloop()
    # messagebox.showinfo("Status", "Operation complete!")


if __name__ == '__main__':
    main(sys.argv[1:])
