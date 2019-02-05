#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    result = []

    i, j = 0, 0
    while i < len(items1) and j < len(items2):
        if items1[i] < items2[j]:
            result.append(items1[i])
            i += 1
        else:
            result.append(items2[j])
            j += 1

    while i < len(items1):
        result.append(items1[i])
        i += 1

    while j < len(items2):
        result.append(items2[j])
        j += 1

    return result
    

def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    center = len(items) // 2

    left = items[:center]
    right = items[center:]

    sorted(left)
    sorted(right)

    return merge(left, right)


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    center = len(items) // 2

    if len(items) == 1:
        return items

    left = items[:center]
    right = items[center:]

    l2, r2 = merge_sort(left), merge_sort(right)

    return merge(l2, r2)


def bucket_sort(items):
    buckets = {}
    maximum = 0
    
    for item in items:
        try:
            bucket = buckets[item // 10]
            if bucket > maximum:
                maximum = bucket

            bucket.append(item)
        except KeyError:
            buckets[item // 10] = [item]

    result = []
    for i in range(0, maximum + 1):
        bucket = buckets[i]
        sorted(bucket)

        result += bucket

    return result


def partition(items):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    pivot, items = items[0], items[1:]
    low = [item for item in items if item <= pivot]
    high = [item for item in items if item > pivot]
    return pivot, low, high


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    if len(items) <= 1:
        return items

    pivot, low, high = partition(items)
    return quick_sort(low) + [pivot] + quick_sort(high)

