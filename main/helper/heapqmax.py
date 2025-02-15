import heapq
"""
each node's children are both bigger than it (min heap) or smaller than (max heap) it.

Order properties
-----------------
leftChild = 2 * i
rightChiId = 2 * i + 1
parent = i / 2

heapify takes an array of numbers without the structure property and turns it into a heap


Max heap methods
-----------------
heapq._heappop_max
heapq._heapify_max
heappush_max - (defined below)
"""


def heappush_max(heap, item):
    """Push item onto heap, maintaining the heap invariant."""
    heap.append(item)
    heapq._siftdown_max(heap, 0, len(heap) - 1)


if __name__ == "__main__":
    heap = [1, 2, 3]
    heapq._heapify_max(heap)
    print(heapq._heappop_max(heap))
    print(heap)
