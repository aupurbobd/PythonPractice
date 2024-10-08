import statistics

def mean_medain_mode(data1):
    return statistics.mean(data1), statistics.median(data1),statistics.mode(data1)


mean, median, mode = mean_medain_mode([2, 5, 3, 10, 155, 221, 255, 15])

print(f'Mean: {mean}\nMedian: {median}\nMode: {mode}')