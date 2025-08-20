def relative_from_root(path: str):
    import test_reqres_microservice
    from pathlib import Path

    return Path(test_reqres_microservice.__file__).parent.parent.joinpath(path).absolute().__str__()