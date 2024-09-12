from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400_response_dto_v2 import Error400ResponseDtoV2
from ...models.error_401_response_dto import Error401ResponseDto
from ...models.error_403_response_dto import Error403ResponseDto
from ...models.error_500_response_dto import Error500ResponseDto
from ...models.push_purchase_order_v2_dto import PushPurchaseOrderV2Dto
from ...models.push_purchase_order_v2_response_dto import PushPurchaseOrderV2ResponseDto
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: PushPurchaseOrderV2Dto,
    additional_query_params: dict[str, str | list[str]] | None = None,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    if additional_query_params:
        params.update(additional_query_params)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v2/accounting/purchaseOrders",
        "params": params,
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
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        PushPurchaseOrderV2ResponseDto,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PushPurchaseOrderV2ResponseDto.from_dict(response.json())

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
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        PushPurchaseOrderV2ResponseDto,
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
    body: PushPurchaseOrderV2Dto,
    additional_query_params: dict[str, str | list[str]] | None = None,
) -> Response[
    Union[
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        PushPurchaseOrderV2ResponseDto,
    ]
]:
    """Create a Purchase Order

     **Supported for:**

    `quickbooks` `xero` `oracleNetsuite` `dynamicsBusinessCentral` `zohoBooks`

    Args:
        body (PushPurchaseOrderV2Dto):
        additional_query_params: extra query params

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, PushPurchaseOrderV2ResponseDto]]
    """

    kwargs = _get_kwargs(
        body=body,
        additional_query_params=additional_query_params,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PushPurchaseOrderV2Dto,
    additional_query_params: dict[str, str | list[str]] | None = None,
) -> Optional[
    Union[
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        PushPurchaseOrderV2ResponseDto,
    ]
]:
    """Create a Purchase Order

     **Supported for:**

    `quickbooks` `xero` `oracleNetsuite` `dynamicsBusinessCentral` `zohoBooks`

    Args:
        body (PushPurchaseOrderV2Dto):
        additional_query_params: extra query params

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, PushPurchaseOrderV2ResponseDto]
    """

    return sync_detailed(
        client=client,
        body=body,
        additional_query_params=additional_query_params,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PushPurchaseOrderV2Dto,
    additional_query_params: dict[str, str | list[str]] | None = None,
) -> Response[
    Union[
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        PushPurchaseOrderV2ResponseDto,
    ]
]:
    """Create a Purchase Order

     **Supported for:**

    `quickbooks` `xero` `oracleNetsuite` `dynamicsBusinessCentral` `zohoBooks`

    Args:
        body (PushPurchaseOrderV2Dto):
        additional_query_params: extra query params

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, PushPurchaseOrderV2ResponseDto]]
    """

    kwargs = _get_kwargs(
        body=body,
        additional_query_params=additional_query_params,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PushPurchaseOrderV2Dto,
    additional_query_params: dict[str, str | list[str]] | None = None,
) -> Optional[
    Union[
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        PushPurchaseOrderV2ResponseDto,
    ]
]:
    """Create a Purchase Order

     **Supported for:**

    `quickbooks` `xero` `oracleNetsuite` `dynamicsBusinessCentral` `zohoBooks`

    Args:
        body (PushPurchaseOrderV2Dto):
        additional_query_params: extra query params

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, PushPurchaseOrderV2ResponseDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            additional_query_params=additional_query_params,
        )
    ).parsed
