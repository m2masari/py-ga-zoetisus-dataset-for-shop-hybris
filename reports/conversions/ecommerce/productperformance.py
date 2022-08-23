from reports import Report
from logger import Logger

logger = Logger


def process():
    report = Report()
    report.category = "Conversions"
    report.name = "EcommerceProductPerformance"
    report.dimensions = ["ga:date", "ga:segment", "ga:productSku", "ga:productName", "ga:productBrand",
                         "ga:productCategoryLevel1", "ga:productCategoryLevel2", "ga:productCategoryLevel3"]
    report.segments = ["gaid::-1", "gaid::-2", "gaid::-3", "sessions::condition::ga:country==United States"]
    report.metrics = ["ga:itemRevenue", "ga:uniquePurchases", "ga:itemQuantity", "ga:productListViews",
                      "ga:productDetailViews", "ga:quantityAddedToCart", "ga:quantityRemovedFromCart", "ga:productCheckouts"]
    report.process()


if __name__ == '__main__':
    raise RuntimeError("{name} can't be run directly!".format(name=__file__))
    logger.critical("Runtime Error: File called directly!")
else:
    process()
