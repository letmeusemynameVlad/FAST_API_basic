from api.product.schemas import UserOut


class Helper:
    def __init__(self):
        self.db: dict[int, UserOut] = {}
        self.current_id = 0

    @property
    def next_id(self) -> int:
        self.current_id += 1
        return self.current_id