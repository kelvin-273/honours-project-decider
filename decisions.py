from random import randint, shuffle
from math import exp
from pprint import pprint
# [item] -> [item]

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

# step :: [Tree item] -> [Tree item]
def step(xs, show=lambda x: str(fst(x)), get_n=lambda m: 2):
    shuffle(xs)
    n = randint(2, get_n(len(xs)) + 1)
    choices = take(n, xs)
    remains = drop(n, xs)
    ns, ss, fs = make_options(choices, remains, show)
    # create dictionary for input to function
    selection_dictionary = {str(n): f for n,f in zip(ns, fs)}
    print("\nMake a choice")
    for i, x in zip(ns, ss):
        print(i, x, sep=": ")
    while True:
        op = input("> ")
        try:
            return selection_dictionary[op]()
        except KeyError:
            print("Invalid Response!")

# make_options :: [Tree item] -> ([Int], [Tree item], ?[Tree item])
def make_options(sample, remains, show=lambda x: str(fst(x))):
    ns = range(len(sample))
    ss = lmap(show, sample) + ["Pass", "Quit", "Random"]
    fs = lmap(lambda n: (lambda: [choose(n, sample)] + remains), ns) + [
        lambda: sample + remains,
        lambda: [],
        lambda: [choose(randint(0, len(sample) - 1), sample)] + remains
    ]
    ns = lmap(str, ns) + ["p", "q", "r"]
    return ns, ss, fs

def list_to_link(xs, show=lambda x: str(fst(x)), get_n=lambda m: 2, depth=0):
    print("Current depth:", depth)
    while len(xs) > 1:
        # pprint(xs)
        xs = step(xs, show=show, get_n=get_n)
    if xs == []:
        return []
    else:
        return [fst(xs[0])] + list_to_link(snd(xs[0]), show=show, get_n=get_n,
                                           depth=depth + 1)


def decider(items, show=lambda x: str(fst(x)), get_n=lambda m: 2):
    return list_to_link(lmap(pure, items), show=show, get_n=get_n)

# adaptive sample size
# parameters estimated thorough trial and error
f = lambda m: int(10 - 8*exp(-(m-2)/20))

if __name__ == '__main__':
    from extract_table import extract_table
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
    # print(decider(selectables, get_n=f))
    print(decider(extract_table("table.html"), show=lambda x: (fst(x)["Project Title"])))
