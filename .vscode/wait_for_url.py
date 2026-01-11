#!/usr/bin/env python3
"""
Simple helper to poll a URL until it returns a successful response.
Usage: python3 wait_for_url.py <url> [timeout_seconds]
"""
import sys
import time
from urllib.request import urlopen
from urllib.error import URLError, HTTPError


def wait_for_url(url, timeout=20, interval=0.2):
    end = time.time() + timeout
    while time.time() < end:
        try:
            with urlopen(url, timeout=5) as resp:
                code = resp.getcode()
                if 200 <= code < 400:
                    print(f"OK: {url} returned {code}")
                    return 0
        except (HTTPError, URLError, OSError) as e:
            # ignore and retry
            pass
        time.sleep(interval)
    print(f"ERROR: {url} did not respond with success within {timeout}s", file=sys.stderr)
    return 1


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: wait_for_url.py <url> [timeout_seconds]")
        sys.exit(2)
    url = sys.argv[1]
    timeout = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    sys.exit(wait_for_url(url, timeout))
