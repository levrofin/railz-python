from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400_response_dto_v2 import Error400ResponseDtoV2
from ...models.error_401_response_dto import Error401ResponseDto
from ...models.error_403_response_dto import Error403ResponseDto
from ...models.error_500_response_dto import Error500ResponseDto
from ...models.put_businesses_response_dto_v2 import PutBusinessesResponseDtoV2
from ...models.update_business_dto_v2 import UpdateBusinessDtoV2
from ...types import Response


def _get_kwargs(
    uuid: str,
    *,
    body: UpdateBusinessDtoV2,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/v2/businesses/{uuid}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, PutBusinessesResponseDtoV2
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PutBusinessesResponseDtoV2.from_dict(response.json())

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
    Union[
        Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, PutBusinessesResponseDtoV2
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
    body: UpdateBusinessDtoV2,
) -> Response[
    Union[
        Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, PutBusinessesResponseDtoV2
    ]
]:
    """Update a Business

    Args:
        uuid (str):
        body (UpdateBusinessDtoV2):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, PutBusinessesResponseDtoV2]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: str,
    *,
    client: AuthenticatedClient,
    body: UpdateBusinessDtoV2,
) -> Optional[
    Union[
        Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, PutBusinessesResponseDtoV2
    ]
]:
    """Update a Business

    Args:
        uuid (str):
        body (UpdateBusinessDtoV2):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, PutBusinessesResponseDtoV2]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
    body: UpdateBusinessDtoV2,
) -> Response[
    Union[
        Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, PutBusinessesResponseDtoV2
    ]
]:
    """Update a Business

    Args:
        uuid (str):
        body (UpdateBusinessDtoV2):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, PutBusinessesResponseDtoV2]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: str,
    *,
    client: AuthenticatedClient,
    body: UpdateBusinessDtoV2,
) -> Optional[
    Union[
        Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, PutBusinessesResponseDtoV2
    ]
]:
    """Update a Business

    Args:
        uuid (str):
        body (UpdateBusinessDtoV2):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, PutBusinessesResponseDtoV2]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
