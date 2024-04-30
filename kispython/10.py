def remove_empty_columns(table):
    return [[row[i] for i in range(len(row))
             if any(row[i] for row in table)] for row in table]


def remove_duplicates(table):
    seen = set()
    result = []
    for row in table:
        row_tuple = tuple(row)
        if row_tuple not in seen:
            seen.add(row_tuple)
            result.append(row)
    return result


def split_column(table, column_index, separator):
    for row in table:
        if row[column_index]:
            date, percentage = row[column_index].split(separator)
            row[column_index] = date
            row.append(percentage)
    return table


def convert_contents(table):
    for row in table:
        if row[0]:
            date = row[0]
            date_parts = date.split('/')
            row[0] = f"{date_parts[0][-2:]}.{date_parts[1]}.{date_parts[2]}"
        if row[-2]:
            phone = row[-2]
            row[-2] = f"{phone[-7:-4]}-{phone[-4:-2]}-{phone[-2:]}"
        if row[-1]:
            percentage = row[-1]
            row[-1] = f"{round(float(percentage) * 100)}%"
    return table


def transpose_table(table):
    return list(map(list, zip(*table)))


def main(input_table):
    table = remove_empty_columns(input_table)
    table = remove_duplicates(table)
    table = split_column(table, 0, '|')
    table = convert_contents(table)
    table = transpose_table(table)
    return table