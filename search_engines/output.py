
import csv
import json
import re
from collections import namedtuple

try:
    from shutil import get_terminal_size
except ImportError:
    from .libs.get_terminal_size import get_terminal_size

from .utils import decode_bytes #, encode_str
from .libs import windows_cmd_encoding


def print_results(search_engines):
    """Prints the search results."""
    for engine in search_engines:
        console(engine.__class__.__name__ + ' results')

        for i, _v in enumerate(engine.results, 1):
            console(f'{i:<4}{_v["link"]}')
        console('')


def create_csv_data(search_engines):
    """CSV formats the search results."""
    encoder = decode_bytes
    data = [['query', 'engine', 'domain', 'URL', 'title', 'text']]

    for engine in search_engines:
        for i in engine.results:
            row = [
                engine.se_query, engine.__class__.__name__,
                # Note: 'host' key throws exception with duckduckgo.
                # i['host'], i['link'], i['title'], i['text']
                i['link'], i['title'], i['text']
            ]
            row = [encoder(i) for i in row]
            data.append(row)
    return data


def create_json_data(search_engines):
    """JSON formats the search results."""
    jobj = {
        'query': search_engines[0].se_query,
        'results': {
            se.__class__.__name__: list(se.results) #[i for i in se.results]
            for se in search_engines
        }
    }
    return json.dumps(jobj)


def create_html_data(search_engines):
    """HTML formats the search results."""
    query = decode_bytes(search_engines[0].se_query) if search_engines else ''
    tables = ''

    for engine in search_engines:
        rows = ''
        for i, _v in enumerate(engine.results, 1):
            data = ''
            if 'title' in engine.se_filters:
                data += HtmlTemplate.data.format(_replace_with_bold(query, _v['title']))
            if 'text' in engine.se_filters:
                data += HtmlTemplate.data.format(_replace_with_bold(query, _v['text']))
            link = _replace_with_bold(query, _v['link']) if 'url' in engine.se_filters else _v['link']
            rows += HtmlTemplate.row.format(number=i, href=_v['link'], link=link, data=data)

        engine_name = engine.__class__.__name__
        tables += HtmlTemplate.table.format(engine=engine_name, rows=rows)
    return HtmlTemplate.html.format(query=query, table=tables)


def _replace_with_bold(query, data):
    """Places the query in <b> tags."""
    for match in re.findall(query, data, re.I):
        data = data.replace(match, f'<b>{match}</b>')
    return data


def write_file(data, path, encoding='utf-8'):
    """Writes search results data to file."""
    try:
        with open(path, 'w', encoding=encoding, newline='') as _f:
            if isinstance(data, list):
                writer = csv.writer(_f)
                writer.writerows(data)
            else:
                _f.write(data)
            console('Output file: ' + path)
    except IOError as err:
        console(err, level=Level.error)


def console(msg, end='\n', level=None):
    """Prints data on the console."""
    console_len = get_terminal_size().columns
    clear_line = f'\r{" " * (console_len - 1)}\r'
    msg = clear_line + (level or '') + msg
    print(msg, end=end)


Level = namedtuple('Level', ['info', 'warning', 'error'])(
    info='INFO ',
    warning='WARNING ',
    error='ERROR '
)

PRINT = 'print'
HTML = 'html'
JSON = 'json'
CSV = 'csv'


class HtmlTemplate:
    """HTML template."""
    html = """<html>
    <head>
    <meta charset="UTF-8">
    <title>Search Results</title>
    <style>
    body {{ background-color:#f5f5f5; font-family:Italic, Charcoal, sans-serif; }} 
    a:link {{ color: #262626; }} 
    a:visited {{ color: #808080; }} 
    th {{ font-size:17px; text-align:left; padding:3px; font-style: italic; }} 
    td {{ font-size:14px; text-align:left; padding:1px; }} 
    </style>
    </head>
    <body>
    <table>
    <tr><th>Query: '{query}'</th></tr>
    <tr><td> </td></tr>
    </table>
    {table}
    </body>
    </html>
    """
    table = """<table>
    <tr><th>{engine} search results </th></tr>
    </table>
    <table>
    {rows}
    </table>
    <br>
    """
    row = """<tr>
    <td>{number})</td>
    <td><a href="{href}" target="_blank">{link}</a></td>
    {data}
    </tr>
    """
    data = """<tr><td></td><td>{}</td></tr>"""
