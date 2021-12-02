import pandas as pd


def get_df_from_file(file_name, header, column_names):
    return pd.read_csv(file_name, header = header, names = column_names)
    
def generate_3_sliding_window_sums(df, field_name):
    prev_field = f"prev_{field_name}"
    prev_prev_field = f"prev_prev_{field_name}"

    df[prev_field] = df[field_name].shift(1)
    df[prev_prev_field] = df[prev_field].shift(1)
    df["sum"] = df[field_name] + df[prev_field] + df[prev_prev_field]

    return df

def generate_differences(df, field_name):
    prev_field_name = f"prev_{field_name}"
    df[prev_field_name] = df[field_name].shift(1)
    df["difference"] = df[field_name] - df[prev_field_name]

    return df
    
def calculate_increases(df, field_name):
    diffs = generate_differences(df, field_name)["difference"]
    
    return diffs[diffs > 0].count()

def calculate_sliding_window_sum_increases(df, field_name):
    return calculate_increases(df, "sum")
    

#TESTS
def given_day1_input_increases_should_be_1482(df):
    increases = calculate_increases(df, "depth")
    assert increases == 1482, f"Increases should be 1482, found {increases}" 

def given_day1_input_sliding_window_sum_increases_should_be_1(df):
    increases = calculate_sliding_window_sum_increases(df, "sum")
    assert increases == 1518, f"Increases should be 1518, found {increases}" 



def main():
    df_sample = get_df_from_file('Day1_sample.txt', None, ["depth"])
    df = get_df_from_file('Day1.txt', None, ["depth"])

    df_sliding = generate_3_sliding_window_sums(df, "depth")

    #------------------ TESTS -------------------
    given_day1_input_increases_should_be_1482(df)
    given_day1_input_sliding_window_sum_increases_should_be_1(df_sliding)




# ============================== RUN MAIN ========================
main()
