import settings


class AbstractFactory:
    computer_name = ""

    def create_cpu(self):
        pass

    def create_main_board(self):
        pass


class IntelFactory(AbstractFactory):
    computer_name = "Intel I7-series computer"

    def create_cpu(self):
        return IntelCpu("I7-6500")

    def create_main_board(self):
        return IntelMainBoard("Intel-6000")


class AmdFactory(AbstractFactory):
    computer_name = "Amd 4 computer"

    def create_cpu(self):
        return AmdCpu("amd444")

    def create_main_board(self):
        return AmdMainBoard("AMD-4000")


class AbstractCpu:
    series_name = ""
    instructions = ""
    arch = ""


class IntelCpu(AbstractCpu):
    def __init__(self, series):
        self.series_name = series


class AmdCpu(AbstractCpu):
    def __init__(self, series):
        self.series_name = series


class AbstractMainBoard:
    series_name = ""


class IntelMainBoard(AbstractMainBoard):
    def __init__(self, series):
        self.series_name = series


class AmdMainBoard(AbstractMainBoard):
    def __init__(self, series):
        self.series_name = series


class CompouterEngineer:
    def make_computer(self, factory_obj):
        self.prepare_hardwares(factory_obj)

    def prepare_hardwares(self, factory_obj):
        self.cpu = factory_obj.create_cpu()
        self.mainboard = factory_obj.create_main_board()
        print(
            f"computer [{factory_obj.computer_name}] info: cpu:{self.cpu.series_name} mainboard:{self.mainboard.series_name}")


if __name__ == '__main__':
    # 工人
    engineer = CompouterEngineer()
    # Intel工厂
    intel_factory = IntelFactory()
    engineer.make_computer(intel_factory)

    # amd工厂
    amd_factory = AmdFactory()
    engineer.make_computer(amd_factory)
