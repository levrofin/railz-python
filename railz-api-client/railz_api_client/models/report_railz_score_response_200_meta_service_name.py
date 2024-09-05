from typing import Literal, Set, cast

ReportRailzScoreResponse200MetaServiceName = Literal[
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

REPORT_RAILZ_SCORE_RESPONSE_200_META_SERVICE_NAME_VALUES: Set[ReportRailzScoreResponse200MetaServiceName] = {
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


def check_report_railz_score_response_200_meta_service_name(value: str) -> ReportRailzScoreResponse200MetaServiceName:
    if value in REPORT_RAILZ_SCORE_RESPONSE_200_META_SERVICE_NAME_VALUES:
        return cast(ReportRailzScoreResponse200MetaServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_RAILZ_SCORE_RESPONSE_200_META_SERVICE_NAME_VALUES!r}"
    )
