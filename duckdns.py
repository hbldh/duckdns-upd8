#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import datetime

import requests


__version__ = '0.1.0'


def get_external_ip():
    """Get your external IP address as string.

    Uses httpbin(1): HTTP Request & Response Service

    """
    return requests.get("http://httpbin.org/ip").json().get('origin')


def duckdns_update(domains, token, verbose=False):
    """Update duckdns.org Dynamic DNS record.

    Args:
        domains (str): The DuckDNS domains to update as comma separated list.
        token (str): An UUID4 provided by DuckDNS for your user.
        verbose (bool): Returns info about whether or not IP has been changed as
            well as if the request was accepted.

    Returns:
        "OK" or "KO" depending on success or failure. Verbose adds IP and change
        status as well.

    """
    params = {
        "domains": domains if domains else os.environ.get("DUCKDNS_DOMAINS"),
        "token": token if token else os.environ.get("DUCKDNS_TOKEN"),
        "ip": get_external_ip(),
        "verbose": verbose
    }
    r = requests.get("https://www.duckdns.org/update", params)
    return r.text.strip().replace('\n', ' ')


def main():
    import argparse
    parser = argparse.ArgumentParser(
        description='Update duckdns.org Dynamic DNS record')
    parser.add_argument(
        '--domains', type=str, default=None,
        help='The DuckDNS domains to update as comma separated list. '
             'Defaults to DUCKDNS_DOMAINS environment variable.')
    parser.add_argument(
        '--token', type=str, default=None,
        help='An UUID4 provided by DuckDNS for your user. '
             'Defaults to DUCKDNS_TOKEN environment variable.')
    parser.add_argument('--verbose', action='store_true', help='More output.')
    args = parser.parse_args()

    out = duckdns_update(
        domains=args.domains, token=args.token, verbose=args.verbose)
    print("{0}: {1}".format(datetime.datetime.now(), out))


if __name__ == "__main__":
    main()
