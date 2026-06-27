def countResponseTimeRegressions(responseTimes):
    result, running_sum = 0, 0
    for idx, val in enumerate(responseTimes):
        if idx > 0 and val > running_sum / idx:
            result += 1
        running_sum += val
    
    return result
