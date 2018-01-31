
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
