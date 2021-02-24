class Iclothes_same:
    def __init__(self, material, size, color, brand):
        self.material = material
        self.size = size
        self.color = color
        self.brand = brand

class Igloves(Iclothes_same):
    def __init__(self, fingers, season):
        self.fingers = fingers
        self.season = season

class Ihat(Iclothes_same):
    def __init__(self, season, feshon):
        self.season = season
        self.feshon = feshon

class Iboots(Iclothes_same):
    def __init__(self, season, type_of_boots):
        self.season = season
        self.type_of_boots = type_of_boots

class Ibody_wear(Iclothes_same):
    def __init__(self, type_of_wear):
        self.type_of_wear = type_of_wear

class Ileg(Iclothes_same):
    def __init__(self, type_of_wear, season, ):
        self.type_of_wear = type_of_wear
        self.season = season
