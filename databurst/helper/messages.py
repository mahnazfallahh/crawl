from enum import StrEnum


class CsvMessage(StrEnum):
    """
    Enumeration class for CSV error messages.

    StrEnum Values:
        CSV_ERROR: Represents an error occurred while processing the CSV file.
    """
    CSV_ERROR = "error occurred while processing the CSV file."