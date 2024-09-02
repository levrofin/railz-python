from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400_response_dto_v2 import Error400ResponseDtoV2
from ...models.error_401_response_dto import Error401ResponseDto
from ...models.error_403_response_dto import Error403ResponseDto
from ...models.error_500_response_dto import Error500ResponseDto
from ...models.get_inventory_response_v2_dto import GetInventoryResponseV2Dto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    connection_uuid: str,
    offset: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = UNSET,
    order_by: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["connectionUuid"] = connection_uuid

    params["offset"] = offset

    params["limit"] = limit

    params["orderBy"] = order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v2/accounting/inventory",
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
        GetInventoryResponseV2Dto,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetInventoryResponseV2Dto.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = GetInventoryResponseV2Dto.from_dict(response.json())

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
        GetInventoryResponseV2Dto,
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
    offset: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = UNSET,
    order_by: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        Any,
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        GetInventoryResponseV2Dto,
    ]
]:
    """List Inventory Items

     **Supported for:**

    `quickbooks` `xero` `freshbooks` `quickbooksDesktop` `sageIntacct` `sageBusinessCloud`
    `oracleNetsuite` `dynamicsBusinessCentral` `wave` `zohoBooks`

    Args:
        connection_uuid (str):
        offset (Union[Unset, float]):
        limit (Union[Unset, float]):
        order_by (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, GetInventoryResponseV2Dto]]
    """

    kwargs = _get_kwargs(
        connection_uuid=connection_uuid,
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
    connection_uuid: str,
    offset: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = UNSET,
    order_by: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        Any,
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        GetInventoryResponseV2Dto,
    ]
]:
    """List Inventory Items

     **Supported for:**

    `quickbooks` `xero` `freshbooks` `quickbooksDesktop` `sageIntacct` `sageBusinessCloud`
    `oracleNetsuite` `dynamicsBusinessCentral` `wave` `zohoBooks`

    Args:
        connection_uuid (str):
        offset (Union[Unset, float]):
        limit (Union[Unset, float]):
        order_by (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, GetInventoryResponseV2Dto]
    """

    return sync_detailed(
        client=client,
        connection_uuid=connection_uuid,
        offset=offset,
        limit=limit,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    connection_uuid: str,
    offset: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = UNSET,
    order_by: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        Any,
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        GetInventoryResponseV2Dto,
    ]
]:
    """List Inventory Items

     **Supported for:**

    `quickbooks` `xero` `freshbooks` `quickbooksDesktop` `sageIntacct` `sageBusinessCloud`
    `oracleNetsuite` `dynamicsBusinessCentral` `wave` `zohoBooks`

    Args:
        connection_uuid (str):
        offset (Union[Unset, float]):
        limit (Union[Unset, float]):
        order_by (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, GetInventoryResponseV2Dto]]
    """

    kwargs = _get_kwargs(
        connection_uuid=connection_uuid,
        offset=offset,
        limit=limit,
        order_by=order_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    connection_uuid: str,
    offset: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = UNSET,
    order_by: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        Any,
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        GetInventoryResponseV2Dto,
    ]
]:
    """List Inventory Items

     **Supported for:**

    `quickbooks` `xero` `freshbooks` `quickbooksDesktop` `sageIntacct` `sageBusinessCloud`
    `oracleNetsuite` `dynamicsBusinessCentral` `wave` `zohoBooks`

    Args:
        connection_uuid (str):
        offset (Union[Unset, float]):
        limit (Union[Unset, float]):
        order_by (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, GetInventoryResponseV2Dto]
    """

    return (
        await asyncio_detailed(
            client=client,
            connection_uuid=connection_uuid,
            offset=offset,
            limit=limit,
            order_by=order_by,
        )
    ).parsed
