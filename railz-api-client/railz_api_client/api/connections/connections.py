from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.connections_response_dto_v2 import ConnectionsResponseDtoV2
from ...models.connections_service_name import ConnectionsServiceName
from ...models.connections_status import ConnectionsStatus
from ...models.error_400_response_dto import Error400ResponseDto
from ...models.error_401_response_dto import Error401ResponseDto
from ...models.error_403_response_dto import Error403ResponseDto
from ...models.error_500_response_dto import Error500ResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    business_name: Union[Unset, str] = UNSET,
    business_uuid: Union[Unset, str] = UNSET,
    service_name: Union[Unset, ConnectionsServiceName] = UNSET,
    institution_name: Union[Unset, str] = UNSET,
    connection_uuid: Union[Unset, str] = UNSET,
    status: Union[Unset, ConnectionsStatus] = UNSET,
    limit: Union[Unset, float] = UNSET,
    offset: Union[Unset, float] = UNSET,
    service_account_ref_id: Union[Unset, str] = UNSET,
    service_account_ref_entity_ref_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["businessName"] = business_name

    params["businessUuid"] = business_uuid

    json_service_name: Union[Unset, str] = UNSET
    if not isinstance(service_name, Unset):
        json_service_name = service_name

    params["serviceName"] = json_service_name

    params["institutionName"] = institution_name

    params["connectionUuid"] = connection_uuid

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    params["limit"] = limit

    params["offset"] = offset

    params["serviceAccountRef.id"] = service_account_ref_id

    params["serviceAccountRef.entityRef.id"] = service_account_ref_entity_ref_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v2/connections",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        Any,
        ConnectionsResponseDtoV2,
        Error400ResponseDto,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ConnectionsResponseDtoV2.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = ConnectionsResponseDtoV2.from_dict(response.json())

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
        ConnectionsResponseDtoV2,
        Error400ResponseDto,
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
    business_uuid: Union[Unset, str] = UNSET,
    service_name: Union[Unset, ConnectionsServiceName] = UNSET,
    institution_name: Union[Unset, str] = UNSET,
    connection_uuid: Union[Unset, str] = UNSET,
    status: Union[Unset, ConnectionsStatus] = UNSET,
    limit: Union[Unset, float] = UNSET,
    offset: Union[Unset, float] = UNSET,
    service_account_ref_id: Union[Unset, str] = UNSET,
    service_account_ref_entity_ref_id: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        Any,
        ConnectionsResponseDtoV2,
        Error400ResponseDto,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
    ]
]:
    """List Connections

     **Supported for:**

    `freshbooks` `quickbooks` `quickbooksDesktop` `xero` `oracleNetsuite` `sageBusinessCloud`
    `sageIntacct` `dynamicsBusinessCentral` `wave` `shopify` `square` `plaid` `zohoBooks`

    Args:
        business_name (Union[Unset, str]):
        business_uuid (Union[Unset, str]):
        service_name (Union[Unset, ConnectionsServiceName]):
        institution_name (Union[Unset, str]):
        connection_uuid (Union[Unset, str]):
        status (Union[Unset, ConnectionsStatus]):
        limit (Union[Unset, float]):
        offset (Union[Unset, float]):
        service_account_ref_id (Union[Unset, str]):
        service_account_ref_entity_ref_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ConnectionsResponseDtoV2, Error400ResponseDto, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto]]
    """

    kwargs = _get_kwargs(
        business_name=business_name,
        business_uuid=business_uuid,
        service_name=service_name,
        institution_name=institution_name,
        connection_uuid=connection_uuid,
        status=status,
        limit=limit,
        offset=offset,
        service_account_ref_id=service_account_ref_id,
        service_account_ref_entity_ref_id=service_account_ref_entity_ref_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    business_name: Union[Unset, str] = UNSET,
    business_uuid: Union[Unset, str] = UNSET,
    service_name: Union[Unset, ConnectionsServiceName] = UNSET,
    institution_name: Union[Unset, str] = UNSET,
    connection_uuid: Union[Unset, str] = UNSET,
    status: Union[Unset, ConnectionsStatus] = UNSET,
    limit: Union[Unset, float] = UNSET,
    offset: Union[Unset, float] = UNSET,
    service_account_ref_id: Union[Unset, str] = UNSET,
    service_account_ref_entity_ref_id: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        Any,
        ConnectionsResponseDtoV2,
        Error400ResponseDto,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
    ]
]:
    """List Connections

     **Supported for:**

    `freshbooks` `quickbooks` `quickbooksDesktop` `xero` `oracleNetsuite` `sageBusinessCloud`
    `sageIntacct` `dynamicsBusinessCentral` `wave` `shopify` `square` `plaid` `zohoBooks`

    Args:
        business_name (Union[Unset, str]):
        business_uuid (Union[Unset, str]):
        service_name (Union[Unset, ConnectionsServiceName]):
        institution_name (Union[Unset, str]):
        connection_uuid (Union[Unset, str]):
        status (Union[Unset, ConnectionsStatus]):
        limit (Union[Unset, float]):
        offset (Union[Unset, float]):
        service_account_ref_id (Union[Unset, str]):
        service_account_ref_entity_ref_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ConnectionsResponseDtoV2, Error400ResponseDto, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto]
    """

    return sync_detailed(
        client=client,
        business_name=business_name,
        business_uuid=business_uuid,
        service_name=service_name,
        institution_name=institution_name,
        connection_uuid=connection_uuid,
        status=status,
        limit=limit,
        offset=offset,
        service_account_ref_id=service_account_ref_id,
        service_account_ref_entity_ref_id=service_account_ref_entity_ref_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    business_name: Union[Unset, str] = UNSET,
    business_uuid: Union[Unset, str] = UNSET,
    service_name: Union[Unset, ConnectionsServiceName] = UNSET,
    institution_name: Union[Unset, str] = UNSET,
    connection_uuid: Union[Unset, str] = UNSET,
    status: Union[Unset, ConnectionsStatus] = UNSET,
    limit: Union[Unset, float] = UNSET,
    offset: Union[Unset, float] = UNSET,
    service_account_ref_id: Union[Unset, str] = UNSET,
    service_account_ref_entity_ref_id: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        Any,
        ConnectionsResponseDtoV2,
        Error400ResponseDto,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
    ]
]:
    """List Connections

     **Supported for:**

    `freshbooks` `quickbooks` `quickbooksDesktop` `xero` `oracleNetsuite` `sageBusinessCloud`
    `sageIntacct` `dynamicsBusinessCentral` `wave` `shopify` `square` `plaid` `zohoBooks`

    Args:
        business_name (Union[Unset, str]):
        business_uuid (Union[Unset, str]):
        service_name (Union[Unset, ConnectionsServiceName]):
        institution_name (Union[Unset, str]):
        connection_uuid (Union[Unset, str]):
        status (Union[Unset, ConnectionsStatus]):
        limit (Union[Unset, float]):
        offset (Union[Unset, float]):
        service_account_ref_id (Union[Unset, str]):
        service_account_ref_entity_ref_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ConnectionsResponseDtoV2, Error400ResponseDto, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto]]
    """

    kwargs = _get_kwargs(
        business_name=business_name,
        business_uuid=business_uuid,
        service_name=service_name,
        institution_name=institution_name,
        connection_uuid=connection_uuid,
        status=status,
        limit=limit,
        offset=offset,
        service_account_ref_id=service_account_ref_id,
        service_account_ref_entity_ref_id=service_account_ref_entity_ref_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    business_name: Union[Unset, str] = UNSET,
    business_uuid: Union[Unset, str] = UNSET,
    service_name: Union[Unset, ConnectionsServiceName] = UNSET,
    institution_name: Union[Unset, str] = UNSET,
    connection_uuid: Union[Unset, str] = UNSET,
    status: Union[Unset, ConnectionsStatus] = UNSET,
    limit: Union[Unset, float] = UNSET,
    offset: Union[Unset, float] = UNSET,
    service_account_ref_id: Union[Unset, str] = UNSET,
    service_account_ref_entity_ref_id: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        Any,
        ConnectionsResponseDtoV2,
        Error400ResponseDto,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
    ]
]:
    """List Connections

     **Supported for:**

    `freshbooks` `quickbooks` `quickbooksDesktop` `xero` `oracleNetsuite` `sageBusinessCloud`
    `sageIntacct` `dynamicsBusinessCentral` `wave` `shopify` `square` `plaid` `zohoBooks`

    Args:
        business_name (Union[Unset, str]):
        business_uuid (Union[Unset, str]):
        service_name (Union[Unset, ConnectionsServiceName]):
        institution_name (Union[Unset, str]):
        connection_uuid (Union[Unset, str]):
        status (Union[Unset, ConnectionsStatus]):
        limit (Union[Unset, float]):
        offset (Union[Unset, float]):
        service_account_ref_id (Union[Unset, str]):
        service_account_ref_entity_ref_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ConnectionsResponseDtoV2, Error400ResponseDto, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            business_name=business_name,
            business_uuid=business_uuid,
            service_name=service_name,
            institution_name=institution_name,
            connection_uuid=connection_uuid,
            status=status,
            limit=limit,
            offset=offset,
            service_account_ref_id=service_account_ref_id,
            service_account_ref_entity_ref_id=service_account_ref_entity_ref_id,
        )
    ).parsed
