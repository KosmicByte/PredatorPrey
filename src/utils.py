

def make_filename(
        params,
        initial_state,
        t_span,
        prefix="lv",
        ext="png") -> str:
    parts = [prefix]
    parts += [f"{k[0]}{v:g}" for k, v in params.items()]
    parts += [f"x{initial_state[0]:g}", f"y{initial_state[1]:g}", f"t{t_span[1]:g}"]
    return "_".join(parts) + f".{ext}"