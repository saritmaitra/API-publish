from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import hypercorn
import json
from typing import List
import requests

testdata = [
    {
        "date_of_news": "February 23, 2018",
        "title": "nGen_LUX is here",
        "hyperlink": "https://learn.colorfabb.com/ngen_lux-is-here/",
        "organizations_entity": [
            [2, "Kristaps Politis"],
        ],
        "person_entity": [[1, "David Payne"]],
    }
]

# Init
app = FastAPI(debug=True)

# # Data (access data)
# with open("testdata.json") as f:
#     data = json.load(f)


# Route
@app.get("/")
async def get_data():
    return {"data": testdata}


@app.put("/")
async def create_prediction():
    return {"data": testdata}


if __name__ == "__main__":
    hypercorn.run(app, host="127.0.0.1", port=8000, reload=True)
