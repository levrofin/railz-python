from typing import Literal, Set, cast

ProbabilityOfDefaultReportMetaDataServiceName = Literal[
    "dynamicsBusinessCentral",
    "freshbooks",
    "oracleNetsuite",
    "quickbooks",
    "quickbooksDesktop",
    "sageBusinessCloud",
    "sageIntacct",
    "wave",
    "xero",
    "zohoBooks",
]

PROBABILITY_OF_DEFAULT_REPORT_META_DATA_SERVICE_NAME_VALUES: Set[ProbabilityOfDefaultReportMetaDataServiceName] = {
    "dynamicsBusinessCentral",
    "freshbooks",
    "oracleNetsuite",
    "quickbooks",
    "quickbooksDesktop",
    "sageBusinessCloud",
    "sageIntacct",
    "wave",
    "xero",
    "zohoBooks",
}


def check_probability_of_default_report_meta_data_service_name(
    value: str,
) -> ProbabilityOfDefaultReportMetaDataServiceName:
    if value in PROBABILITY_OF_DEFAULT_REPORT_META_DATA_SERVICE_NAME_VALUES:
        return cast(ProbabilityOfDefaultReportMetaDataServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PROBABILITY_OF_DEFAULT_REPORT_META_DATA_SERVICE_NAME_VALUES!r}"
    )
