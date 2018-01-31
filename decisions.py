from random import shuffle
# [item] -> [item]

# type Tree a = (item, [Tree a])

# pure :: item -> Tree a
def pure(s):
    return (s, [])

# fst :: Tree a -> item
def fst(tree):
    return tree[0]

# snd :: Tree a -> [Tree a]
def snd(tree):
    return tree[1]

# add_children :: Tree a -> [Tree a] -> Tree a
def add_children(parent, children):
    return (fst(parent), snd(parent) + children)

# is_sington :: [Tree a] -> Bool
def is_sington(trees):
    assert type(trees) is list
    return len(trees) == 1

# is_empty :: [Tree a] -> Bool
def is_empty(trees):
    return trees == []

def take(n, xs):
    return xs[:n]

def drop(n, xs):
    return xs[n:]

def lmap(f, iterator):
    return list(map(f, iterator))

# choose :: Int -> [Tree a] -> Tree a
def choose(n, sample):
    parent = sample.pop(n)
    return add_children(parent, sample)

# step :: [Tree a] -> [Tree a]
def step(xs, show=lambda x: str(fst(x))):
    shuffle(xs)
    n = 3 # TODO: make this flexible
    choices = take(n, xs)
    remains = drop(n, xs)
    ns, ss, fs = make_options(choices, remains, show)
    selection_dictionary = {n: f for n,f in zip(ns, fs)}
    print("\nMake a choice")
    for i, x in zip(ns, ss):
        print(i, x, sep=": ")
    while True:
        op = input("> ")
        try:
            return selection_dictionary[op]()
        except KeyError:
            print("Invalid Response!")
    # create dictionary for input to function

# make_options :: [Tree a] -> ([Int], [Tree a], ?[Tree a])
def make_options(sample, remains, show=lambda x: str(fst(x))):
    ns = range(len(sample))
    ss = lmap(show, sample) + ["Pass", "Quit"]
    fs = [(lambda: [choose(n, sample)] + remains) for n in ns] + [
        lambda: sample + remains,
        lambda: []
    ]
    ns = lmap(str, ns) + ["p", "q"]
    return ns, ss, fs



# # make_choice :: [Tree a] -> Tree a
# def make_choice(choices):
#     for (i, x) in enumerate(choices)
#         print(i, x)
#     print("p: Pass")
#     print("q: Quit")



if __name__ == '__main__':
    selectables = [
        "asdf1",
        "asdf2",
        "asdf3",
        "asdf4",
        "asdf5",
        "asdf6",
        "asdf7",
        "asdf8",
        "asdf9",
        "asdf10",
        "asdf11",
        "asdf12",
    ]
