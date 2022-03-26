#!/usr/bin/env python3
import argparse

try:
    from search_engines.engines import search_engines_dict
    from search_engines.multiple_search_engines import MultipleSearchEngines, AllSearchEngines
    from search_engines import config
except ImportError as err:
    MSG = '\nPlease install `search_engines` to resolve this error.'
    raise ImportError(f'{MSG}') from err


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-q',
                        help='query', required=True)
    parser.add_argument('-e',
                        help='search engine(s) - ' + ', '.join(search_engines_dict) + ', or "all"',
                        default='duckduckgo')
    parser.add_argument('-o',
                        help='output file [html, csv, json]',
                        default='print')
    parser.add_argument('-n',
                        help='filename for output file',
                        default=config.OUTPUT_DIR+'output')
    parser.add_argument('-p',
                        help='number of pages',
                        default=config.SEARCH_ENGINE_RESULTS_PAGES,
                        type=int)
    parser.add_argument('-f',
                        help='filter results [url, title, text, host]',
                        default=None)
    parser.add_argument('-i',
                        help='ignore duplicates, useful when multiple search engines are used',
                        action='store_true')
    parser.add_argument('-proxy',
                        help='use proxy (protocol://ip:port)',
                        default=config.PROXY)

    args = parser.parse_args()

    proxy = args.proxy
    timeout = config.TIMEOUT + (10 * bool(proxy))
    agent = config.FAKE_USER_AGENT
    engines = [
        e.strip() for e in args.e.lower().split(',')
        if e.strip() in search_engines_dict or e.strip() == 'all'
    ]

    if not engines:
        print('Please choose a search engine: ' + ', '.join(search_engines_dict))
    else:
        if 'all' in engines:
            engine = AllSearchEngines(agent, proxy, timeout)
        elif len(engines) > 1:
            engine = MultipleSearchEngines(engines, agent, proxy, timeout)
        else:
            engine = search_engines_dict[engines[0]](agent, proxy, timeout)

        engine.ignore_duplicate_urls = args.i
        if args.f:
            engine.set_search_operator(args.f)

        engine.search(args.q, args.p)
        engine.output(args.o, args.n)


if __name__ == '__main__':
    main()
