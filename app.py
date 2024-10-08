def switch_case_example(value):
    match value:
        case 1:
            return "Case 1"
        case 2:
            return "Case 2"
        case 3:
            return "Case 3"
        case _:
            return "Default case"

# Test
print(switch_case_example(1))  # Output: Case 2

