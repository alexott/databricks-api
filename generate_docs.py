import inspect

from databricks_api import DatabricksAPI
import databricks_cli


db = DatabricksAPI(host="localhost", token="token")


intro = """databricks-api
==============

*[This documentation is auto-generated]*

This package provides a simplified interface for the Databricks REST API.
The interface is autogenerated on instantiation using the underlying client
library used in the official ``databricks-cli`` python package.

The docs here describe the interface for version **{version}** of
the ``databricks-cli`` package for API version **{api_version}**.
Assuming there are no major changes to the ``databricks-cli`` package
structure, this package should continue to work without a required update.

The ``databricks-api`` package contains a ``DatabricksAPI`` class which provides
instance attributes for the ``databricks-cli`` ``ApiClient``, as well as each of
the available service instances. The attributes of a ``DatabricksAPI`` instance are:

""".format(
    version=databricks_cli.version.version,
    api_version=databricks_cli.sdk.version.API_VERSION,
)

attrs = []

for k, v in db.__dict__.items():
    attrs.append("* DatabricksAPI." + k + " *<" + v.__class__.__module__ + "." + v.__class__.__name__ + ">*\n")

middle = """
To instantiate the client, provide the databricks host and either a token or
user and password. Also shown is the full signature of the
underlying ``ApiClient.__init__``

.. code-block:: python

    from databricks_api import DatabricksAPI

    # Provide a host and token
    db = DatabricksAPI(host="example.cloud.databricks.com", token="dpapi123...")

    # OR a host and user and password
    db = DatabricksAPI(host="example.cloud.databricks.com", user="me@example.com", password="password")

    # Full __init__ signature
    {instantiate}

Refer to the `official documentation <https://docs.databricks.com/api/index.html>`_
on the functionality and required arguments of each method below.

Each of the service instance attributes provides the following public methods:

""".format(instantiate="db = DatabricksAPI" + str(inspect.signature(databricks_cli.sdk.ApiClient)))

services = []
for k, v in db.__dict__.items():
    if k == "client":
        continue
    print(k, v)
    h = "DatabricksAPI." + k
    services.append(h + "\n")
    services.append("-" * len(h) + "\n\n")
    methods = inspect.getmembers(v, predicate=inspect.ismethod)
    print(methods)
    for method in methods:
        print(method)
        if not method[0].startswith("_"):
            services.append("* " + "``DatabricksAPI." + k + "." + method[0] + str(inspect.signature(method[1])) + "``\n")
    services.append("\n")


with open("README.rst", "w") as f:
    f.write(intro)
    for a in attrs:
        f.write(a)
    f.write(middle)
    for s in services:
        f.write(s)
