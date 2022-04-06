from binascii import hexlify
from collections import namedtuple
from secrets import token_bytes
from time import time

import requests

from search_engines import utils as utl
from search_engines.config import TIMEOUT, PROXY, USER_AGENT

# Generate X-Amzn-Trace-Id for header.
# https://docs.aws.amazon.com/xray/latest/devguide/xray-api-sendingdata.html#xray-api-traceids
#    TRACE_ID =  f"1-{HEX}-{binascii.hexlify(os.urandom(12)).decode('utf-8')}"
HEX_TIME = hex(int(time()))[2:]
TRACE_ID =  f"1-{HEX_TIME}-{hexlify(token_bytes(12)).decode('utf-8')}"


class HttpClient:
    """Performs HTTP requests. A `requests` wrapper, essentially."""
    def __init__(self, timeout=TIMEOUT, proxy=PROXY):
        self.session = requests.sessions.Session()

        self.session.proxies = self._set_proxy(proxy)
        self.session.headers['User-Agent'] = USER_AGENT
        self.session.headers['Accept-Language'] = 'en-GB,en;q=0.5'
        self.session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        self.session.headers['Accept-Encoding'] = "gzip, deflate"
        self.session.headers['Sec-Fetch-Dest'] = "document"
        self.session.headers['Sec-Fetch-Mode'] = "navigate"
        self.session.headers['Sec-Fetch-Site'] = "none"
        self.session.headers['Sec-Fetch-User'] = "?1"
        self.session.headers['Sec-Gpc'] = "1"
        self.session.headers['Upgrade-Insecure-Requests'] = "1"
        self.session.headers['X-Amzn-Trace-Id'] = TRACE_ID

        self.timeout = timeout
        self.response = namedtuple('response', ['http', 'html'])

    def get(self, page):
        """Submits a HTTP GET request."""
        page = self._quote(page)
        try:
            req = self.session.get(page, timeout=self.timeout)
            self.session.headers['Referer'] = page
        except requests.exceptions.RequestException as _e:
            return self.response(http=0, html=_e.__doc__)
        return self.response(http=req.status_code, html=req.text)

    def post(self, page, data):
        """Submits a HTTP POST request."""
        page = self._quote(page)
        try:
            req = self.session.post(page, data, timeout=self.timeout)
            self.session.headers['Referer'] = page
        except requests.exceptions.RequestException as _e:
            return self.response(http=0, html=_e.__doc__)
        return self.response(http=req.status_code, html=req.text)

    @staticmethod
    def _quote(url):
        """URL-encodes URLs."""
        if utl.decode_bytes(utl.unquote_url(url)) == utl.decode_bytes(url):
            url = utl.quote_url(url)
        return url

    @staticmethod
    def _set_proxy(proxy):
        """Returns HTTP or SOCKS proxies dictionary."""
        if proxy:
            if not utl.is_url(proxy):
                raise ValueError('Invalid proxy format!')
            proxy = {'http': proxy, 'https': proxy}
        return proxy
