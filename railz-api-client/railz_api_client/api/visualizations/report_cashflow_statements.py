from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400_response_dto import Error400ResponseDto
from ...models.error_401_response_dto import Error401ResponseDto
from ...models.error_403_response_dto import Error403ResponseDto
from ...models.error_500_response_dto import Error500ResponseDto
from ...models.report_cashflow_statements_accounting_method import (
    ReportCashflowStatementsAccountingMethod,
)
from ...models.report_cashflow_statements_report_frequency import (
    ReportCashflowStatementsReportFrequency,
)
from ...models.report_cashflow_statements_response_200 import ReportCashflowStatementsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    connection_uuid: str,
    start_date: str,
    end_date: str,
    report_frequency: ReportCashflowStatementsReportFrequency,
    accounting_method: Union[Unset, ReportCashflowStatementsAccountingMethod] = "accrual",
    additional_query_params: dict[str, str] | list[tuple[str, str]] | None = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    if additional_query_params:
        params.update(additional_query_params)

    params["connectionUuid"] = connection_uuid

    params["startDate"] = start_date

    params["endDate"] = end_date

    json_report_frequency: str = report_frequency
    params["reportFrequency"] = json_report_frequency

    json_accounting_method: Union[Unset, str] = UNSET
    if not isinstance(accounting_method, Unset):
        json_accounting_method = accounting_method

    params["accountingMethod"] = json_accounting_method

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v2/visualizations/cashflowStatements",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        Any,
        Error400ResponseDto,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        ReportCashflowStatementsResponse200,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ReportCashflowStatementsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = cast(Any, None)
        return response_202
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Error400ResponseDto.from_dict(response.json())

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
        Error400ResponseDto,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        ReportCashflowStatementsResponse200,
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
    start_date: str,
    end_date: str,
    report_frequency: ReportCashflowStatementsReportFrequency,
    accounting_method: Union[Unset, ReportCashflowStatementsAccountingMethod] = "accrual",
    additional_query_params: dict[str, str] | list[tuple[str, str]] | None = None,
) -> Response[
    Union[
        Any,
        Error400ResponseDto,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        ReportCashflowStatementsResponse200,
    ]
]:
    """List Cashflow report

     **Supported for:**

    `quickbooks` `dynamicsBusinessCentral` `zohoBooks`

    Args:
        connection_uuid (str):
        start_date (str):
        end_date (str):
        report_frequency (ReportCashflowStatementsReportFrequency):
        accounting_method (Union[Unset, ReportCashflowStatementsAccountingMethod]):  Default:
            'accrual'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error400ResponseDto, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, ReportCashflowStatementsResponse200]]
    """

    kwargs = _get_kwargs(
        connection_uuid=connection_uuid,
        start_date=start_date,
        end_date=end_date,
        report_frequency=report_frequency,
        accounting_method=accounting_method,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    connection_uuid: str,
    start_date: str,
    end_date: str,
    report_frequency: ReportCashflowStatementsReportFrequency,
    accounting_method: Union[Unset, ReportCashflowStatementsAccountingMethod] = "accrual",
    additional_query_params: dict[str, str] | list[tuple[str, str]] | None = None,
) -> Optional[
    Union[
        Any,
        Error400ResponseDto,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        ReportCashflowStatementsResponse200,
    ]
]:
    """List Cashflow report

     **Supported for:**

    `quickbooks` `dynamicsBusinessCentral` `zohoBooks`

    Args:
        connection_uuid (str):
        start_date (str):
        end_date (str):
        report_frequency (ReportCashflowStatementsReportFrequency):
        accounting_method (Union[Unset, ReportCashflowStatementsAccountingMethod]):  Default:
            'accrual'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error400ResponseDto, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, ReportCashflowStatementsResponse200]
    """

    return sync_detailed(
        client=client,
        connection_uuid=connection_uuid,
        start_date=start_date,
        end_date=end_date,
        report_frequency=report_frequency,
        accounting_method=accounting_method,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    connection_uuid: str,
    start_date: str,
    end_date: str,
    report_frequency: ReportCashflowStatementsReportFrequency,
    accounting_method: Union[Unset, ReportCashflowStatementsAccountingMethod] = "accrual",
    additional_query_params: dict[str, str] | list[tuple[str, str]] | None = None,
) -> Response[
    Union[
        Any,
        Error400ResponseDto,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        ReportCashflowStatementsResponse200,
    ]
]:
    """List Cashflow report

     **Supported for:**

    `quickbooks` `dynamicsBusinessCentral` `zohoBooks`

    Args:
        connection_uuid (str):
        start_date (str):
        end_date (str):
        report_frequency (ReportCashflowStatementsReportFrequency):
        accounting_method (Union[Unset, ReportCashflowStatementsAccountingMethod]):  Default:
            'accrual'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error400ResponseDto, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, ReportCashflowStatementsResponse200]]
    """

    kwargs = _get_kwargs(
        connection_uuid=connection_uuid,
        start_date=start_date,
        end_date=end_date,
        report_frequency=report_frequency,
        accounting_method=accounting_method,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    connection_uuid: str,
    start_date: str,
    end_date: str,
    report_frequency: ReportCashflowStatementsReportFrequency,
    accounting_method: Union[Unset, ReportCashflowStatementsAccountingMethod] = "accrual",
    additional_query_params: dict[str, str] | list[tuple[str, str]] | None = None,
) -> Optional[
    Union[
        Any,
        Error400ResponseDto,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        ReportCashflowStatementsResponse200,
    ]
]:
    """List Cashflow report

     **Supported for:**

    `quickbooks` `dynamicsBusinessCentral` `zohoBooks`

    Args:
        connection_uuid (str):
        start_date (str):
        end_date (str):
        report_frequency (ReportCashflowStatementsReportFrequency):
        accounting_method (Union[Unset, ReportCashflowStatementsAccountingMethod]):  Default:
            'accrual'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error400ResponseDto, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, ReportCashflowStatementsResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            connection_uuid=connection_uuid,
            start_date=start_date,
            end_date=end_date,
            report_frequency=report_frequency,
            accounting_method=accounting_method,
        )
    ).parsed
