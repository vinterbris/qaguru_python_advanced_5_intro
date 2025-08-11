def relative_from_root(path: str):
    import reqres_microservice
    from pathlib import Path

    return Path(reqres_microservice.__file__).parent.parent.joinpath(path).absolute().__str__()


print('hello')