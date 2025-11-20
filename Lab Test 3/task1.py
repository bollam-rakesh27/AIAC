#!/usr/bin/env python3

import sys

def merge(left, right):
    i = j = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    if i < len(left):
        merged.extend(left[i:])
    if j < len(right):
        merged.extend(right[j:])
    return merged

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merged = merge(left, right)
    print(f"Merging {left} and {right} -> {merged}")
    return merged

def parse_input(s):
    s = s.strip()
    if not s:
        return []
    # accept spaces, commas, or mixed
    parts = []
    for token in s.replace(',', ' ').split():
        parts.append(int(token))
    return parts

if __name__ == "__main__":
    try:
        raw = input("Enter integers separated by spaces or commas: ")
    except EOFError:
        raw = ""
    arr = parse_input(raw)
    if not arr:
        print("No integers provided.")
        sys.exit(0)
    sorted_arr = merge_sort(arr)
    print("Sorted list:", sorted_arr)

