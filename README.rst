===============
DuckDNS Updater
===============

Python package for updating the dynamic DNS
`DuckDNS <https://www.duckdns.org/>`_ via GET requests.


Installation
------------

.. code-block:: bash

    $ pip install git+https://github.com/hbldh/duckdns-upd8.git

Basic Usage
-----------

Set the domain(s) to update and the DuckDNS token as environment variables:

.. code-block:: bash

    DUCKDNS_DOMAINS = mydomainname
    DUCKDNS_TOKEN = cbb9abcf-5a3f-4b67-98f3-c1e878b05b56

Then call the scipt:

.. code-block:: bash

    $ duckdns-upd8 --verbose
    2017-11-03 22:41:41.778529: OK 81.224.155.58  UPDATED
    $ duckdns-upd8 --verbose
    2017-11-03 22:42:36.228766: OK 81.224.155.58  NOCHANGE

You can for instance add such a call to your `cron.daily`:

.. code-block:: bash

    /opt/venv/bin/duckdns-upd8 --verbose >> /var/log/duckdns-upd8.log

Command line interface
----------------------

.. code-block:: bash

    $ duckdns-upd8 --help
    usage: duckdns-upd8 [-h] [--domains DOMAINS] [--token TOKEN] [--verbose]

    Update duckdns.org Dynamic DNS record

    optional arguments:
      -h, --help         show this help message and exit
      --domains DOMAINS  The DuckDNS domains to update as comma separated
                         list. Defaults to DUCKDNS_DOMAINS environment variable.
      --token TOKEN      An UUID4 provided by DuckDNS for your user. Defaults to
                         DUCKDNS_TOKEN environment variable.
      --verbose          More output.

