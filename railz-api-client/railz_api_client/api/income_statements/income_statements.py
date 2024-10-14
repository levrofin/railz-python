from http import HTTPStatus
from typing import Any, Dict, Mapping, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400_response_dto_v2 import Error400ResponseDtoV2
from ...models.error_401_response_dto import Error401ResponseDto
from ...models.error_403_response_dto import Error403ResponseDto
from ...models.error_500_response_dto import Error500ResponseDto
from ...models.income_statements_accounting_method import (
    IncomeStatementsAccountingMethod,
)
from ...models.income_statements_report_frequency import (
    IncomeStatementsReportFrequency,
)
from ...models.income_statements_response_v2_dto import IncomeStatementsResponseV2Dto
from ...models.income_statements_section import IncomeStatementsSection
from ...models.income_statements_sub_section import IncomeStatementsSubSection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    connection_uuid: str,
    accounting_method: Union[Unset, IncomeStatementsAccountingMethod] = "accrual",
    report_frequency: IncomeStatementsReportFrequency,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    section: Union[Unset, IncomeStatementsSection] = UNSET,
    sub_section: Union[Unset, IncomeStatementsSubSection] = UNSET,
    group: Union[Unset, str] = UNSET,
    sub_group: Union[Unset, str] = UNSET,
    account_id: Union[Unset, str] = UNSET,
    sub_account_id: Union[Unset, str] = UNSET,
    account: Union[Unset, str] = UNSET,
    value: Union[Unset, float] = UNSET,
    offset: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    additional_query_params: Mapping[str, str | list[str]] | None = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    if additional_query_params:
        params.update(additional_query_params)

    params["connectionUuid"] = connection_uuid

    json_accounting_method: Union[Unset, str] = UNSET
    if not isinstance(accounting_method, Unset):
        json_accounting_method = accounting_method

    params["accountingMethod"] = json_accounting_method

    json_report_frequency: str = report_frequency
    params["reportFrequency"] = json_report_frequency

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

    params["value"] = value

    params["offset"] = offset

    params["limit"] = limit

    params["orderBy"] = order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v2/accounting/incomeStatements",
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
        IncomeStatementsResponseV2Dto,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = IncomeStatementsResponseV2Dto.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = IncomeStatementsResponseV2Dto.from_dict(response.json())

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
        IncomeStatementsResponseV2Dto,
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
    accounting_method: Union[Unset, IncomeStatementsAccountingMethod] = "accrual",
    report_frequency: IncomeStatementsReportFrequency,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    section: Union[Unset, IncomeStatementsSection] = UNSET,
    sub_section: Union[Unset, IncomeStatementsSubSection] = UNSET,
    group: Union[Unset, str] = UNSET,
    sub_group: Union[Unset, str] = UNSET,
    account_id: Union[Unset, str] = UNSET,
    sub_account_id: Union[Unset, str] = UNSET,
    account: Union[Unset, str] = UNSET,
    value: Union[Unset, float] = UNSET,
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
        IncomeStatementsResponseV2Dto,
    ]
]:
    """List Income Statements

     **Supported for:**

    `quickbooks` `xero` `freshbooks` `quickbooksDesktop` `dynamicsBusinessCentral` `zohoBooks`

    Args:
        connection_uuid (str):
        accounting_method (Union[Unset, IncomeStatementsAccountingMethod]):  Default: 'accrual'.
        report_frequency (IncomeStatementsReportFrequency):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        section (Union[Unset, IncomeStatementsSection]):
        sub_section (Union[Unset, IncomeStatementsSubSection]):
        group (Union[Unset, str]):
        sub_group (Union[Unset, str]):
        account_id (Union[Unset, str]):
        sub_account_id (Union[Unset, str]):
        account (Union[Unset, str]):
        value (Union[Unset, float]):
        offset (Union[Unset, float]):
        limit (Union[Unset, float]):
        order_by (Union[Unset, str]):
        additional_query_params: extra query params

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, IncomeStatementsResponseV2Dto]]
    """

    kwargs = _get_kwargs(
        connection_uuid=connection_uuid,
        accounting_method=accounting_method,
        report_frequency=report_frequency,
        start_date=start_date,
        end_date=end_date,
        section=section,
        sub_section=sub_section,
        group=group,
        sub_group=sub_group,
        account_id=account_id,
        sub_account_id=sub_account_id,
        account=account,
        value=value,
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
    accounting_method: Union[Unset, IncomeStatementsAccountingMethod] = "accrual",
    report_frequency: IncomeStatementsReportFrequency,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    section: Union[Unset, IncomeStatementsSection] = UNSET,
    sub_section: Union[Unset, IncomeStatementsSubSection] = UNSET,
    group: Union[Unset, str] = UNSET,
    sub_group: Union[Unset, str] = UNSET,
    account_id: Union[Unset, str] = UNSET,
    sub_account_id: Union[Unset, str] = UNSET,
    account: Union[Unset, str] = UNSET,
    value: Union[Unset, float] = UNSET,
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
        IncomeStatementsResponseV2Dto,
    ]
]:
    """List Income Statements

     **Supported for:**

    `quickbooks` `xero` `freshbooks` `quickbooksDesktop` `dynamicsBusinessCentral` `zohoBooks`

    Args:
        connection_uuid (str):
        accounting_method (Union[Unset, IncomeStatementsAccountingMethod]):  Default: 'accrual'.
        report_frequency (IncomeStatementsReportFrequency):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        section (Union[Unset, IncomeStatementsSection]):
        sub_section (Union[Unset, IncomeStatementsSubSection]):
        group (Union[Unset, str]):
        sub_group (Union[Unset, str]):
        account_id (Union[Unset, str]):
        sub_account_id (Union[Unset, str]):
        account (Union[Unset, str]):
        value (Union[Unset, float]):
        offset (Union[Unset, float]):
        limit (Union[Unset, float]):
        order_by (Union[Unset, str]):
        additional_query_params: extra query params

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, IncomeStatementsResponseV2Dto]
    """

    return sync_detailed(
        client=client,
        connection_uuid=connection_uuid,
        accounting_method=accounting_method,
        report_frequency=report_frequency,
        start_date=start_date,
        end_date=end_date,
        section=section,
        sub_section=sub_section,
        group=group,
        sub_group=sub_group,
        account_id=account_id,
        sub_account_id=sub_account_id,
        account=account,
        value=value,
        offset=offset,
        limit=limit,
        order_by=order_by,
        additional_query_params=additional_query_params,
        skip_parsing=skip_parsing,
    ).parsed
