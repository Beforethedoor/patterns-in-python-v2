from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# Команда для включения света
class LightOnCommand(Command):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_on()

    def undo(self):
        self._light.turn_off()


# Команда для выключения света
class LightOffCommand(Command):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_off()

    def undo(self):
        self._light.turn_on()


# Получатель команды (управляемый объект)
class Light:
    def turn_on(self):
        print("Свет включён")

    def turn_off(self):
        print("Свет выключен")


class RemoteControl:
    def __init__(self):
        self._commands = {}
        self._history = []

    def set_command(self, button, command):
        self._commands[button] = command

    def press_button(self, button):
        if button in self._commands:
            command = self._commands[button]
            command.execute()
            self._history.append(command)
        else:
            print("Неизвестная команда")

    def undo_last(self):
        if self._history:
            last_command = self._history.pop()
            last_command.undo()


if __name__ == "__main__":
    # Создаём свет и команды
    light = Light()
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    # Настраиваем пульт
    remote = RemoteControl()
    remote.set_command("A", light_on)  # Кнопка A — включить свет
    remote.set_command("B", light_off) # Кнопка B — выключить свет

    # Тестируем
    remote.press_button("A")  # Свет включён
    remote.press_button("B")  # Свет выключен
    remote.undo_last()        # Отмена: Свет включён
