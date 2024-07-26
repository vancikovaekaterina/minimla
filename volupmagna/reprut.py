# Sample dataset
dataset = [
    {'pivot_field': 'value1', 'other_field': 'data1'},
    {'pivot_field': 'value2', 'other_field': 'data2'},
    {'pivot_field': 'value1', 'other_field': 'data3'},
    {'pivot_field': 'value3', 'other_field': 'data4'}
]

# Collect unique pivot field values
unique_pivot_values = {record['pivot_field'] for record in dataset}

print(unique_pivot_values)
