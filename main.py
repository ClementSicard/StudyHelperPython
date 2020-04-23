import numpy as np
import os
import time
import pandas as pd
import getpass
import platform


# UPDATE YOUR THE PATH TO YOUR DIRECTORY
path = "[PATH TO YOUR DIRECTORY]"


clear_command = "cls" if platform.system() == "Windows" else "clear"


def quitAnim():
    os.system(clear_command)
    print("Don't give up !!")
    time.sleep(1)
    quit()


while True:
    os.system(clear_command)

    # Getting back to original directory
    os.chdir(path)

    # List current directories
    dir_list = next(os.walk('.'))[1]

    # Choose the subject
    try:
        class_list = open("courses.txt")

    except IOError:
        print('Unable to find the classes file. Exiting')
        time.sleep(10)
        quit()

    summary = dict()

    i = 1
    for line in class_list:
        line = line.rstrip()
        if line[:2] != "//" and line[:1] != '\n':
            print('[%d]' % i, line)
            summary[i] = line
            i += 1
    print('\n[Q] Quit')

    while True:
        try:
            choice = input('> ')
            if choice.upper() == 'Q':
                quitAnim()
            elif int(choice) <= i:
                s = summary[int(choice)]
                os.chdir(s)
                break
            else:
                print("Wrong input. Please type in a number between '1' and '%d'" % (
                    i - 1), "or 'Q'")
        except ValueError:
            print("Wrong input. Please type in a number between '1' and '%d'" %
                  (i - 1), "or 'Q'")
        except KeyboardInterrupt or EOFError:
            print("Keyboard interruption")
            print("Quitting...")
            time.sleep(2)
            quit()
    del(choice)

    # Random selection or not
    while True:
        try:
            choice = input('Random ? [y/n] : ').upper().strip()
            if choice == 'Y':
                random = True
                break
            elif choice == 'N':
                random = False
                break
            else:
                print('Wrong value. Please try again.')
        except KeyboardInterrupt or EOFError:
            print("Keyboard interruption")
            print("Quitting...")
            time.sleep(2)
            quit()
    del(choice)

    os.system(clear_command)

    summary = dict()
    subjects_r = pd.read_csv('subjects.csv')
    chapters = subjects_r.columns.tolist()

    print(s.upper(), "\n\n")
    i = 1
    for chapter in chapters:
        print('[%d]' % i, chapter)
        summary[i] = chapter
        i += 1
    print('\n[A] All chapters')
    print('\n[Q] Quit')

    # Select chapters
    while True:
        # index = None
        try:
            choice = input('> ').upper().strip()
            if choice == 'A':
                subjects = []
                f = subjects_r.values
                for a in f:
                    for s in a:
                        if isinstance(s, str):
                            subjects.append(s)
                subjects = np.asarray(subjects)
                break
            elif choice == 'Q':
                quitAnim()
            else:
                try:
                    if int(choice) <= i:
                        index = summary[int(choice)]
                        subjects = subjects_r[index].dropna()
                        break
                    else:
                        print('Wrong value. Please try again')
                except ValueError:
                    print(
                        "Wrong value. Please try again with a value between 1 and", i - 1)
        except KeyError:
            print('Wrong value. Please try again with a value between 1 and', i - 1)
        except KeyboardInterrupt or EOFError:
            print("Keyboard interruption")
            print("Quitting...")
            time.sleep(2)
            quit()

    if random:
        np.random.shuffle(subjects)

    os.system(clear_command)

    total = subjects.size
    count = 1

    print("Press [ENTER] to pass to next subject\n")
    for sub in subjects:
        s = '[%d/%d]' % (count, total)
        count_str = s.rjust(100 - len(sub))
        count += 1
        i = sub + count_str
        a = getpass.getpass(i)

    while True:
        a = input('\n *********** Done! Almost ready! ***********')
        if a == "":
            break
