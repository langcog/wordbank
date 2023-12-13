import instruments.models


def get_instrument_model(language, form):
    return getattr(
        instruments.models,
        "_".join(language.replace("(", "").replace(")", "").split())
        + "_"
        + "_".join(form.split()),
    )
