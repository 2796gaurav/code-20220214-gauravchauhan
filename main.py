from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette.requests import Request
import pandas as pd
import ijson
from modules.func import get_solution1, res_to_csv


app = FastAPI()


class Data(BaseModel):
    input_location: str
    output_location: str  # local file location


@app.post("/solution1/")
async def sol1(data: Data):
    """
    Solution to problem statement 1

    Parameters
    ----------
    data : POST input API json data body
        input_location : input location of json file
        output_location : output location of json file

    Returns
    -------
    response
        JSON response with providing no. of entries it has modified into.
    """
    inp_loc = data.input_location
    out_loc = data.output_location

    if (inp_loc[-4:] != "json") or (out_loc[-3:] != "csv"):
        raise HTTPException(status_code=400, detail="Invalid input/ output file type")

    output_df = pd.DataFrame(
        columns=["Gender", "HeightCm", "WeightKg", "bmi", "BMI Category", "Health risk"]
    )
    output_df.to_csv(out_loc, index=False)
    c = 0
    try:
        with open(inp_loc, "rb") as data:
            for obj in ijson.items(data, "item"):
                # get results
                res = get_solution1(obj)
                # to csv
                out = res_to_csv(res, out_loc)
                c += 1
    except:
        raise HTTPException(
            status_code=400, detail="Not found Json file or Json file format incorrect."
        )
    return {"status": "ok", "msg": "updated solution to output file", "records": c}


@app.get("/solution2/{input_location}")
async def sol2(input_location: str):
    """
    Solution to problem statement 2

    Parameters
    ----------
    input_location : GET input API data body
        input_location : input location of csv file (It is same as output of solution 1)

    Returns
    -------
    response
        JSON response with providing no. of entries it has encountered in BMI category as overweight.
    """

    if input_location[-3:] != "csv":
        raise HTTPException(status_code=400, detail="Invalid input file type")

    df = pd.read_csv(input_location)
    res = df[df["BMI Category"] == "Overweight"].shape[0]
    return {"count": res}
