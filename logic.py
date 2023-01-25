import random
from threading import Lock

from tools import get_direction, plural_days


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances or args or kwargs:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Adventure(metaclass=SingletonMeta):
    def __init__(self, width=4, height=4):
        self.world = None
        self.final_position = None
        self.current_position = None
        self.width = width
        self.height = height
        self.generate_game()
        self.is_finished = False

    # Генерация мира, финальной и стартовой комнат
    def generate_game(self):
        current_position = [random.randint(1, self.height), random.randint(1, self.width)]
        finish_position = [random.randint(1, self.height), random.randint(1, self.width)]
        while current_position == finish_position:
            finish_position = [random.randint(1, self.height), random.randint(1, self.width)]

        total = []
        for x in range(1, self.height + 1):
            line = []
            for y in range(1, self.width + 1):
                di = {f"Комната {x}-{y}": [x, y]}
                line.append(di)
            total.append(line)

        self.current_position = current_position
        self.final_position = finish_position
        self.world = total

    # Совершение "шага": проверка его возможности, определение завершения игры и вывода соответствующих сообщений
    def make_step(self, steps, way):
        is_success = False
        alert_type = "warning"

        if way == 1:
            if self.current_position[0] - steps >= 1:
                self.current_position[0] -= steps
                is_success = True
        elif way == 2:
            if self.current_position[1] + steps <= self.width:
                self.current_position[1] += steps
                is_success = True
        elif way == 3:
            if self.current_position[0] + steps <= self.height:
                self.current_position[0] += steps
                is_success = True
        elif way == 4:
            if self.current_position[1] - steps >= 1:
                self.current_position[1] -= steps
                is_success = True

        if is_success:
            if self.check_win():
                alert_type = "success"
                return "Вы успешно добрались до цели, поздравляю!\nИгра окончена: можете переиграть её заново, " \
                       "или создать мир другого размера, вернувшись на главную.", alert_type
            else:
                return f'Вы сделали {plural_days(steps, "steps", False)} на {get_direction(way)}. ' \
                       f'Сейчас вы в комнате {self.current_position[0]}-{self.current_position[1]}', alert_type
        else:
            alert_type = "danger"
            return "Вы не можете сделать этот шаг", alert_type

    # Проверка, завершилась ли игра или нет
    def check_win(self):
        if self.current_position == self.final_position:
            self.is_finished = True
        return self.is_finished
