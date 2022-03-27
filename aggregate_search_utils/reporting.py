from aggregate_search_utils.files import results2file


def report_results(searchterm: str, message: str) -> None:
    """
    Output results or messages to Terminal and file.

    :param searchterm: Current search term; is used for file naming.
    :param message: Message or result string to be printed and written.
    """
    print(message)
    results2file(searchterm, f'{message}\n')
