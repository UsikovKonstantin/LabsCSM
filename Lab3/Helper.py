def get_int_from_input_min_max(min_val: int, max_val: int):
    while True:
        try:
            str_val = input()
            int_val = int(str_val)
            if min_val <= int_val <= max_val:
                break
            print(f"Число должно быть от {min_val} до {max_val}. Попробуйте снова.")
        except ValueError:
            print("Не удалось привести строку к целому числу. Попробуйте снова.")
    return int_val


def get_int_from_input_min(min_val: int):
    while True:
        try:
            str_val = input()
            int_val = int(str_val)
            if min_val <= int_val:
                break
            print(f"Число должно быть больше или равно {min_val}. Попробуйте снова.")
        except ValueError:
            print("Не удалось привести строку к целому числу. Попробуйте снова.")
    return int_val


def get_float_from_input(min_val: float):
    while True:
        try:
            str_val = input()
            float_val = float(str_val)
            if min_val < float_val:
                break
            print(f"Число должно быть больше {min_val}. Попробуйте снова.")
        except ValueError:
            print("Не удалось привести строку к вещественному числу. Попробуйте снова.")
    return float_val


def parse_input_string(lines):
    smo_type = None
    m = None
    n = None
    lambda_ = None
    t_obsl = None

    for line in lines:
        line_without_comments = line.split("#")[0].strip()

        if line_without_comments.startswith('smo_type:'):
            lst = line_without_comments.split(':')
            if len(lst) != 2:
                raise ValueError(f"Unable to parse line \"{line_without_comments}\" (too many \":\").")
            s = lst[1].strip()
            try:
                x = int(s)
            except ValueError:
                raise ValueError(f"Couldn't convert smo_type \"{s}\" to int.")
            if x <= 0 or x >= 7:
                raise ValueError(f"smo_type ({x}) must be in [0, 6].")
            smo_type = x
        elif line_without_comments.startswith('m:'):
            lst = line_without_comments.split(':')
            if len(lst) != 2:
                raise ValueError(f"Unable to parse line \"{line_without_comments}\" (too many \":\").")
            s = lst[1].strip()
            try:
                x = int(s)
            except ValueError:
                raise ValueError(f"Couldn't convert m \"{s}\" to int.")
            if x <= 0:
                raise ValueError(f"m ({x}) must be more than 0.")
            m = x
        elif line_without_comments.startswith('n:'):
            lst = line_without_comments.split(':')
            if len(lst) != 2:
                raise ValueError(f"Unable to parse line \"{line_without_comments}\" (too many \":\").")
            s = lst[1].strip()
            try:
                x = int(s)
            except ValueError:
                raise ValueError(f"Couldn't convert n \"{s}\" to int.")
            if x <= 0:
                raise ValueError(f"n ({x}) must be more than 0.")
            n = x
        elif line_without_comments.startswith('lambda_:'):
            lst = line_without_comments.split(':')
            if len(lst) != 2:
                raise ValueError(f"Unable to parse line \"{line_without_comments}\" (too many \":\").")
            s = lst[1].strip()
            try:
                x = float(s)
            except ValueError:
                raise ValueError(f"Couldn't convert lambda_ \"{s}\" to float.")
            if x <= 0:
                raise ValueError(f"lambda_ ({x}) must be more than 0.")
            lambda_ = x
        elif line_without_comments.startswith('t_obsl:'):
            lst = line_without_comments.split(':')
            if len(lst) != 2:
                raise ValueError(f"Unable to parse line \"{line_without_comments}\" (too many \":\").")
            s = lst[1].strip()
            try:
                x = float(s)
            except ValueError:
                raise ValueError(f"Couldn't convert t_obsl \"{s}\" to float.")
            if x <= 0:
                raise ValueError(f"t_obsl ({x}) must be more than 0.")
            t_obsl = x

    if smo_type is None:
        raise ValueError("smo_type is not defined")
    if lambda_ is None:
        raise ValueError("lambda_ is not defined")
    if t_obsl is None:
        raise ValueError("t_obsl is not defined")
    if smo_type > 3:
        if n is None:
            raise ValueError("n is not defined")
    if smo_type == 2 or smo_type == 5:
        if m is None:
            raise ValueError("m is not defined")

    return smo_type, m, n, lambda_, t_obsl
