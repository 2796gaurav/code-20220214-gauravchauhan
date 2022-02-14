import pandas as pd

# preprocessing: reading standard bmi table
bt = pd.read_csv("bmi_table.csv")
bt["BMI max (kg/m2)"] = bt["BMI max (kg/m2)"].astype(float)


def calculate_bmi(weight, height):
    """
    Calculate BMI

    Parameters
    ----------
    weight : weight of user in KG
    height : weight of user in cm

    Returns
    -------
    BMI result in KG/m2
    """
    return (weight / height / height) * 10000


def calculate_bmi_category_risk(bmi):
    """
    Calculate bmi category and health risk

    Parameters
    ----------
    bmi : bmi of the user

    Returns
    -------
    list : bmi_category and health_risk
    """
    minv = 0
    for idx, rows in bt.iterrows():
        if minv < bmi <= rows["BMI max (kg/m2)"]:
            return list([rows["BMI Category"], rows["Health risk"]])
        minv = rows["BMI max (kg/m2)"]


def get_solution1(obj):
    """
    solution of problem 1

    Parameters
    ----------
    obj : input data of user in dict

    Returns
    -------
    count of how many users it has modified data into. It should always be 1
    """
    df = pd.DataFrame.from_dict(obj, orient="index").T
    df["bmi"] = [
        x
        for x in df[["WeightKg", "HeightCm"]].apply(lambda x: calculate_bmi(*x), axis=1)
    ]
    df["BMI Category"], df["Health risk"] = zip(
        *df["bmi"].apply(calculate_bmi_category_risk)
    )
    return df.values[0]


def res_to_csv(res, out_loc):
    """
    append the row to csv file

    Parameters
    ----------
    res : list of the row we want to append
    out_loc : output location of csv
    """
    output_df = pd.read_csv(out_loc)
    output_df.loc[len(output_df.index)] = res
    output_df.to_csv(out_loc, index=False)
