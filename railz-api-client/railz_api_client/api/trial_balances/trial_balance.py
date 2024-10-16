from http import HTTPStatus
from typing import Any, Dict, Mapping, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400_response_dto_v2 import Error400ResponseDtoV2
from ...models.error_401_response_dto import Error401ResponseDto
from ...models.error_403_response_dto import Error403ResponseDto
from ...models.error_500_response_dto import Error500ResponseDto
from ...models.trial_balance_accounting_method import (
    TrialBalanceAccountingMethod,
)
from ...models.trial_balance_report_frequency import TrialBalanceReportFrequency
from ...models.trial_balance_section import TrialBalanceSection
from ...models.trial_balance_sub_section import TrialBalanceSubSection
from ...models.trial_balances_response_v2_dto import TrialBalancesResponseV2Dto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    connection_uuid: str,
    report_frequency: TrialBalanceReportFrequency,
    accounting_method: Union[Unset, TrialBalanceAccountingMethod] = "accrual",
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    section: Union[Unset, TrialBalanceSection] = UNSET,
    sub_section: Union[Unset, TrialBalanceSubSection] = UNSET,
    group: Union[Unset, str] = UNSET,
    sub_group: Union[Unset, str] = UNSET,
    account_id: Union[Unset, str] = UNSET,
    sub_account_id: Union[Unset, str] = UNSET,
    account: Union[Unset, str] = UNSET,
    debit: Union[Unset, float] = UNSET,
    credit: Union[Unset, float] = UNSET,
    ytd_debit: Union[Unset, float] = UNSET,
    ytd_credit: Union[Unset, float] = UNSET,
    offset: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    additional_query_params: Mapping[str, str | list[str]] | None = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    if additional_query_params:
        params.update(additional_query_params)

    params["connectionUuid"] = connection_uuid

    json_report_frequency: str = report_frequency
    params["reportFrequency"] = json_report_frequency

    json_accounting_method: Union[Unset, str] = UNSET
    if not isinstance(accounting_method, Unset):
        json_accounting_method = accounting_method

    params["accountingMethod"] = json_accounting_method

    params["startDate"] = start_date

    params["endDate"] = end_date

    json_section: Union[Unset, str] = UNSET
    if not isinstance(section, Unset):
        json_section = section

    params["section"] = json_section

    json_sub_section: Union[Unset, str] = UNSET
    if not isinstance(sub_section, Unset):
        json_sub_section = sub_section

    params["subSection"] = json_sub_section

    params["group"] = group

    params["subGroup"] = sub_group

    params["accountId"] = account_id

    params["subAccountId"] = sub_account_id

    params["account"] = account

    params["debit"] = debit

    params["credit"] = credit

    params["ytdDebit"] = ytd_debit

    params["ytdCredit"] = ytd_credit

    params["offset"] = offset

    params["limit"] = limit

    params["orderBy"] = order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v2/accounting/trialBalances",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        Any,
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        TrialBalancesResponseV2Dto,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TrialBalancesResponseV2Dto.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = TrialBalancesResponseV2Dto.from_dict(response.json())

        return response_202
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Error400ResponseDtoV2.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Error401ResponseDto.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Error403ResponseDto.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Error500ResponseDto.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response, skip_parsing: bool = False
) -> Response[
    Union[
        Any,
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        TrialBalancesResponseV2Dto,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=None if skip_parsing else _parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    connection_uuid: str,
    report_frequency: TrialBalanceReportFrequency,
    accounting_method: Union[Unset, TrialBalanceAccountingMethod] = "accrual",
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    section: Union[Unset, TrialBalanceSection] = UNSET,
    sub_section: Union[Unset, TrialBalanceSubSection] = UNSET,
    group: Union[Unset, str] = UNSET,
    sub_group: Union[Unset, str] = UNSET,
    account_id: Union[Unset, str] = UNSET,
    sub_account_id: Union[Unset, str] = UNSET,
    account: Union[Unset, str] = UNSET,
    debit: Union[Unset, float] = UNSET,
    credit: Union[Unset, float] = UNSET,
    ytd_debit: Union[Unset, float] = UNSET,
    ytd_credit: Union[Unset, float] = UNSET,
    offset: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    additional_query_params: Mapping[str, str | list[str]] | None = None,
    skip_parsing: bool = False,
) -> Response[
    Union[
        Any,
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        TrialBalancesResponseV2Dto,
    ]
]:
    """List Trial Balances

     **Supported for:**

    `quickbooks` `xero` `freshbooks` `quickbooksDesktop` `sageIntacct` `sageBusinessCloud`
    `oracleNetsuite` `dynamicsBusinessCentral` `zohoBooks`

    Args:
        connection_uuid (str):
        report_frequency (TrialBalanceReportFrequency):
        accounting_method (Union[Unset, TrialBalanceAccountingMethod]):  Default: 'accrual'.
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        section (Union[Unset, TrialBalanceSection]):
        sub_section (Union[Unset, TrialBalanceSubSection]):
        group (Union[Unset, str]):
        sub_group (Union[Unset, str]):
        account_id (Union[Unset, str]):
        sub_account_id (Union[Unset, str]):
        account (Union[Unset, str]):
        debit (Union[Unset, float]):
        credit (Union[Unset, float]):
        ytd_debit (Union[Unset, float]):
        ytd_credit (Union[Unset, float]):
        offset (Union[Unset, float]):
        limit (Union[Unset, float]):
        order_by (Union[Unset, str]):
        additional_query_params: extra query params

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, TrialBalancesResponseV2Dto]]
    """

    kwargs = _get_kwargs(
        connection_uuid=connection_uuid,
        report_frequency=report_frequency,
        accounting_method=accounting_method,
        start_date=start_date,
        end_date=end_date,
        section=section,
        sub_section=sub_section,
        group=group,
        sub_group=sub_group,
        account_id=account_id,
        sub_account_id=sub_account_id,
        account=account,
        debit=debit,
        credit=credit,
        ytd_debit=ytd_debit,
        ytd_credit=ytd_credit,
        offset=offset,
        limit=limit,
        order_by=order_by,
        additional_query_params=additional_query_params,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response, skip_parsing=skip_parsing)


def sync(
    *,
    client: AuthenticatedClient,
    connection_uuid: str,
    report_frequency: TrialBalanceReportFrequency,
    accounting_method: Union[Unset, TrialBalanceAccountingMethod] = "accrual",
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    section: Union[Unset, TrialBalanceSection] = UNSET,
    sub_section: Union[Unset, TrialBalanceSubSection] = UNSET,
    group: Union[Unset, str] = UNSET,
    sub_group: Union[Unset, str] = UNSET,
    account_id: Union[Unset, str] = UNSET,
    sub_account_id: Union[Unset, str] = UNSET,
    account: Union[Unset, str] = UNSET,
    debit: Union[Unset, float] = UNSET,
    credit: Union[Unset, float] = UNSET,
    ytd_debit: Union[Unset, float] = UNSET,
    ytd_credit: Union[Unset, float] = UNSET,
    offset: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    additional_query_params: Mapping[str, str | list[str]] | None = None,
    skip_parsing: bool = False,
) -> Optional[
    Union[
        Any,
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        TrialBalancesResponseV2Dto,
    ]
]:
    """List Trial Balances

     **Supported for:**

    `quickbooks` `xero` `freshbooks` `quickbooksDesktop` `sageIntacct` `sageBusinessCloud`
    `oracleNetsuite` `dynamicsBusinessCentral` `zohoBooks`

    Args:
        connection_uuid (str):
        report_frequency (TrialBalanceReportFrequency):
        accounting_method (Union[Unset, TrialBalanceAccountingMethod]):  Default: 'accrual'.
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        section (Union[Unset, TrialBalanceSection]):
        sub_section (Union[Unset, TrialBalanceSubSection]):
        group (Union[Unset, str]):
        sub_group (Union[Unset, str]):
        account_id (Union[Unset, str]):
        sub_account_id (Union[Unset, str]):
        account (Union[Unset, str]):
        debit (Union[Unset, float]):
        credit (Union[Unset, float]):
        ytd_debit (Union[Unset, float]):
        ytd_credit (Union[Unset, float]):
        offset (Union[Unset, float]):
        limit (Union[Unset, float]):
        order_by (Union[Unset, str]):
        additional_query_params: extra query params

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, TrialBalancesResponseV2Dto]
    """

    return sync_detailed(
        client=client,
        connection_uuid=connection_uuid,
        report_frequency=report_frequency,
        accounting_method=accounting_method,
        start_date=start_date,
        end_date=end_date,
        section=section,
        sub_section=sub_section,
        group=group,
        sub_group=sub_group,
        account_id=account_id,
        sub_account_id=sub_account_id,
        account=account,
        debit=debit,
        credit=credit,
        ytd_debit=ytd_debit,
        ytd_credit=ytd_credit,
        offset=offset,
        limit=limit,
        order_by=order_by,
        additional_query_params=additional_query_params,
        skip_parsing=skip_parsing,
    ).parsed
