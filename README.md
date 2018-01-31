# honours-project-decider

This project aims to assist with the process of ordering preferences for Computer Science Honours Projects at Monash, but the underlying algorithm can be used for ordering any list with human intervention.

## Main Idea
Let each item in the list be a node that you would normally find in a tree. These nodes do not have any children or parents as of yet.

``` python
options = [
    ('Apples', []),
    ('Oranges', []),
    ('Pears', []),
    ...
]
```

You take a sample from the list, and select one of the items in the sample that you like the most.
```
Make a choice
1: Apples
2: Pears
```
The remaining items in the sample get added to the children of the selected item.
```
> 2
('Pears', [
   ('Apples', [])
])
```
Then, the result gets put back in the list and repeat until one node remains in the list. From there, repeat The process on the children of that node until we end up with a linked list and there is the ordering.
