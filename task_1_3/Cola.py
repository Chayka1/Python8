from task_1_3.Beverage import Beverage


class Cola(Beverage):
    def __init__(self, bev_name):
        Beverage.__init__(self, bev_name)

    def __str__(self):
        return self.get_bev_name()

