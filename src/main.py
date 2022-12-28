from src.di import injector
from src.usecase import UseCaseInterface

usecase = injector.get(UseCaseInterface)  # type: ignore


data_path = "src/data/origin.json"
save_path = "src/data/save.json"
usecase.execute(data_path, save_path)
