from reports import Report
from logger import Logger

logger = Logger


def process():
    report = Report()
    report.category = "Acquisition"
    report.name = "CampaignsAllCampaigns"
    report.dimensions = ["ga:date", "ga:segment", "ga:source", "ga:medium", "ga:campaign", "ga:keyword"]
    report.segments = ["gaid::-1", "gaid::-2", "gaid::-3", "sessions::condition::ga:country==United States"]
    report.metrics = ["ga:users", "ga:newUsers", "ga:uniquePageViews", "ga:pageViews", "ga:bounceRate",
                      "ga:pageViewsPerSession", "ga:avgSessionDuration", "ga:transactions", "ga:transactionRevenue",
                      "ga:transactionsPerSession"]
    report.process()


if __name__ == '__main__':
    raise RuntimeError("{name} can't be run directly!".format(name=__file__))
    logger.critical("Runtime Error: File called directly!")
else:
    process()
