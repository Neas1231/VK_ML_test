"""
python3 script.py <%Y-%m-%d date>
Ex.
python3 script.py 2024-09-10 
"""


import os
import sys
import datetime


ACTION_TYPES = [
    "CREATE",
    "READ",
    "UPDATE",
    "DELETE",
]


def load_csv(filepath):
    rows = []
    with open(filepath) as f:
        for row in f:
            # Strip whitespaces
            row = row.strip()
            # Separate the columns
            row = row.split(',')
            # Save row
            rows.append(row)
    return rows


def save_output(output):
    dirname = './output'
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    filepath = os.path.join(dirname, f"{dt.strftime('%Y-%m-%d')}.csv")
    # Dicts output to 2d array
    array_output = [[row[0],*row[1].values()] for row in output.items()]
    # Save to csv file
    with open(filepath, 'w') as out:
        for row in array_output:
            out.write(','.join([str(elem) for elem in row]) + '\n')
    return True



if __name__ == "__main__":

    output = {}
    dt = datetime.datetime.strptime(sys.argv[1], '%Y-%m-%d')
    for i in range(7,0,-1):
        curr_dt = dt - datetime.timedelta(days=i)
        filepath = './input/' + curr_dt.strftime('%Y-%m-%d') + '.csv'
        rows = load_csv(filepath)
        for row in rows:
            # Create row in output
            if row[0] not in output:
                output[row[0]] = {act: 0 for act in ACTION_TYPES}
            # Count actions
            output[row[0]][row[1]] += 1
    save_output(output)