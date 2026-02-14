def to_int(obj: str):
    try:
        new_obj = int(obj)
        return new_obj
    except ValueError:
        return obj