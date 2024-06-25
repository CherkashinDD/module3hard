data_structure = [
    [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(element_list):
    count = 0

    def checking_elements_and_calculate(element_list):
        nonlocal count

        if isinstance(element_list, int):
            count += element_list
        elif isinstance(element_list, str):
            count += len(element_list)
        elif isinstance(element_list, dict):
            for k, v in element_list.items():
                checking_elements_and_calculate(k)
                checking_elements_and_calculate(v)
        elif isinstance(element_list, (list, tuple, set)):
            for inner_element in element_list:
                checking_elements_and_calculate(inner_element)

    checking_elements_and_calculate(element_list)
    return count


print(calculate_structure_sum(data_structure))
