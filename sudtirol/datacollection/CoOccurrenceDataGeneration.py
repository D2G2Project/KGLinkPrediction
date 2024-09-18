import pandas as pd
from itertools import combinations

data = pd.read_csv('tourismdata1.csv', header=0)

# Find co-occurrences by grouping by 'resource_id' and getting all pairs of osm_id
co_occurrence_dict = {}

for resource, group in data.groupby('resource_id')['osm_id']:
    osm_ids = group.unique()
    for osm1, osm2 in combinations(osm_ids, 2):
        co_occurrence_dict[(osm1, osm2)] = co_occurrence_dict.get((osm1, osm2), 0) + 1
        co_occurrence_dict[(osm2, osm1)] = co_occurrence_dict.get((osm2, osm1), 0) + 1

# Step 2: Calculate total occurrences for each osm_id
total_occurrences = data['osm_id'].value_counts()

# Step 3: Create the co-occurrence matrix and normalize the values
osm_ids = total_occurrences.index
co_occurrence_matrix = pd.DataFrame(index=osm_ids, columns=osm_ids, data=0.0)

for (osm1, osm2), count in co_occurrence_dict.items():
    co_occurrence_matrix.loc[osm1, osm2] = count / total_occurrences[osm1]


# Function to format each row as "osm_id,score" pairs, with space separation
def format_row(row):
    formatted_row = []
    for osm_id, value in row.items():
        formatted_row.append(f"{osm_id},{value}")
    return ' '.join(formatted_row)

# Create a new DataFrame where each row is formatted as desired
formatted_output = pd.DataFrame({
    'osm_id': co_occurrence_matrix.index,
    'co_occurrences': co_occurrence_matrix.apply(format_row, axis=1)
})

# Save the formatted DataFrame to a CSV file
output_file = 'formatted_co_occurrence_matrix.csv'
formatted_output.to_csv(output_file, index=False, header=False, sep=' ')

print(f"Formatted co-occurrence matrix saved to {output_file}")