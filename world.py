from database_table import DatabaseTable


class World:
    def __init__(self, name):
        self.name = name

        self.cities = DatabaseTable()
        self.add_city("Waterdeep", 2500000, economy_type='Trade City', leader="Lady S")

        self.trade_routes = DatabaseTable()

    def generate_world(self, settings):
        pass

    def add_city(self, name, population, economy_type='Normal', leader=None, special_traits=None):
        """Add a city with demographic and economic details."""
        self.cities.insert_row(name=name, population=population,
                               economy_type=economy_type, leader=leader,
                               special_traits=special_traits)

    def remove_city(self, city_name):
        """Remove a city from the world."""
        pass

    def add_road(self, city1, city2, distance, danger_level):
        """Establish a trade route between two cities utilizing
            a graph network to allow chain routes."""
        if city1 not in self.trade_routes:
            self.trade_routes.insert_row(name=city1, roads=[[city2, distance, danger_level]])
        else:
            self.trade_routes[city1]["roads"].append([city2, distance, danger_level])
