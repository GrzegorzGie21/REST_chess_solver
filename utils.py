def create_response_context(**kwargs: any) -> dict:
    context = {}
    for key, value in kwargs.items():
        context[key] = value

    return context