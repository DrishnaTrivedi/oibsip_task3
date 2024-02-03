import argparse
import random
import string
import sys
parser = argparse.ArgumentParser()

parser.add_argument('--l', type=int)
parser.add_argument('--c', type=str)
args= parser.parse_args()

list1= "1234567890"
symbols = "!@#$%^&*()_+"
# lower= random.choice(string.ascii_lowercase)

def pswdGen(args):
    if(args.l > 0):
        pswd = ""
        dummy = ""

        if(args.c == "all"):
            for i in range(args.l):
                dummy = dummy + random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) +str(random.choice(list1)) + str(random.choice(symbols))
                pswd = pswd + random.choice(dummy)
            sys.stdout.write(f"your paswword is: {pswd}")

        elif (args.c == "letters+numbers" or args.c == "numbers+letters"):
            for i in range(args.l):
                dummy = dummy + random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) +str(random.choice(list1))
                pswd = pswd + random.choice(dummy)
            sys.stdout.write(f"your paswword is: {pswd}")

        elif (args.c == "symbols+numbers" or args.c == "numbers+symbols"):
            for i in range(args.l):
                dummy = dummy  +str(random.choice(list1)) + str(random.choice(symbols))
                pswd = pswd + random.choice(dummy)
            sys.stdout.write(f"your paswword is: {pswd}")

        elif(args.c == "symbols+letters" or args.c == "letters+symbols"):
            for i in range(args.l):
                dummy = dummy + random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase)  + str(random.choice(symbols))
                pswd = pswd + random.choice(dummy)
            sys.stdout.write(f"your paswword is: {pswd}")

        elif(args.c == "letters"):
            for i in range(args.l):
                dummy = dummy + random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase)
                pswd = pswd + random.choice(dummy)
            sys.stdout.write(f"your paswword is: {pswd}")

        elif(args.c == "numbers"):
            for i in range(args.l):

                pswd = pswd + random.choice(list1)
            sys.stdout.write(f"your paswword is: {pswd}")

        elif(args.c == "symbols"):
            for i in range(args.l):
                pswd = pswd + random.choice(symbols)
            sys.stdout.write(f"your paswword is: {pswd}")

        else:
            sys.stdout.write("ENTER VALID INPUT")

    else:
        sys.stdout.write("ENTER APPROPRIATE LENGTH")
pswdGen(args)