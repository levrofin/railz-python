from http import HTTPStatus
from typing import Any, Dict, Mapping, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400_response_dto_v2 import Error400ResponseDtoV2
from ...models.error_401_response_dto import Error401ResponseDto
from ...models.error_403_response_dto import Error403ResponseDto
from ...models.error_500_response_dto import Error500ResponseDto
from ...models.financial_ratios_ratio import FinancialRatiosRatio
from ...models.financial_ratios_ratio_type import FinancialRatiosRatioType
from ...models.financial_ratios_reconstruct import FinancialRatiosReconstruct
from ...models.financial_ratios_report_frequency import (
    FinancialRatiosReportFrequency,
)
from ...models.financial_ratios_response_v2_dto import FinancialRatiosResponseV2Dto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    connection_uuid: str,
    report_frequency: FinancialRatiosReportFrequency,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    ratio: Union[Unset, FinancialRatiosRatio] = UNSET,
    ratio_type: Union[Unset, FinancialRatiosRatioType] = UNSET,
    offset: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    reconstruct: Union[Unset, FinancialRatiosReconstruct] = "false",
    additional_query_params: Mapping[str, str | list[str]] | None = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    if additional_query_params:
        params.update(additional_query_params)

    params["connectionUuid"] = connection_uuid

    json_report_frequency: str = report_frequency
    params["reportFrequency"] = json_report_frequency

    params["startDate"] = start_date

    params["endDate"] = end_date

    json_ratio: Union[Unset, str] = UNSET
    if not isinstance(ratio, Unset):
        json_ratio = ratio

    params["ratio"] = json_ratio

    json_ratio_type: Union[Unset, str] = UNSET
    if not isinstance(ratio_type, Unset):
        json_ratio_type = ratio_type

    params["ratioType"] = json_ratio_type

    params["offset"] = offset

    params["limit"] = limit

    params["orderBy"] = order_by

    json_reconstruct: Union[Unset, str] = UNSET
    if not isinstance(reconstruct, Unset):
        json_reconstruct = reconstruct

    params["reconstruct"] = json_reconstruct

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v2/analytics/financialRatios",
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
        FinancialRatiosResponseV2Dto,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = FinancialRatiosResponseV2Dto.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = FinancialRatiosResponseV2Dto.from_dict(response.json())

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
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        FinancialRatiosResponseV2Dto,
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
    report_frequency: FinancialRatiosReportFrequency,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    ratio: Union[Unset, FinancialRatiosRatio] = UNSET,
    ratio_type: Union[Unset, FinancialRatiosRatioType] = UNSET,
    offset: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    reconstruct: Union[Unset, FinancialRatiosReconstruct] = "false",
    additional_query_params: Mapping[str, str | list[str]] | None = None,
) -> Response[
    Union[
        Any,
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        FinancialRatiosResponseV2Dto,
    ]
]:
    """List Financial Ratios

     **Supported for:**

    `quickbooks` `xero` `freshbooks` `quickbooksDesktop` `dynamicsBusinessCentral` `zohoBooks`

    Args:
        connection_uuid (str):
        report_frequency (FinancialRatiosReportFrequency):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        ratio (Union[Unset, FinancialRatiosRatio]):
        ratio_type (Union[Unset, FinancialRatiosRatioType]):
        offset (Union[Unset, float]):
        limit (Union[Unset, float]):
        order_by (Union[Unset, str]):
        reconstruct (Union[Unset, FinancialRatiosReconstruct]):  Default: 'false'.
        additional_query_params: extra query params

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, FinancialRatiosResponseV2Dto]]
    """

    kwargs = _get_kwargs(
        connection_uuid=connection_uuid,
        report_frequency=report_frequency,
        start_date=start_date,
        end_date=end_date,
        ratio=ratio,
        ratio_type=ratio_type,
        offset=offset,
        limit=limit,
        order_by=order_by,
        reconstruct=reconstruct,
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
    report_frequency: FinancialRatiosReportFrequency,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    ratio: Union[Unset, FinancialRatiosRatio] = UNSET,
    ratio_type: Union[Unset, FinancialRatiosRatioType] = UNSET,
    offset: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    reconstruct: Union[Unset, FinancialRatiosReconstruct] = "false",
    additional_query_params: Mapping[str, str | list[str]] | None = None,
) -> Optional[
    Union[
        Any,
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        FinancialRatiosResponseV2Dto,
    ]
]:
    """List Financial Ratios

     **Supported for:**

    `quickbooks` `xero` `freshbooks` `quickbooksDesktop` `dynamicsBusinessCentral` `zohoBooks`

    Args:
        connection_uuid (str):
        report_frequency (FinancialRatiosReportFrequency):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        ratio (Union[Unset, FinancialRatiosRatio]):
        ratio_type (Union[Unset, FinancialRatiosRatioType]):
        offset (Union[Unset, float]):
        limit (Union[Unset, float]):
        order_by (Union[Unset, str]):
        reconstruct (Union[Unset, FinancialRatiosReconstruct]):  Default: 'false'.
        additional_query_params: extra query params

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, FinancialRatiosResponseV2Dto]
    """

    return sync_detailed(
        client=client,
        connection_uuid=connection_uuid,
        report_frequency=report_frequency,
        start_date=start_date,
        end_date=end_date,
        ratio=ratio,
        ratio_type=ratio_type,
        offset=offset,
        limit=limit,
        order_by=order_by,
        reconstruct=reconstruct,
        additional_query_params=additional_query_params,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    connection_uuid: str,
    report_frequency: FinancialRatiosReportFrequency,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    ratio: Union[Unset, FinancialRatiosRatio] = UNSET,
    ratio_type: Union[Unset, FinancialRatiosRatioType] = UNSET,
    offset: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    reconstruct: Union[Unset, FinancialRatiosReconstruct] = "false",
    additional_query_params: Mapping[str, str | list[str]] | None = None,
) -> Response[
    Union[
        Any,
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        FinancialRatiosResponseV2Dto,
    ]
]:
    """List Financial Ratios

     **Supported for:**

    `quickbooks` `xero` `freshbooks` `quickbooksDesktop` `dynamicsBusinessCentral` `zohoBooks`

    Args:
        connection_uuid (str):
        report_frequency (FinancialRatiosReportFrequency):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        ratio (Union[Unset, FinancialRatiosRatio]):
        ratio_type (Union[Unset, FinancialRatiosRatioType]):
        offset (Union[Unset, float]):
        limit (Union[Unset, float]):
        order_by (Union[Unset, str]):
        reconstruct (Union[Unset, FinancialRatiosReconstruct]):  Default: 'false'.
        additional_query_params: extra query params

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, FinancialRatiosResponseV2Dto]]
    """

    kwargs = _get_kwargs(
        connection_uuid=connection_uuid,
        report_frequency=report_frequency,
        start_date=start_date,
        end_date=end_date,
        ratio=ratio,
        ratio_type=ratio_type,
        offset=offset,
        limit=limit,
        order_by=order_by,
        reconstruct=reconstruct,
        additional_query_params=additional_query_params,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    connection_uuid: str,
    report_frequency: FinancialRatiosReportFrequency,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    ratio: Union[Unset, FinancialRatiosRatio] = UNSET,
    ratio_type: Union[Unset, FinancialRatiosRatioType] = UNSET,
    offset: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    reconstruct: Union[Unset, FinancialRatiosReconstruct] = "false",
    additional_query_params: Mapping[str, str | list[str]] | None = None,
) -> Optional[
    Union[
        Any,
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        FinancialRatiosResponseV2Dto,
    ]
]:
    """List Financial Ratios

     **Supported for:**

    `quickbooks` `xero` `freshbooks` `quickbooksDesktop` `dynamicsBusinessCentral` `zohoBooks`

    Args:
        connection_uuid (str):
        report_frequency (FinancialRatiosReportFrequency):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        ratio (Union[Unset, FinancialRatiosRatio]):
        ratio_type (Union[Unset, FinancialRatiosRatioType]):
        offset (Union[Unset, float]):
        limit (Union[Unset, float]):
        order_by (Union[Unset, str]):
        reconstruct (Union[Unset, FinancialRatiosReconstruct]):  Default: 'false'.
        additional_query_params: extra query params

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, FinancialRatiosResponseV2Dto]
    """

    return (
        await asyncio_detailed(
            client=client,
            connection_uuid=connection_uuid,
            report_frequency=report_frequency,
            start_date=start_date,
            end_date=end_date,
            ratio=ratio,
            ratio_type=ratio_type,
            offset=offset,
            limit=limit,
            order_by=order_by,
            reconstruct=reconstruct,
            additional_query_params=additional_query_params,
        )
    ).parsed
