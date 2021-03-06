from random import randint, shuffle
from math import exp
from pprint import pprint
from extract_table import extract_table
import os
import re

# type Tree item = (item, [Tree item])

# pure :: item -> Tree item
def pure(s):
    return (s, [])

# fst :: Tree item -> item
def fst(tree):
    return tree[0]

# snd :: Tree item -> [Tree item]
def snd(tree):
    return tree[1]

# add_children :: Tree item -> [Tree item] -> Tree item
def add_children(parent, children):
    return (fst(parent), snd(parent) + children)

# is_sington :: [Tree item] -> Bool
def is_sington(trees):
    assert type(trees) is list
    return len(trees) == 1

# is_empty :: [Tree item] -> Bool
def is_empty(trees):
    return trees == []

def take(n, xs):
    return xs[:n]

def drop(n, xs):
    return xs[n:]

def lmap(f, iterator):
    return list(map(f, iterator))

# choose :: Int -> [Tree item] -> Tree item
def choose(n, sample):
    sample = sample.copy()
    parent = sample.pop(n)
    return add_children(parent, sample)

def _delete(n, sample):
    sample = sample.copy()
    sample.pop(n)
    return sample

# step :: [Tree item] -> [Tree item]
def step(xs, show=lambda x: str(fst(x))):
    shuffle(xs)
    # extract sample from xs
    n = randint(2, func(len(xs)))
    choices = take(n, xs)
    remains = drop(n, xs)
    # create dictionary for input to function
    ns, ss, fs = make_options(choices, remains, show)
    # selection_dictionary = {str(n): f for n,f in zip(ns, fs)}
    # display menu and as for input
    print("\nMake a choice")
    for i, x in zip(ns, ss):
        print(i, x, sep=": ")
    while True:
        op = input("> ")
        try:
            # return selection_dictionary[op]()
            return fs(op)
            # TODO: Change this lazy dictionary of functions to a closure result
        except KeyError:
            print("Invalid Response!")
        except KeyboardInterrupt:
            pass

# make_options :: [Tree item] -> ([Int], [Tree item], ?[Tree item])
# def make_options(sample, remains, show=lambda x: str(fst(x))):
#     ns = range(len(sample))
#     ss = lmap(show, sample) + ["Delete All", "Pass", "Quit", "Random", "Current State"]
#     fs = lmap(lambda n: (lambda: [choose(n, sample)] + remains), ns) + [
#         lambda: remains,
#         lambda: sample + remains,
#         lambda: [],
#         lambda: [choose(randint(0, len(sample) - 1), sample)] + remains,
#         lambda: [pure(sample + remains)]
#     ]
#     ns = lmap(str, ns) + ["dd", "p", "q", "r", "c"]
#     return ns, ss, fs

def make_options(sample, remains, show=lambda x: str(fst(x))):
    ns = range(len(sample))
    ss = lmap(show, sample) + ["Delete Item", "Delete All", "Pass", "Quit",
                               "Random", "Current State"]

    def in_to_uit(op):
        if re.fullmatch(r"^[0-" + str(len(sample) - 1) + r"]$", op):
            return [choose(int(op), sample)] + remains
        elif re.fullmatch(r"^d[0-" + str(len(sample) - 1) + r"]$", op):
            return _delete(int(op[1:]), sample) + remains
        elif re.fullmatch(r"^dd$", op):
            return remains
        elif re.fullmatch(r"^p$", op):
            return sample + remains
        elif re.fullmatch(r"^q$", op):
            return []
        elif re.fullmatch(r"^r$", op):
            return [choose(randint(0, len(sample) - 1), sample)] + remains
        elif re.fullmatch(r"^c$", op):
            return [pure(sample + remains)]
        else:
            raise KeyError

    ns = lmap(str, ns) + ["dN", "dd", "p", "q", "r", "c"]
    return ns, ss, in_to_uit

def list_to_link(xs, show=lambda x: str(fst(x)), depth=0):
    print("Current depth:", depth)
    while len(xs) > 1:
        print("Items at current depth:", len(xs))
        xs = step(xs, show=show)
    if xs == []:
        return []
    else:
        return [fst(xs[0])] + list_to_link(snd(xs[0]), show=show,
                                           depth=depth + 1)

def decider(items, show=lambda x: str(fst(x))):
    output = list_to_link(lmap(pure, items), show=show)
    if any(map(is_list_of_trees, output)):
        with open("save.txt", "w") as f:
            f.write(str(output))
    return output

def is_tree(obj):
    if not type(obj) is tuple: return False
    if not len(obj) == 2: return False
    if not type(snd(obj)) is list: return False
    return all(map(is_tree, snd(obj))) # True if snd(obj) == []

def is_list_of_trees(obj):
    if not type(obj) is list:
        return False
    else:
        return all(map(is_tree, obj))

def continue_from_file(filename, show=lambda x: str(fst(x))):
    with open(filename, "r") as f:
        xs = eval(f.read())
    confirmed = [i for i in xs if not is_list_of_trees(i)]
    unconfirmed = [i for i in xs if is_list_of_trees(i)]
    assert len(unconfirmed) < 2
    output = list_to_link(unconfirmed[0], show=show, depth=len(confirmed))
    if any(map(is_list_of_trees, output)):
        with open(filename, "w") as f:
            f.write(str(output))
    else:
        with open("output.txt", "w") as f:
            f.write(str(output))
        os.remove(filename)
    return output

# adaptive sample size
# parameters estimated thorough trial and error
func = lambda m: int(10 - 8*exp(-(m-2)/20))

def main():
    if os.path.exists("save.txt"):
        print("Continuing from save.txt\n")
        return continue_from_file("save.txt",
                                  show=lambda x: str(fst(x)["Project Title"]))
    else:
        print("Starting new save.txt\n")
        return decider(extract_table("table.html"),
                       show=lambda x: (fst(x)["Project Title"]))

if __name__ == '__main__':
    # selectables = [
    #     "asdf1",
    #     "asdf2",
    #     "asdf3",
    #     "asdf4",
    #     "asdf5",
    #     "asdf6",
    #     "asdf7",
    #     "asdf8",
    #     "asdf9",
    #     "asdf10",
    #     "asdf11",
    #     "asdf12",
    # ]
    # print(decider(selectables))
    print(main())
