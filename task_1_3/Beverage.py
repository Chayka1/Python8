class Beverage:
    def __init__(self, bev_name):
        self.__bev_name = bev_name

    def set_bev_name(self, bev_name):
        self.__bev_name = bev_name

    def get_bev_name(self):
        return self.__bev_name

