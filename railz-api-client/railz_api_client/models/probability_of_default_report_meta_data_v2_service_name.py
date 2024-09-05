from typing import Literal, Set, cast

ProbabilityOfDefaultReportMetaDataV2ServiceName = Literal[
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

PROBABILITY_OF_DEFAULT_REPORT_META_DATA_V2_SERVICE_NAME_VALUES: Set[ProbabilityOfDefaultReportMetaDataV2ServiceName] = {
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


def check_probability_of_default_report_meta_data_v2_service_name(
    value: str,
) -> ProbabilityOfDefaultReportMetaDataV2ServiceName:
    if value in PROBABILITY_OF_DEFAULT_REPORT_META_DATA_V2_SERVICE_NAME_VALUES:
        return cast(ProbabilityOfDefaultReportMetaDataV2ServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PROBABILITY_OF_DEFAULT_REPORT_META_DATA_V2_SERVICE_NAME_VALUES!r}"
    )
