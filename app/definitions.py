"""The code location's Definitions: the assets, jobs and schedules Dagster loads.

Wodby's code server loads this module, app.definitions, unless the service's
"Python module" setting names another one.
"""

import dagster as dg


@dg.asset
def greeting() -> str:
    """An example asset. Replace it with your own."""
    return "Hello from Dagster on Wodby"


greeting_job = dg.define_asset_job("greeting_job", selection=[greeting])

defs = dg.Definitions(assets=[greeting], jobs=[greeting_job])
