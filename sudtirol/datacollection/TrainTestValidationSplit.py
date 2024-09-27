import pandas as pd
from itertools import combinations
import numpy as np
from sklearn.model_selection import train_test_split

data = pd.read_csv('tourismdata1.csv', header=0)

# Step 1: Find co-occurrences by grouping by 'resource_id' and getting all pairs of osm_id
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

# Step 4: Flatten the co-occurrence matrix into a table
def flatten_co_occurrence_matrix(co_occurrence_matrix):
    flat_co_occurrence = []
    for osm_id_1 in co_occurrence_matrix.index:
        for osm_id_2 in co_occurrence_matrix.columns:
            if osm_id_1 != osm_id_2:  # Avoid diagonal pairs (self pairs)
                score = co_occurrence_matrix.loc[osm_id_1, osm_id_2]
                flat_co_occurrence.append([osm_id_1, osm_id_2, score])
    # Convert to DataFrame
    flat_df = pd.DataFrame(flat_co_occurrence, columns=['osm_id_1', 'osm_id_2', 'score'])

    # Convert `osm_id_1` and `osm_id_2` to strings without '.0'
    flat_df['osm_id_1'] = flat_df['osm_id_1'].astype(int).astype(str)
    flat_df['osm_id_2'] = flat_df['osm_id_2'].astype(int).astype(str)
    return flat_df

# Step 5: Stratified split function for train/validation/test split
def stratified_split(df, train_ratio=0.7, val_ratio=0.1, test_ratio=0.2):
    df = df.sample(frac=1).reset_index(drop=True)  # Shuffle the data

    # Initialize empty DataFrames for train, validation, and test sets
    train_set = pd.DataFrame(columns=df.columns)
    val_set = pd.DataFrame(columns=df.columns)
    test_set = pd.DataFrame(columns=df.columns)

    # Get the counts of each osm_id in the dataset
    osm_counts = df[['osm_id_1', 'osm_id_2']].stack().value_counts()

    # Initialize individual counts for train, validation, and test sets
    train_counts = pd.Series(0, index=osm_counts.index)
    val_counts = pd.Series(0, index=osm_counts.index)
    test_counts = pd.Series(0, index=osm_counts.index)

    def assign_row(row, target_set, target_counts):
        target_set.loc[len(target_set)] = row
        target_counts[row['osm_id_1']] += 1
        target_counts[row['osm_id_2']] += 1
        return target_set, target_counts

    # Iterate over rows and assign them to train/validation/test sets
    for _, row in df.iterrows():
        osm_id_1, osm_id_2 = row['osm_id_1'], row['osm_id_2']
        total_count = osm_counts[osm_id_1] + osm_counts[osm_id_2]

        # Calculate the current ratios for train, val, and test sets
        train_ratio_current = (train_counts[osm_id_1] + train_counts[osm_id_2]) / total_count
        val_ratio_current = (val_counts[osm_id_1] + val_counts[osm_id_2]) / total_count
        test_ratio_current = (test_counts[osm_id_1] + test_counts[osm_id_2]) / total_count

        # Assign the row based on the current ratios
        if train_ratio_current < train_ratio:
            train_set, train_counts = assign_row(row, train_set, train_counts)
        elif val_ratio_current < val_ratio:
            val_set, val_counts = assign_row(row, val_set, val_counts)
        else:
            test_set, test_counts = assign_row(row, test_set, test_counts)

    return train_set, val_set, test_set

# Step 6: Format each of the sets into the required CSV format
def format_and_save_csv(df, output_file):
    osm_ids = sorted(set(df['osm_id_1']).union(set(df['osm_id_2'])))
    formatted_rows = []

    for osm_id in osm_ids:
        row_scores = {osm: 0 for osm in osm_ids}  # Initialize all scores to 0
        for _, row in df[(df['osm_id_1'] == osm_id) | (df['osm_id_2'] == osm_id)].iterrows():
            if row['osm_id_1'] == osm_id:
                row_scores[row['osm_id_2']] = row['score']
            else:
                row_scores[row['osm_id_1']] = row['score']

        # Format the row as "osm_id,score"
        formatted_row = f"{osm_id}, " + ' '.join([f"{osm},{row_scores[osm]}" for osm in osm_ids])
        formatted_rows.append(formatted_row)

    # Write the formatted rows to a CSV file
    with open(output_file, 'w') as f:
        for row in formatted_rows:
            f.write(row + '\n')

# Step 7: Save both flattened and formatted versions
def save_split_sets(train_df, val_df, test_df):
    # Save the flattened versions
    train_df.to_csv('train_flattened.csv', index=False)
    val_df.to_csv('validation_flattened.csv', index=False)
    test_df.to_csv('test_flattened.csv', index=False)

    # Save the formatted versions
    format_and_save_csv(train_df, 'train_formatted.csv')
    format_and_save_csv(val_df, 'validation_formatted.csv')
    format_and_save_csv(test_df, 'test_formatted.csv')

    print("Both flattened and formatted train, validation, and test files saved as CSV.")

# Step 8: Main function to combine all tasks and save the outputs
def process_and_save_co_occurrence_matrix(co_occurrence_matrix):
    # Flatten the co-occurrence matrix into a table
    flat_df = flatten_co_occurrence_matrix(co_occurrence_matrix)

    # Save the flattened table as CSV (optional, depending on whether you want this)
    flat_df.to_csv('flattened_co_occurrence.csv', index=False)
    print("Flattened co-occurrence matrix saved as 'flattened_co_occurrence.csv'.")

    # Perform the stratified split (70/20/10)
    train_df, val_df, test_df = stratified_split(flat_df, train_ratio=0.7, val_ratio=0.1, test_ratio=0.2)

    # Save both flattened and formatted versions of the train/validation/test sets
    save_split_sets(train_df, val_df, test_df)

# Return results
process_and_save_co_occurrence_matrix(co_occurrence_matrix)