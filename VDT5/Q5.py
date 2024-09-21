#QUESTION 5 
#----------------

from typing import List, Dict, Callable, Any

# Function as specified by question
def aggregate_data(data: List[Dict], key: str, aggregator: Callable[[List[Dict]], Any]) -> Dict:
    
    grouped_data = {}

    # Group values by the specified key
    for item in data:
        key_value = item[key]
        if key_value not in grouped_data:
            grouped_data[key_value] = []
        grouped_data[key_value].append(item)

    # Apply the aggregator to each group
    aggregated_result = {}
    for key_value, items in grouped_data.items():
        aggregated_result[key_value] = aggregator(items)

    return aggregated_result


# Function to sum fields based on key (assuming sum operation)
def sum_field(items: List[Dict], field: str) -> int: # items- list of dictionaries of data, field- the key on which data is aggregated
    return sum(item[field] for item in items)


# Test the solution
if __name__ == "__main__":
    data = [
        {'fruit': 'Apple', 'quantity': 10},
        {'fruit': 'Banana', 'quantity': 2},
        {'fruit': 'Apple', 'quantity': 30},
        {'fruit': 'Berry', 'quantity': 40},
        {'fruit': 'Apple', 'quantity': 40},
    ]

    # Aggregate by adding the 'quantity' field
    # lamda used to allow flexiblity in passing data
    result = aggregate_data(data, 'fruit', lambda items: sum_field(items, 'quantity'))
    print(result)

