def oxford_comma(items):
    if len(items) > 2:
        items[len(items) - 1] = f"and {items[len(items) - 1]}"
        return ", ".join(items)
    elif len(items) == 2:
        return " and ".join(items)
    else:
        return items[0]
