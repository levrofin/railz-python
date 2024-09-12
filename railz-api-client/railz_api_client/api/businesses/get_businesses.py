from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.businesses_v2_response_dto import BusinessesV2ResponseDto
from ...models.error_400_response_dto_v2 import Error400ResponseDtoV2
from ...models.error_401_response_dto import Error401ResponseDto
from ...models.error_403_response_dto import Error403ResponseDto
from ...models.error_500_response_dto import Error500ResponseDto
from ...models.get_businesses_status_item import GetBusinessesStatusItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    business_name: Union[Unset, str] = UNSET,
    business_name_or_uuid: Union[Unset, str] = UNSET,
    integration_uuids: Union[Unset, List[str]] = UNSET,
    status: Union[Unset, List[GetBusinessesStatusItem]] = UNSET,
    limit: Union[Unset, float] = UNSET,
    offset: Union[Unset, float] = UNSET,
    additional_query_params: dict[str, str] | list[tuple[str, str]] | None = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    if additional_query_params:
        params.update(additional_query_params)

    params["businessName"] = business_name

    params["businessNameOrUuid"] = business_name_or_uuid

    json_integration_uuids: Union[Unset, List[str]] = UNSET
    if not isinstance(integration_uuids, Unset):
        json_integration_uuids = integration_uuids

    params["integrationUuids"] = json_integration_uuids

    json_status: Union[Unset, List[str]] = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item: str = status_item_data
            json_status.append(status_item)

    params["status"] = json_status

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v2/businesses",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        Any,
        BusinessesV2ResponseDto,
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = BusinessesV2ResponseDto.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = BusinessesV2ResponseDto.from_dict(response.json())

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
        BusinessesV2ResponseDto,
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
    business_name: Union[Unset, str] = UNSET,
    business_name_or_uuid: Union[Unset, str] = UNSET,
    integration_uuids: Union[Unset, List[str]] = UNSET,
    status: Union[Unset, List[GetBusinessesStatusItem]] = UNSET,
    limit: Union[Unset, float] = UNSET,
    offset: Union[Unset, float] = UNSET,
    additional_query_params: dict[str, str] | list[tuple[str, str]] | None = None,
) -> Response[
    Union[
        Any,
        BusinessesV2ResponseDto,
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
    ]
]:
    """List Businesses

    Args:
        business_name (Union[Unset, str]):
        business_name_or_uuid (Union[Unset, str]):
        integration_uuids (Union[Unset, List[str]]):
        status (Union[Unset, List[GetBusinessesStatusItem]]):
        limit (Union[Unset, float]):
        offset (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BusinessesV2ResponseDto, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto]]
    """

    kwargs = _get_kwargs(
        business_name=business_name,
        business_name_or_uuid=business_name_or_uuid,
        integration_uuids=integration_uuids,
        status=status,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    business_name: Union[Unset, str] = UNSET,
    business_name_or_uuid: Union[Unset, str] = UNSET,
    integration_uuids: Union[Unset, List[str]] = UNSET,
    status: Union[Unset, List[GetBusinessesStatusItem]] = UNSET,
    limit: Union[Unset, float] = UNSET,
    offset: Union[Unset, float] = UNSET,
    additional_query_params: dict[str, str] | list[tuple[str, str]] | None = None,
) -> Optional[
    Union[
        Any,
        BusinessesV2ResponseDto,
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
    ]
]:
    """List Businesses

    Args:
        business_name (Union[Unset, str]):
        business_name_or_uuid (Union[Unset, str]):
        integration_uuids (Union[Unset, List[str]]):
        status (Union[Unset, List[GetBusinessesStatusItem]]):
        limit (Union[Unset, float]):
        offset (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BusinessesV2ResponseDto, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto]
    """

    return sync_detailed(
        client=client,
        business_name=business_name,
        business_name_or_uuid=business_name_or_uuid,
        integration_uuids=integration_uuids,
        status=status,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    business_name: Union[Unset, str] = UNSET,
    business_name_or_uuid: Union[Unset, str] = UNSET,
    integration_uuids: Union[Unset, List[str]] = UNSET,
    status: Union[Unset, List[GetBusinessesStatusItem]] = UNSET,
    limit: Union[Unset, float] = UNSET,
    offset: Union[Unset, float] = UNSET,
    additional_query_params: dict[str, str] | list[tuple[str, str]] | None = None,
) -> Response[
    Union[
        Any,
        BusinessesV2ResponseDto,
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
    ]
]:
    """List Businesses

    Args:
        business_name (Union[Unset, str]):
        business_name_or_uuid (Union[Unset, str]):
        integration_uuids (Union[Unset, List[str]]):
        status (Union[Unset, List[GetBusinessesStatusItem]]):
        limit (Union[Unset, float]):
        offset (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BusinessesV2ResponseDto, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto]]
    """

    kwargs = _get_kwargs(
        business_name=business_name,
        business_name_or_uuid=business_name_or_uuid,
        integration_uuids=integration_uuids,
        status=status,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    business_name: Union[Unset, str] = UNSET,
    business_name_or_uuid: Union[Unset, str] = UNSET,
    integration_uuids: Union[Unset, List[str]] = UNSET,
    status: Union[Unset, List[GetBusinessesStatusItem]] = UNSET,
    limit: Union[Unset, float] = UNSET,
    offset: Union[Unset, float] = UNSET,
    additional_query_params: dict[str, str] | list[tuple[str, str]] | None = None,
) -> Optional[
    Union[
        Any,
        BusinessesV2ResponseDto,
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
    ]
]:
    """List Businesses

    Args:
        business_name (Union[Unset, str]):
        business_name_or_uuid (Union[Unset, str]):
        integration_uuids (Union[Unset, List[str]]):
        status (Union[Unset, List[GetBusinessesStatusItem]]):
        limit (Union[Unset, float]):
        offset (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BusinessesV2ResponseDto, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            business_name=business_name,
            business_name_or_uuid=business_name_or_uuid,
            integration_uuids=integration_uuids,
            status=status,
            limit=limit,
            offset=offset,
        )
    ).parsed
