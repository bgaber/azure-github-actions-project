import logging
import json

import azure.functions as func


def main(req: func.HttpRequest, myCosmosInputBinding: func.DocumentList, myCosmosOutputBinding: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request to get Cosmos DB data.')
    if not myCosmosInputBinding:
        logging.warning("Counter item not found")
    else:
        # Increment Counter
        counter = int(myCosmosInputBinding[0]['counter']) + 1
        logging.info("Found Counter item, Counter=%s",
                     counter)

        # Update Cosmos DB counter value with incremented value
        try:
            # Store output data using Cosmos DB output binding
            # use the value of the name parameter found in the output binding, in this case myCosmosOutputBinding
            db_dict = {"id": "1234567", "account_number": "resume", "counter": str(counter)}
            myCosmosOutputBinding.set(func.Document.from_dict(db_dict))
            db_string = json.dumps(db_dict)
            #myCosmosOutputBinding.set(func.Document.from_json(db_string))
        except Exception as e:
            logging.info(f"Error: {e}")
            print('Error:')
            print(e)

    #return 'I AM OKAY'
    return func.HttpResponse(
        db_string,
        status_code=200
    )
