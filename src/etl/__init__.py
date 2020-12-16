"""This script contains the ETL dag definition
"""
from prefect import Flow
from prefect.engine.executors import LocalDaskExecutor
from prefect.engine.state import State
from . import tasks


def create_flow() -> Flow:
    """Function to create prefect flow dag

    Returns:
        Flow: Prefect Flow Instance represening the workflow DAG
    """
    with Flow(
        "FLOW: insurance-marketplace-realities-20xx-fall-update-executive-summary",
        executor=LocalDaskExecutor(),
    ) as flow:
        tasks.download_document()
    return flow


def run_flow(**flow_kwargs) -> State:
    """Function to run the workflow given flow arguments

    Returns:
        State: State represening the state of the workflow after completion
    """
    flow = create_flow()
    return flow.run(flow_kwargs)
