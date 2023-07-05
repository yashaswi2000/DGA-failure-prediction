import pandas as pd
data = pd.read_excel('./data/mainData.xlsx')
print(data.head)
feature_cols = ['n2', 'o2', 'h2', 'ch4']
thresh_dict = {'n2': 5, 'o2': 0.5, 'h2': 50, 'ch4': 500}


def fitness_function(col_name, data, thresh_dict, scale_factor):
    theta = thresh_dict[col_name]
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    for row in data.index:
        if data[col_name][row] >= theta:
            if data['Status'][row] == 'Faulty':
                tp += 1
            else:
                fp += 1
        else:
            if data['Status'][row] == 'Healthy':
                tn += 1
            else:
                fn += 1

    return scale_factor*(tp/(tp+fn))*(tn/(tn+fp))


def genetic_programming(feature_cols, thresh_dict, data):

    return 0
