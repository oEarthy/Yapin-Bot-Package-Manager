"""
This project automatically runs the code at "https://www.yapin.gg/sdk/yapper.py"
This is just meant as a demonstration, and from a cybersecurity standpoint, this is horrible
Please make sure you use this project with an understanding of the risks when running it!

Author: Earthy
"""
from urllib.request import Request, urlopen


def _load_sdk():
    url = "https://www.yapin.gg/sdk/yapper.py"
    request = Request(
        url,
        headers={
            "User-Agent": "yapper-sdk-fetcher/1.0",
            "Accept": "text/plain,*/*",
        },
    )

    with urlopen(request, timeout=30) as response:
        source = response.read().decode("utf-8")

    exec(compile(source, url, "exec"), globals())


_load_sdk()