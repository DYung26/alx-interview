#!/usr/bin/python3
'''A module for solving the lockbox puzzle.
In this puzzle, each box contains a list of keys that correspond
to the indices of other boxes.
The goal is to determine if all boxes can be unlocked,
starting from box 0 (which is always unlocked).
'''

def canUnlockAll(boxes):
    '''Determines if all boxes can be unlocked.

    This function checks if it's possible to unlock all the boxes
    in the given list.
    Each box may contain keys, which are indices of other boxes.
    Initially, box 0 is unlocked, and the function attempts to
    unlock all other boxes by using the keys found in unlocked boxes.

    Args:
        boxes (list of list of int): A list where each element is a list
        of keys (integers). Each key represents the index of a box
        that can be unlocked.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.

    Variables:
        n (int): The total number of boxes.
        seen_boxes (set): A set that tracks the indices of boxes
        that have been unlocked.
        unseen_boxes (set): A set that tracks the indices of boxes
        that can potentially be unlocked, based on keys found in unlocked boxes.
    '''
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()

        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)
    return n == len(seen_boxes)
