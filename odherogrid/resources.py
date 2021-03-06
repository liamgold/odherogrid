from copy import deepcopy

from .settings import DEFAULT_GRID_NAME


CATEGORY_BASE = {
    "category_name": "name",
    "x_position": 0.000000,
    "y_position": 0.000000,
    "width": 1180.0,
    "height": 180.0,
    "hero_ids": [],
}


HERO_GRID_BASE = {
    "config_name": DEFAULT_GRID_NAME,
    "categories": [
        {
            "category_name": "Strength",
            "x_position": 0.000000,
            "y_position": 0.000000,
            "width": 1180.0,
            "height": 180.0,
            "hero_ids": [],
        },
        {
            "category_name": "Agility",
            "x_position": 0.000000,
            "y_position": 200.000000,
            "width": 1180.0,
            "height": 180.0,
            "hero_ids": [],
        },
        {
            "category_name": "Intelligence",
            "x_position": 0.000000,
            "y_position": 400.000000,
            "width": 1180.0,
            "height": 180.0,
            "hero_ids": [],
        }
    ]
}


# Represents default hero_grid_config.json
HERO_GRID_CONFIG_BASE = {
    "version": 3,
    "configs": [],
}

def _get_new_category(name: str, x_pos: float=0.0, y_pos: float=0.0, width: float=0.0, height: float=0.0) -> dict:
    # Copy category and give it a name
    category = deepcopy(CATEGORY_BASE)
    category["category_name"] = name

    params = {
        "x_position": x_pos,
        "y_position": y_pos,
        "width": width,
        "height": height
    }
    for param, value in params.items():
        value = float(abs(value)) # ensure value is a positive float
        if value:
            category[param] = value

    return category


def get_new_hero_grid_base() -> dict:
    return deepcopy(HERO_GRID_BASE)


def get_new_hero_grid_config() -> dict:
    """
    Returns a dict with contents equivalent to an empty
    hero_grid_config.json
    """
    return deepcopy(HERO_GRID_CONFIG_BASE)