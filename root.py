import shutil


def main():

    from reports import conversions
    from reports import acquisition

    from reports import concatenate
    concatenate.concatenate()

    shutil.rmtree(
        path=r"C:\Users\onder.tanrikulu\OneDrive - NMQ Digital\Automated Exports\zoetis\Datasets\py-ga-zoetisus-dataset-for-shop-hybris\_exports")
    shutil.copytree(src=r"C:\Users\melik.masarifoglu\PycharmProjects\py-ga-zoetisus-dataset-for-shop-hybris\_exports",
                    dst=r"C:\Users\onder.tanrikulu\OneDrive - NMQ Digital\Automated Exports\zoetis\Datasets\py-ga-zoetisus-dataset-for-shop-hybris\_exports",
                    dirs_exist_ok=True)

    return


# Moving old transaction files. Adapt and use when necessary
# For 2020 transaction data. No longer used or called. Change Shutil before using.
def move_transactions():
    import datetime
    import os
    from config import Options
    from logger import Logger

    logger = Logger

    options = Options()

    def get_weekly_calendar(year, calendar_week):
        monday = datetime.datetime.strptime(f'{year}-{calendar_week}-1', "%Y-%W-%w").date()
        return [{"startDate": (monday - datetime.timedelta(days=1)).strftime("%Y-%m-%d"),
                 "endDate": (monday + datetime.timedelta(days=5.9)).strftime("%Y-%m-%d")}]

    start_date = datetime.date(2020, 1, 1)
    end_date = datetime.date.today()

    date_list = []

    for y in range(start_date.year, end_date.year + 1):
        for w in range(0, abs(datetime.date(y, 1, 1) - datetime.date(y + 1, 1, 1)).days // 7):
            if y < end_date.year:
                date_list.append([str(y) + "-" + str((w % 52) + 1).zfill(2), get_weekly_calendar(y, w % 52)])
            elif y == end_date.year:
                if w < int(datetime.datetime.today().strftime("%U")):
                    date_list.append([str(y) + "-" + str((w % 52) + 1).zfill(2), get_weekly_calendar(y, w % 52)])

    for date_item in date_list:
        source = os.path.join(options.dir_response, date_item[
            0] + "__183945438__ConversionsEcommerceTransactions" + "__" + "0.csv")

        if os.path.exists(source):
            shutil.move(source,
                        r"C:\Users\bilge.dogan\PycharmProjects\py-ga-zoetisus-dataset-for-shop-hybris\_ConversionsEcommerceTransactions_backup")
            logger.info(date_item[0] + "_ConversionsEcommerceTransactions is moved to backup")
        else:
            logger.info("no file as  " + source)


if __name__ == '__main__':
    main()
# else:
#    raise RuntimeError("{name} can't be imported!".format(name=__file__))
