class SeedToPlant:
    def __init__(self, num:int):
        self.seeds = num
        self.seed_changed = False
        self.soil = num
        self.soil_changed = False
        self.fertilizer = num
        self.fertilizer_changed = False
        self.water = num
        self.water_changed = False
        self.light = num
        self.light_changed = False
        self.temperature = num
        self.temperature_changed = False
        self.humidity = num
        self.humidity_changed = False
        self.location = num
        self.location_changed = False

    def return_parameter(self, parameter):
        match parameter:
            case 'seeds':
                return self.seeds
            case 'soil':
                return self.soil
            case 'fertilizer':
                return self.fertilizer
            case 'water':
                return self.water
            case 'light':
                return self.light
            case 'temperature':
                return self.temperature
            case 'humidity':
                return self.humidity
            case 'location':
                return self.location
            case _:
                return self.seeds
    def change_parameter(self, parameter_main, new, should_change):
        match parameter_main:
            case 'seeds':
                if not self.seed_changed:
                    self.seeds = new
                    if should_change and not self.seed_changed:
                        self.seed_changed = True
                    self.change_parameter('soil', new, False)
            case 'soil':
                if not self.soil_changed:
                    self.soil = new
                    if should_change and not self.soil_changed:
                        self.soil_changed = True
                    self.change_parameter('fertilizer', new, False)
            case 'fertilizer':
                if not self.fertilizer_changed:
                    self.fertilizer = new
                    if should_change and not self.fertilizer_changed:
                        self.fertilizer_changed = True
                    self.change_parameter('water', new, False)
            case 'water':
                if not self.water_changed:
                    self.water = new
                    if should_change and not self.water_changed:
                        self.water_changed = True
                    self.change_parameter('light', new, False)
            case 'light':
                if not self.light_changed:
                    self.light = new
                    if should_change and not self.light_changed:
                        self.light_changed = True
                    self.change_parameter('temperature', new, False)
            case 'temperature':
                if not self.temperature_changed:
                    self.temperature = new
                    if should_change and not self.temperature_changed:
                        self.temperature_changed = True
                    self.change_parameter('humidity', new, False)
            case 'humidity':
                if not self.humidity_changed:
                    self.humidity = new
                    if should_change and not self.humidity_changed:
                        self.humidity_changed = True
                    self.change_parameter('location', new, False)
            case 'location':
                if not self.location_changed:
                    self.location = new
                    if should_change and not self.location_changed:
                        self.location_changed = True
            case _:
                return
    def __repr__(self):
        return (f'Seed:{self.seeds}, soil:{self.soil}, fertilizer:{self.fertilizer}, water:{self.water}, light:{self.light}'
                f', temperature: {self.temperature}, humidity:{self.humidity}, location:{self.location}')
