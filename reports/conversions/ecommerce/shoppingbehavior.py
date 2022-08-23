from reports import Report
from logger import Logger

logger = Logger


def process():
    report = Report()
    report.category = "Conversions"
    report.name = "EcommerceShoppingBehavior"
    report.dimensions = ["ga:date", "ga:segment", "ga:browser", "ga:deviceCategory", "ga:sourceMedium",
                         "ga:region", "ga:country", "ga:city", "ga:shoppingStage"]
    report.segments = ["gaid::-1", "gaid::-2", "gaid::-3", "sessions::condition::ga:country==United States"]
    report.metrics = ["ga:sessions"]
    report.process()


if __name__ == '__main__':
    raise RuntimeError("{name} can't be run directly!".format(name=__file__))
    logger.critical("Runtime Error: File called directly!")
else:
    process()
