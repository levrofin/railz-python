from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400_response_dto_v2 import Error400ResponseDtoV2
from ...models.error_401_response_dto import Error401ResponseDto
from ...models.error_403_response_dto import Error403ResponseDto
from ...models.error_500_response_dto import Error500ResponseDto
from ...models.sync_info_response_v2_dto import SyncInfoResponseV2Dto
from ...models.sync_info_sync_type import SyncInfoSyncType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    connection_uuid: str,
    request_id: Union[Unset, str] = UNSET,
    sync_type: Union[Unset, SyncInfoSyncType] = UNSET,
    additional_query_params: dict[str, str] | list[tuple[str, str]] | None = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    if additional_query_params:
        params.update(additional_query_params)

    params["connectionUuid"] = connection_uuid

    params["requestId"] = request_id

    json_sync_type: Union[Unset, str] = UNSET
    if not isinstance(sync_type, Unset):
        json_sync_type = sync_type

    params["syncType"] = json_sync_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v2/data/syncInfo",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, SyncInfoResponseV2Dto]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SyncInfoResponseV2Dto.from_dict(response.json())

        return response_200
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
    Union[Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, SyncInfoResponseV2Dto]
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
    request_id: Union[Unset, str] = UNSET,
    sync_type: Union[Unset, SyncInfoSyncType] = UNSET,
    additional_query_params: dict[str, str] | list[tuple[str, str]] | None = None,
) -> Response[
    Union[Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, SyncInfoResponseV2Dto]
]:
    """Fetch Latest Sync Information

     Gets info related to the latest synchronization of a business connection.

    Args:
        connection_uuid (str):
        request_id (Union[Unset, str]):
        sync_type (Union[Unset, SyncInfoSyncType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, SyncInfoResponseV2Dto]]
    """

    kwargs = _get_kwargs(
        connection_uuid=connection_uuid,
        request_id=request_id,
        sync_type=sync_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    connection_uuid: str,
    request_id: Union[Unset, str] = UNSET,
    sync_type: Union[Unset, SyncInfoSyncType] = UNSET,
    additional_query_params: dict[str, str] | list[tuple[str, str]] | None = None,
) -> Optional[
    Union[Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, SyncInfoResponseV2Dto]
]:
    """Fetch Latest Sync Information

     Gets info related to the latest synchronization of a business connection.

    Args:
        connection_uuid (str):
        request_id (Union[Unset, str]):
        sync_type (Union[Unset, SyncInfoSyncType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, SyncInfoResponseV2Dto]
    """

    return sync_detailed(
        client=client,
        connection_uuid=connection_uuid,
        request_id=request_id,
        sync_type=sync_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    connection_uuid: str,
    request_id: Union[Unset, str] = UNSET,
    sync_type: Union[Unset, SyncInfoSyncType] = UNSET,
    additional_query_params: dict[str, str] | list[tuple[str, str]] | None = None,
) -> Response[
    Union[Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, SyncInfoResponseV2Dto]
]:
    """Fetch Latest Sync Information

     Gets info related to the latest synchronization of a business connection.

    Args:
        connection_uuid (str):
        request_id (Union[Unset, str]):
        sync_type (Union[Unset, SyncInfoSyncType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, SyncInfoResponseV2Dto]]
    """

    kwargs = _get_kwargs(
        connection_uuid=connection_uuid,
        request_id=request_id,
        sync_type=sync_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    connection_uuid: str,
    request_id: Union[Unset, str] = UNSET,
    sync_type: Union[Unset, SyncInfoSyncType] = UNSET,
    additional_query_params: dict[str, str] | list[tuple[str, str]] | None = None,
) -> Optional[
    Union[Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, SyncInfoResponseV2Dto]
]:
    """Fetch Latest Sync Information

     Gets info related to the latest synchronization of a business connection.

    Args:
        connection_uuid (str):
        request_id (Union[Unset, str]):
        sync_type (Union[Unset, SyncInfoSyncType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, SyncInfoResponseV2Dto]
    """

    return (
        await asyncio_detailed(
            client=client,
            connection_uuid=connection_uuid,
            request_id=request_id,
            sync_type=sync_type,
        )
    ).parsed
