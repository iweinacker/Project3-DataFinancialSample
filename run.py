import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('financials_sample')

financials = SHEET.worksheet('financials')


def get_financials_data():
    """
    Get sales figures input from the user
    """
    print("Please enter sales or expense data from the year that correspond.")
    print("Data should be positive or negative.")
    print("Please enter sales data from the actual year.\n")

    data_str = input("Enter your data here: ")
    financials_data = data_str.split(",")
    validate_data(financials_data)


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if string cannot converted into int.
    """
    try:
        if len(values) != 6:
            # ojo poner 12
            raise ValueError(
                f"Exactly 12 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")


get_financials_data()
