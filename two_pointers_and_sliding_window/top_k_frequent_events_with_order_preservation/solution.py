def getTopKFrequentEvents(events, k):
    seen = {}
    for event in events:
        seen[event] = seen.get(event, 0) + 1

    bucket = [[] for _ in range(len(events) + 1)]
    for event in seen:
        bucket[seen[event]].append(event)
    
    result = []
    for f in range(len(events), 0, -1):
        result.extend(bucket[f])
        if len(result) >= k:
            return result[:k]
    return result
