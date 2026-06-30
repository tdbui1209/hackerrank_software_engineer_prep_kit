def findTaskPairForSlot(taskDurations, slotLength):
    seen = {}
    for idx, task in enumerate(taskDurations):
        complement = slotLength - task
        if complement in seen:
            return [seen[complement], idx]
        seen[task] = idx
    return [-1, -1]
