
import re
import json
import secrets
from urllib.parse import urlsplit

import requests


class QuotesApiException(Exception):
    pass


class QuotesApi:
    url = None

    def _get_host(self):
        split_res = urlsplit(self.url)

        return "{0.scheme}//{0.netloc}".format(split_res)

    def _fetch_data(self):
        assert self.url is not None

        response = requests.get(self.url)

        if response.status_code in [400, 404]:
            raise Exception(response.reason)

        return response.text

    def _parse(self, data):
        raise NotImplementedError

    def get_random_quote(self):
        try:
            data = self._fetch_data()
        except Exception as e:
            raise QuotesApiException(
                u"Failed to fetch quote from %s: %s",
                self._get_host(), e.message)

        try:
            parsed_data = self._parse(data)
        except json.JSONDecodeError as e:
            raise QuotesApiException(
                u"Failed to parse data from %s: %s",
                self._get_host(), e.message)

        return parsed_data


class QuotesOnDesignAPI(QuotesApi):
    url = "http://quotesondesign.com/wp-json/posts?filter%5Borderby%5D=rand&filter%5Bposts_per_page%5D=1"

    def _parse(self, data):
        data_dict = json.loads(data)[0]

        return {
            "quote": clean_content(data_dict["content"]),
            "author": clean_content(data_dict["title"])
        }


class ForismaticAPI(QuotesApi):
    url = "https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en"

    def _parse(self, data):
        data_dict = json.loads(data)

        return {
            "quote": clean_content(data_dict["quoteText"]),
            "author": clean_content(data_dict["quoteAuthor"])
        }

QUOTE_APIS = [
    QuotesOnDesignAPI(),
    ForismaticAPI()
]


def clean_content(content):
    # remove HTML
    p = re.compile('<.*?>')
    cleaned = re.sub(p, '', content)

    # clean spaces and new lines
    return cleaned.replace("\n", "").strip()


def get_random_quote():
    return secrets.choice(QUOTE_APIS).get_random_quote()
