light_sources = {
    "external": {
        "position": [45, 33, 15],
        "color": [0.93, 0.92, 1.0],
        "rotation_data": {
            "center": [65, 33, 15],
            "radius": 22,
            "speed": 0.007,
            "angle": 0,
        },
    },
    "internal": {
        "position": [-28, 3.5, -19],
        "color": [1.0, 0.83, 0.42],
    },
}

models_repo = {
    "internal_light_model": {
        "obj_filename": "caixa/caixa.obj",
        "texture_filename": "caixa/white.jpg",
        "draw_type": "TRIANGLE",
        "translation": light_sources["internal"]["position"],
        "scale": [0.1, 0.1, 0.1],
        "angles": [0, 0, 0],
        "light_source": "internal",
        "light_coefs": [1.0, 1.0, 1.0, 1.0],
        "follow_light": True,
    },
    "external_light_model": {
        "obj_filename": "caixa/caixa.obj",
        "texture_filename": "caixa/white.jpg",
        "draw_type": "TRIANGLE",
        "translation": light_sources["external"]["position"],
        "scale": [0.1, 0.1, 0.1],
        "angles": [0, 0, 0],
        "light_source": "external",
        "light_coefs": [1.0, 1.0, 1.0, 1.0],
        "follow_light": True,
    },
    "box": {
        "obj_filename": "caixa/caixa.obj",
        "texture_filename": "caixa/caixa.jpg",
        "draw_type": "TRIANGLE",
        "translation": [-26, 0.8, -18],
        "scale": [0.6, 0.6, 0.6],
        "angles": [0, 0, 0],
        "light_source": "internal",
        "light_coefs": [0.3, 0.5, 1.0, 5.0],
    },
    "skybox": {
        "obj_filename": "sky/sky.obj",
        "texture_filename": "sky/sky.png",
        "draw_type": "TRIANGLE",
        "translation": [0, 0, 0],
        "scale": [3, 3, 3],
        "angles": [0, 0, 0],
        "light_source": None,
        "light_coefs": [1.0, 1.0, 1.0, 1.0],
    },
    "terrain_grass": {
        "obj_filename": "terrain/terrain_adjusted.obj",
        "texture_filename": "terrain/grass.jpg",
        "draw_type": "TRIANGLE",
        "translation": [0, 0, 0],
        "scale": [200, 1, 200],
        "angles": [0, 0, 0],
        "light_source": "external",
        "light_coefs": [1.0, 1.0, 0.7, 30.0],
    },
    "terrain_sand": {
        "obj_filename": "terrain/terrain_adjusted.obj",
        "texture_filename": "terrain/sand.jpeg",
        "draw_type": "TRIANGLE",
        "translation": [25, 0.1, 50],
        "scale": [50, 1, 50],
        "angles": [0, 0, 0],
        "light_source": "external",
        "light_coefs": [1.0, 1.0, 0.7, 30.0],
    },
    "small_skull": {
        "obj_filename": "skull/skull.obj",
        "texture_filename": "skull/skull.jpg",
        "draw_type": "QUADS",
        "translation": [-26, 2.8, -23],
        "scale": [0.055, 0.055, 0.055],
        "angles": [-90, 45, 0],
        "light_source": "internal",
        "light_coefs": [0.3, 0.5, 1.0, 5.0],
    },
    "big_skull": {
        "obj_filename": "skull/skull.obj",
        "texture_filename": "skull/skull.jpg",
        "draw_type": "QUADS",
        "translation": [65, 29, 15],
        "scale": [0.7, 0.7, 0.7],
        "angles": [-90, 0, 0],
        "light_source": "external",
        "light_coefs": [0.5, 0.7, 1.0, 5.0],
    },
    "pineapple": {
        "obj_filename": "pineapple/pineapple.obj",
        "texture_filename": "pineapple/pineapple.jpg",
        "draw_type": "QUADS",
        "translation": [-26, 1.4, -18],
        "scale": [0.06, 0.06, 0.06],
        "angles": [-90, 0, 0],
        "light_source": "internal",
        "light_coefs": [0.3, 0.5, 1.0, 5.0],
    },
    "cat": {
        "obj_filename": "cat/cat.obj",
        "texture_filename": "cat/cat.jpg",
        "draw_type": "QUADS",
        "translation": [-17, 0.66, -8],
        "scale": [0.042, 0.042, 0.042],
        "angles": [-90, 100, 0],
        "light_source": "external",
        "light_coefs": [0.9, 0.8, 0.3, 40.0],
    },
    "watchtower": {
        "obj_filename": "watchtower/watchtower.obj",
        "texture_filename": "watchtower/watchtower.jpg",
        "draw_type": "QUADS",
        "translation": [65, -3, 15],
        "scale": [2, 3.5, 2],
        "angles": [0, 0, 0],
        "light_source": "external",
        "light_coefs": [0.8, 0.8, 0.5, 25.0],
    },
    "farmhouse": {
        "obj_filename": "farmhouse/farmhouse_adjusted.obj",
        "texture_filename": "farmhouse/farmhouse.jpg",
        "draw_type": "TRIANGLE",
        "translation": [-20, 0, -15],
        "scale": [0.5, 0.5, 0.5],
        "angles": [0, -135, 0],
        "light_source": "internal",
        "light_coefs": [0.7, 0.7, 1.0, 15.0],
    },
}
