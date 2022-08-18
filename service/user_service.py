from model.user_dao import UserDao


class UserService:
    def __init__(self, user_dao, config):
        self.user_dao = user_dao
        self.config = config

    def retrieve_car_plate(self):
        car_plate = self.user_dao.get_CarPlate()
        return car_plate