import logging, json

import azure.functions as func
from services.todo_service import get_todo


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    data = get_todo()
    return func.HttpResponse(json.dumps(data), headers={"content-type": "application/json"})