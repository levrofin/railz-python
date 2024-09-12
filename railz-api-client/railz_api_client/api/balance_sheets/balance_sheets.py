from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.balance_sheets_accounting_method import (
    BalanceSheetsAccountingMethod,
)
from ...models.balance_sheets_report_frequency import (
    BalanceSheetsReportFrequency,
)
from ...models.balance_sheets_response_v2_dto import BalanceSheetsResponseV2Dto
from ...models.balance_sheets_section import BalanceSheetsSection
from ...models.balance_sheets_sub_section import BalanceSheetsSubSection
from ...models.error_400_response_dto_v2 import Error400ResponseDtoV2
from ...models.error_401_response_dto import Error401ResponseDto
from ...models.error_403_response_dto import Error403ResponseDto
from ...models.error_500_response_dto import Error500ResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    connection_uuid: str,
    accounting_method: Union[Unset, BalanceSheetsAccountingMethod] = "accrual",
    report_frequency: BalanceSheetsReportFrequency,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    section: Union[Unset, BalanceSheetsSection] = UNSET,
    sub_section: Union[Unset, BalanceSheetsSubSection] = UNSET,
    group: Union[Unset, str] = UNSET,
    sub_group: Union[Unset, str] = UNSET,
    account_id: Union[Unset, str] = UNSET,
    sub_account_id: Union[Unset, str] = UNSET,
    account: Union[Unset, str] = UNSET,
    value: Union[Unset, float] = UNSET,
    offset: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    additional_query_params: dict[str, str | list[str]] | None = None,
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
        "url": "/v2/accounting/balanceSheets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        Any,
        BalanceSheetsResponseV2Dto,
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = BalanceSheetsResponseV2Dto.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = BalanceSheetsResponseV2Dto.from_dict(response.json())

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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        Any,
        BalanceSheetsResponseV2Dto,
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    connection_uuid: str,
    accounting_method: Union[Unset, BalanceSheetsAccountingMethod] = "accrual",
    report_frequency: BalanceSheetsReportFrequency,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    section: Union[Unset, BalanceSheetsSection] = UNSET,
    sub_section: Union[Unset, BalanceSheetsSubSection] = UNSET,
    group: Union[Unset, str] = UNSET,
    sub_group: Union[Unset, str] = UNSET,
    account_id: Union[Unset, str] = UNSET,
    sub_account_id: Union[Unset, str] = UNSET,
    account: Union[Unset, str] = UNSET,
    value: Union[Unset, float] = UNSET,
    offset: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    additional_query_params: dict[str, str | list[str]] | None = None,
) -> Response[
    Union[
        Any,
        BalanceSheetsResponseV2Dto,
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
    ]
]:
    """List Balance Sheets

     **Supported for:**

    `quickbooks` `xero` `freshbooks` `quickbooksDesktop` `dynamicsBusinessCentral` `zohoBooks`

    Args:
        connection_uuid (str):
        accounting_method (Union[Unset, BalanceSheetsAccountingMethod]):  Default: 'accrual'.
        report_frequency (BalanceSheetsReportFrequency):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        section (Union[Unset, BalanceSheetsSection]):
        sub_section (Union[Unset, BalanceSheetsSubSection]):
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
        Response[Union[Any, BalanceSheetsResponseV2Dto, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto]]
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

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    connection_uuid: str,
    accounting_method: Union[Unset, BalanceSheetsAccountingMethod] = "accrual",
    report_frequency: BalanceSheetsReportFrequency,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    section: Union[Unset, BalanceSheetsSection] = UNSET,
    sub_section: Union[Unset, BalanceSheetsSubSection] = UNSET,
    group: Union[Unset, str] = UNSET,
    sub_group: Union[Unset, str] = UNSET,
    account_id: Union[Unset, str] = UNSET,
    sub_account_id: Union[Unset, str] = UNSET,
    account: Union[Unset, str] = UNSET,
    value: Union[Unset, float] = UNSET,
    offset: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    additional_query_params: dict[str, str | list[str]] | None = None,
) -> Optional[
    Union[
        Any,
        BalanceSheetsResponseV2Dto,
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
    ]
]:
    """List Balance Sheets

     **Supported for:**

    `quickbooks` `xero` `freshbooks` `quickbooksDesktop` `dynamicsBusinessCentral` `zohoBooks`

    Args:
        connection_uuid (str):
        accounting_method (Union[Unset, BalanceSheetsAccountingMethod]):  Default: 'accrual'.
        report_frequency (BalanceSheetsReportFrequency):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        section (Union[Unset, BalanceSheetsSection]):
        sub_section (Union[Unset, BalanceSheetsSubSection]):
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
        Union[Any, BalanceSheetsResponseV2Dto, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto]
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
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    connection_uuid: str,
    accounting_method: Union[Unset, BalanceSheetsAccountingMethod] = "accrual",
    report_frequency: BalanceSheetsReportFrequency,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    section: Union[Unset, BalanceSheetsSection] = UNSET,
    sub_section: Union[Unset, BalanceSheetsSubSection] = UNSET,
    group: Union[Unset, str] = UNSET,
    sub_group: Union[Unset, str] = UNSET,
    account_id: Union[Unset, str] = UNSET,
    sub_account_id: Union[Unset, str] = UNSET,
    account: Union[Unset, str] = UNSET,
    value: Union[Unset, float] = UNSET,
    offset: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    additional_query_params: dict[str, str | list[str]] | None = None,
) -> Response[
    Union[
        Any,
        BalanceSheetsResponseV2Dto,
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
    ]
]:
    """List Balance Sheets

     **Supported for:**

    `quickbooks` `xero` `freshbooks` `quickbooksDesktop` `dynamicsBusinessCentral` `zohoBooks`

    Args:
        connection_uuid (str):
        accounting_method (Union[Unset, BalanceSheetsAccountingMethod]):  Default: 'accrual'.
        report_frequency (BalanceSheetsReportFrequency):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        section (Union[Unset, BalanceSheetsSection]):
        sub_section (Union[Unset, BalanceSheetsSubSection]):
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
        Response[Union[Any, BalanceSheetsResponseV2Dto, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto]]
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

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    connection_uuid: str,
    accounting_method: Union[Unset, BalanceSheetsAccountingMethod] = "accrual",
    report_frequency: BalanceSheetsReportFrequency,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    section: Union[Unset, BalanceSheetsSection] = UNSET,
    sub_section: Union[Unset, BalanceSheetsSubSection] = UNSET,
    group: Union[Unset, str] = UNSET,
    sub_group: Union[Unset, str] = UNSET,
    account_id: Union[Unset, str] = UNSET,
    sub_account_id: Union[Unset, str] = UNSET,
    account: Union[Unset, str] = UNSET,
    value: Union[Unset, float] = UNSET,
    offset: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    additional_query_params: dict[str, str | list[str]] | None = None,
) -> Optional[
    Union[
        Any,
        BalanceSheetsResponseV2Dto,
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
    ]
]:
    """List Balance Sheets

     **Supported for:**

    `quickbooks` `xero` `freshbooks` `quickbooksDesktop` `dynamicsBusinessCentral` `zohoBooks`

    Args:
        connection_uuid (str):
        accounting_method (Union[Unset, BalanceSheetsAccountingMethod]):  Default: 'accrual'.
        report_frequency (BalanceSheetsReportFrequency):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        section (Union[Unset, BalanceSheetsSection]):
        sub_section (Union[Unset, BalanceSheetsSubSection]):
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
        Union[Any, BalanceSheetsResponseV2Dto, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto]
    """

    return (
        await asyncio_detailed(
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
        )
    ).parsed
