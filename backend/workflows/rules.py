def evaluate_conditions(conditions, payload):
    for condition in conditions:
        field = condition["field"]
        operator = condition["operator"]
        value = condition["value"]

        if operator == "equals" and payload.get(field) != value:
            return False
        if operator == "gt" and payload.get(field, 0) <= value:
            return False
    return True
