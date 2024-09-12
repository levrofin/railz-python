from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400_response_dto_v2 import Error400ResponseDtoV2
from ...models.error_401_response_dto import Error401ResponseDto
from ...models.error_403_response_dto import Error403ResponseDto
from ...models.error_500_response_dto import Error500ResponseDto
from ...models.tax_benchmarkings_response_dto import TaxBenchmarkingsResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    industry_code: str,
    region: Union[Unset, str] = UNSET,
    offset: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    additional_query_params: dict[str, str] | list[tuple[str, str]] | None = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    if additional_query_params:
        params.update(additional_query_params)

    params["industryCode"] = industry_code

    params["region"] = region

    params["offset"] = offset

    params["limit"] = limit

    params["orderBy"] = order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v2/analytics/taxBenchmarking",
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
        TaxBenchmarkingsResponseDto,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TaxBenchmarkingsResponseDto.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = TaxBenchmarkingsResponseDto.from_dict(response.json())

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
        TaxBenchmarkingsResponseDto,
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
    industry_code: str,
    region: Union[Unset, str] = UNSET,
    offset: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    additional_query_params: dict[str, str] | list[tuple[str, str]] | None = None,
) -> Response[
    Union[
        Any,
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        TaxBenchmarkingsResponseDto,
    ]
]:
    """List of Tax Benchmarks

    Args:
        industry_code (str):
        region (Union[Unset, str]):
        offset (Union[Unset, float]):
        limit (Union[Unset, float]):
        order_by (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, TaxBenchmarkingsResponseDto]]
    """

    kwargs = _get_kwargs(
        industry_code=industry_code,
        region=region,
        offset=offset,
        limit=limit,
        order_by=order_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    industry_code: str,
    region: Union[Unset, str] = UNSET,
    offset: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    additional_query_params: dict[str, str] | list[tuple[str, str]] | None = None,
) -> Optional[
    Union[
        Any,
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        TaxBenchmarkingsResponseDto,
    ]
]:
    """List of Tax Benchmarks

    Args:
        industry_code (str):
        region (Union[Unset, str]):
        offset (Union[Unset, float]):
        limit (Union[Unset, float]):
        order_by (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, TaxBenchmarkingsResponseDto]
    """

    return sync_detailed(
        client=client,
        industry_code=industry_code,
        region=region,
        offset=offset,
        limit=limit,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    industry_code: str,
    region: Union[Unset, str] = UNSET,
    offset: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    additional_query_params: dict[str, str] | list[tuple[str, str]] | None = None,
) -> Response[
    Union[
        Any,
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        TaxBenchmarkingsResponseDto,
    ]
]:
    """List of Tax Benchmarks

    Args:
        industry_code (str):
        region (Union[Unset, str]):
        offset (Union[Unset, float]):
        limit (Union[Unset, float]):
        order_by (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, TaxBenchmarkingsResponseDto]]
    """

    kwargs = _get_kwargs(
        industry_code=industry_code,
        region=region,
        offset=offset,
        limit=limit,
        order_by=order_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    industry_code: str,
    region: Union[Unset, str] = UNSET,
    offset: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    additional_query_params: dict[str, str] | list[tuple[str, str]] | None = None,
) -> Optional[
    Union[
        Any,
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        TaxBenchmarkingsResponseDto,
    ]
]:
    """List of Tax Benchmarks

    Args:
        industry_code (str):
        region (Union[Unset, str]):
        offset (Union[Unset, float]):
        limit (Union[Unset, float]):
        order_by (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, TaxBenchmarkingsResponseDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            industry_code=industry_code,
            region=region,
            offset=offset,
            limit=limit,
            order_by=order_by,
        )
    ).parsed
