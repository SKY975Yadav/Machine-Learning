# Required libraries for ID3
import numpy as np
import pandas as pd
import math

# Dataset
data = {
    'Whether': ['Sunny', 'Rain', 'Cloudy', 'Sunny', 'Sunny', 'Cloudy', 'Rain', 'Rain', 'Sunny', 'Cloudy', 'Rain', 'Sunny'],
    'Temperature': ['High', 'Normal', 'High', 'High', 'Low', 'Low', 'Normal', 'Low', 'Normal', 'Low', 'High', 'Normal'],
    'Wind': ['High', 'High', 'Normal', 'High', 'Normal', 'High', 'Normal', 'Normal', 'High', 'Normal', 'High', 'Normal'],
    'Play': ['No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No']
}

# Convert dataset into a DataFrame
df = pd.DataFrame(data)

# Function to calculate entropy
def entropy(target_col):
    elements, counts = np.unique(target_col, return_counts=True)
    entropy_val = 0
    for i in range(len(elements)):
        p_i = counts[i] / sum(counts)
        entropy_val += -p_i * math.log2(p_i)
    return entropy_val

# Function to calculate information gain
def information_gain(data, split_attribute, target_attribute='Play'):
    # Calculate the entropy of the whole dataset
    total_entropy = entropy(data[target_attribute])
    
    # Calculate the weighted entropy for the split attribute
    values, counts = np.unique(data[split_attribute], return_counts=True)
    weighted_entropy = 0
    for i in range(len(values)):
        subset = data[data[split_attribute] == values[i]]
        weighted_entropy += (counts[i] / np.sum(counts)) * entropy(subset[target_attribute])
    
    # Calculate the information gain
    info_gain = total_entropy - weighted_entropy
    return info_gain

# ID3 algorithm implementation
def id3(data, original_data, features, target_attribute='Play', parent_node_class=None):
    # If all target values are the same, return that class
    if len(np.unique(data[target_attribute])) == 1:
        return np.unique(data[target_attribute])[0]
    
    # If dataset is empty, return the majority class of the original dataset
    elif len(data) == 0:
        return np.unique(original_data[target_attribute])[np.argmax(np.unique(original_data[target_attribute], return_counts=True)[1])]
    
    # If no features are left, return the majority class of the current dataset
    elif len(features) == 0:
        return parent_node_class
    
    # Otherwise, proceed with ID3
    else:
        # Record the majority class at the parent node
        parent_node_class = np.unique(data[target_attribute])[np.argmax(np.unique(data[target_attribute], return_counts=True)[1])]
        
        # Calculate the information gain for each feature
        info_gains = [information_gain(data, feature) for feature in features]
        
        # Choose the feature with the highest information gain
        best_feature_index = np.argmax(info_gains)
        best_feature = features[best_feature_index]
        
        # Create the tree structure
        tree = {best_feature: {}}
        
        # Remove the feature with the highest information gain from the feature list
        features = [i for i in features if i != best_feature]
        
        # Grow the tree
        for value in np.unique(data[best_feature]):
            value_subset = data[data[best_feature] == value]
            subtree = id3(value_subset, original_data, features, target_attribute, parent_node_class)
            tree[best_feature][value] = subtree
        
        return tree

# Prepare the dataset and run ID3
features = list(df.columns[:-1])
decision_tree = id3(df, df, features)
print("Decision Tree using ID3:")
print(decision_tree)
