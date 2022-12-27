import requests


def quote_url(url):
    """encodes URLs."""
    return requests.utils.quote(url, safe=';/?:@&=+$,#')


def unquote_url(url):
    """decodes URLs."""
    return decode_bytes(requests.utils.unquote(url))


def is_url(link):
    """Checks if link is URL"""
    parts = requests.utils.urlparse(link)
    return bool(parts.scheme and parts.netloc)


def domain(url):
    """Returns domain form URL"""
    host = requests.utils.urlparse(url).netloc
    return host.lower().split(':')[0].replace('www.', '')


def decode_bytes(s, encoding='utf-8', errors='replace'):
    """Decodes bytes to str, str to unicode."""
    return s.decode(encoding, errors=errors) if isinstance(s, bytes) else s

