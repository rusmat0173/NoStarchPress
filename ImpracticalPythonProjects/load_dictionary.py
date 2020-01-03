""" Playing with palingrams in Cpt 2. of the book

"""
import sys  # <= used for error handling

def load(name):
    try:
        with open(name, "r") as f:
            loaded_txt = f.read().split()
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file),
                file=sys.stderr)
        sys.exit(1)