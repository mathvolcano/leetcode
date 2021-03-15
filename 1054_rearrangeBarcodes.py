"""
1054. Distant Barcodes
https://leetcode.com/problems/distant-barcodes/
"""

def rearrangeBarcodes(barcodes):
    from collections import Counter
    from heapq import heapify, heappop, heappush
    counts = Counter(barcodes)
    heap = [(-counts[n], n) for n in counts]
    heapify(heap)  # Compares the first attribute of the tuple
    # print pq
    result = []
    while len(heap) >= 2:
        count1, barcode1 = heappop(heap)
        count2, barcode2 = heappop(heap)
        result.extend([barcode1, barcode2])
        
        if count1 + 1: 
            heappush(heap, (count1 + 1, barcode1))
        if count2 + 1: 
            heappush(heap, (count2 + 1, barcode2))

    if heap:
        result.append(heap[0][1])
    
    return result
