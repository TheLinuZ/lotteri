import random

class Lotteri:

    def __init__(self):
        self.list_vinster = ["Solstol", "iPhone",
        "Handduk",
        "Tandborste",
        "Ockelbo 500",
        "Polaris RMK",
        "BMX",
        "Lyx yacht",
        "El sparkcykel",
        "Skateboard",
        "Resa till Hawaii",
        "Kaffe och Bulle",
        "JBL Hörlurar",
        "Konsert med Queen",
        "ICA Matkasse",
        "Surfbräda",
        "Ficklampa",
        "Bregott",
        "Ny dator",
        "Tuggummi",
        "2L Tvål",
        "Supra MK4"
        ]

    def get_vinst(self):
        slumptal=random.randint(0,19)
        return self.list_vinster[slumptal]
    
