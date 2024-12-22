def grouptosingle(group_data):
    ''' [list of numeric string] -> list of mumber
    Return the grouped_data to new data.

    >>> grouptosingle(['10-20', '20-30', '30-40']
    [15.0, 25.0, 35.0]

    >>> grouptosingle(['10-15', '15-20', '20-25']
    [12.5, 17.5, 22.5]
    '''
    new_data = []
    for n in group_data:
        lower_bound, upper_bound = n.split('-')
        xi = (int(lower_bound) + int(upper_bound))/2 
        new_data.append(xi)
            
    return new_data

def mean(data, frequency=None):
    ''' ([(converted)list of number], [list of number]) -> number
    Return the mean value of the data.
    
    >>> mean([1, 2, 3, 4, 5])
    3.0
    >>> mean(['10-20', '20-30', '30-40'], [1, 1, 1])
    25.0
    '''
    # for grouped data
    if frequency is not None:
        data_set = grouptosingle(data)

        # make list of midpoint times frequency
        fixi_list = []
        for i in range(len(data_set)):
            fixi = dataset[i] * frequency[i]
            fixi_list.append(fixi)

        return sum(list_of_number)/sum(frequency)
    
    # for single data
    return sum(data)/len(data)

def median(data, frequency=None):
    ''' [list of number] -> number
    Return the median value of the data.

    >>> median([1, 2, 3, 4, 5])
    3.0
    >>> median(['10-20', '20-30', '30-40'], [1, 1, 1])
    24.5
    '''
    # for grouped data
    if frequency is not None:

        # determine the location of median class
        n_by_2 = sum(frequency)/2

        # determine the median class
        med_class = 0
        for i  in range(len(data)):
            if med_class >= n_by_2:
                med_class = i - 1
                break
            else:
                med_class = med_class + frequency[i]

        # turn data given to new data set
        data_set = []
        for value in data:
            lower_bound, upper_bound = value.split('-')
            lower_bound = int(lower_bound)
            upper_bound = int(upper_bound)
            data_set.append(lower_bound)
            data_set.append(upper_bound)

        # determine interval class
        intv_class = upper_bound - lower_bound + 1                                              
        # determine cumulative frequency before the median class
        F = sum( frequency[:med_class])

        # determine median class frequency
        fn =  frequency[med_class]

        # determine lower boundary of median class
        L = data_set[med_class * 2] - 0.5

        # count median value of the data
        result = L + intv_class * (n_by_2 - F)/fn

        return result

    # for single data

    # arranged the data from smallest to largest
    arranged = sorted(data)

    # for even number of data
    if len(data) % 2 == 0:
        return (arranged[len(data)//2-1] + arranged[len(data)//2-2])/2

    # for odd number of data
    else:
        return (arranged[len(list_of_number)//2])

def mode(data, frequency=None):
    ''' [list of number] -> number
    Return the mode value of the data.

    >>> mode([1, 3, 2, 6, 3])
    3
    >>> mode(['150-158', '159-167', '168-176', '177-185', '186-194', '195-203', '204-212'], [1, 1, 5, 5, 5
    [176.0, 181.0, 186.0]
    '''
    # for grouped data
    if frequency is not None:

        # determine the location of mode class
        mode_freq = max(frequency)

        # determine the mode class
        mode_class = []
        for i in range(len(frequency)):
            if frequency[i] == mode_freq:
                mode_class.append(i)

        # turn data given to new data set
        data_set = []
        for value in data:
            lower_bound, upper_bound = value.split('-')
            lower_bound = int(lower_bound)
            upper_bound = int(upper_bound)
            data_set.append(lower_bound)
            data_set.append(upper_bound)
        
        # determine the interval class
        intv_class = upper_bound - lower_bound

        # find mode for each class
        result = []
        for i in range(len(mode_class)):
            
            # when modus class is in first
            if mode_class[i] == 0:

                # frequency in each class
                f1 = frequency[mode_class[i]]
                f0 = 0
                f2 = frequency[mode_class[i] + 1]
                
                # determine the mode class
                L = data_set[mode_class[i] * 2]

                # count mode value of the data
                mode = L + intv_class * ((f1-f0)/(2*f1 - f0 - f2))

                result.append(mode)

            # when mode class is the last
            elif mode_class[i] == len(frequency) - 1:
                f1 = frequency[mode_class[i] * 2]
                f0 = frequency[mode_class[i] - 1]
                f2 = 0
                
                L = data_set[mode_class[i] * 2]
                mode = L + intv_class*(f1-f0/(2*f1 - f0 - f2))

                result.append(mode)

            # when mode class between other mode class
            elif frequency[mode_class[i]] == frequency[mode_class[i] - 1] andfrequency[mode_class[i]] == frequency[mode_class[i] + 1]:

                mode = (data_set[mode_class[i] * 2 + 1] + data_set[mode_class[i] * 2])/2
                
                result.append(mode)
        
            else:
                f1 = frequency[mode_class[i]]
                f0 = frequency[mode_class[i] - 1]
                f2 = frequency[mode_class[i] + 1]
                
                L = data_set[mode_class[i] * 2]

                mode = L + intv_class * ((f1-f0)/(2*f1 - f0 - f2))

                result.append(mode)

        if len(result) == len(frequency):
            return 'Your Data Has No Mode Value'

        return result

    # for single data

    # count how many data has appeared
    appeared = {}
    for n in data:
        if n in appeared:
            appeared[n] += 1
        else:
            appeared[n] = 1
    
    # make a list of frequency
    frequencies = []
    for freq in appeared:
        frequencies.append(appeared[freq])

    # determine the mode value
    mode = max(frequencies)

    # matching the mode value with number frequency
    output = []
    for n  in appeared:
        if appeared[n] == mode:
            output.append(n)

    if len(output) == len(appeared):
        return 'Your Data Has No Mode Value'

    return output
