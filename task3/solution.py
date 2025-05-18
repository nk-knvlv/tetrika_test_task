def strict(func):
    def wrapper(*args, **kwargs):
        arg_i = 0
        received_args = [*args, *kwargs]
        for arg_name, arg_type in list(func.__annotations__.items())[:-1]:  # пропускаем return аргумент
            if (received_arg_type := type(received_args[arg_i])) is not arg_type:
                raise ValueError(f'expected {arg_type} got {received_arg_type}')
            arg_i += 1
        return func(*args, **kwargs)

    return wrapper