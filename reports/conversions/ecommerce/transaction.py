from reports import Report
from logger import Logger

logger = Logger

# 24 May 2021: from 2020-01 responses, this report will contain ga:sourceMedium
def process():
    report = Report()
    report.category = "Conversions"
    report.name = "EcommerceTransactions"
    report.dimensions = ["ga:date", "ga:segment", "ga:transactionId", "ga:campaign", "ga:productName", "ga:productBrand",
                         "ga:productCategoryLevel1", "ga:productCategoryLevel2", "ga:sourceMedium"]
    report.segments = ["gaid::-1", "gaid::-2", "gaid::-3", "sessions::condition::ga:country==United States"]
    report.metrics = ["ga:itemRevenue", "ga:uniquePurchases", "ga:itemQuantity"]
    report.process()


if __name__ == '__main__':
    raise RuntimeError("{name} can't be run directly!".format(name=__file__))
    logger.critical("Runtime Error: File called directly!")
else:
    process()
