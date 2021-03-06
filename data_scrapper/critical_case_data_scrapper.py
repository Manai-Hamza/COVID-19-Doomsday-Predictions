from data_scrapper.data_scrapper import DataScrapper
from data_scrapper.graphs_data_scrapper import GraphsDataScrapper

class CriticalCasesDataScrapper(DataScrapper):
    PREFIX = "critical"

    def __init__(self):
        super()

    def scrap_data(self):
        graphs_scrapper = GraphsDataScrapper()

        data = graphs_scrapper.get_data("coronavirus-cases", case_type = 3)
        filename = self.get_dataset_file_name()

        self.save_data_to_file(filename, data)

    def get_dataset_file_name(self, dataset_date=""):
        return super().get_dataset_file_name(CriticalCasesDataScrapper.PREFIX, dataset_date=dataset_date)
