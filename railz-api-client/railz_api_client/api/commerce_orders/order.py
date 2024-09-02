from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400_response_dto_v2 import Error400ResponseDtoV2
from ...models.error_401_response_dto import Error401ResponseDto
from ...models.error_403_response_dto import Error403ResponseDto
from ...models.error_500_response_dto import Error500ResponseDto
from ...models.get_order_response_v2_dto import GetOrderResponseV2Dto
from ...models.order_fulfillment_status import OrderFulfillmentStatus
from ...models.order_payment_status import OrderPaymentStatus
from ...models.order_status import OrderStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    connection_uuid: str,
    offset: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    id: Union[Unset, str] = UNSET,
    fulfillment_status: Union[Unset, OrderFulfillmentStatus] = UNSET,
    payment_status: Union[Unset, OrderPaymentStatus] = UNSET,
    status: Union[Unset, OrderStatus] = UNSET,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["connectionUuid"] = connection_uuid

    params["offset"] = offset

    params["limit"] = limit

    params["orderBy"] = order_by

    params["id"] = id

    json_fulfillment_status: Union[Unset, str] = UNSET
    if not isinstance(fulfillment_status, Unset):
        json_fulfillment_status = fulfillment_status

    params["fulfillmentStatus"] = json_fulfillment_status

    json_payment_status: Union[Unset, str] = UNSET
    if not isinstance(payment_status, Unset):
        json_payment_status = payment_status

    params["paymentStatus"] = json_payment_status

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    params["startDate"] = start_date

    params["endDate"] = end_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v2/commerce/orders",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        Any, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, GetOrderResponseV2Dto
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetOrderResponseV2Dto.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = GetOrderResponseV2Dto.from_dict(response.json())

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
        Any, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, GetOrderResponseV2Dto
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
    id: Union[Unset, str] = UNSET,
    fulfillment_status: Union[Unset, OrderFulfillmentStatus] = UNSET,
    payment_status: Union[Unset, OrderPaymentStatus] = UNSET,
    status: Union[Unset, OrderStatus] = UNSET,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        Any, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, GetOrderResponseV2Dto
    ]
]:
    """List Orders

     **Supported for:**

    `shopify` `square`

    Args:
        connection_uuid (str):
        offset (Union[Unset, float]):
        limit (Union[Unset, float]):
        order_by (Union[Unset, str]):
        id (Union[Unset, str]):
        fulfillment_status (Union[Unset, OrderFulfillmentStatus]):
        payment_status (Union[Unset, OrderPaymentStatus]):
        status (Union[Unset, OrderStatus]):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, GetOrderResponseV2Dto]]
    """

    kwargs = _get_kwargs(
        connection_uuid=connection_uuid,
        offset=offset,
        limit=limit,
        order_by=order_by,
        id=id,
        fulfillment_status=fulfillment_status,
        payment_status=payment_status,
        status=status,
        start_date=start_date,
        end_date=end_date,
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
    id: Union[Unset, str] = UNSET,
    fulfillment_status: Union[Unset, OrderFulfillmentStatus] = UNSET,
    payment_status: Union[Unset, OrderPaymentStatus] = UNSET,
    status: Union[Unset, OrderStatus] = UNSET,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        Any, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, GetOrderResponseV2Dto
    ]
]:
    """List Orders

     **Supported for:**

    `shopify` `square`

    Args:
        connection_uuid (str):
        offset (Union[Unset, float]):
        limit (Union[Unset, float]):
        order_by (Union[Unset, str]):
        id (Union[Unset, str]):
        fulfillment_status (Union[Unset, OrderFulfillmentStatus]):
        payment_status (Union[Unset, OrderPaymentStatus]):
        status (Union[Unset, OrderStatus]):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, GetOrderResponseV2Dto]
    """

    return sync_detailed(
        client=client,
        connection_uuid=connection_uuid,
        offset=offset,
        limit=limit,
        order_by=order_by,
        id=id,
        fulfillment_status=fulfillment_status,
        payment_status=payment_status,
        status=status,
        start_date=start_date,
        end_date=end_date,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    connection_uuid: str,
    offset: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    id: Union[Unset, str] = UNSET,
    fulfillment_status: Union[Unset, OrderFulfillmentStatus] = UNSET,
    payment_status: Union[Unset, OrderPaymentStatus] = UNSET,
    status: Union[Unset, OrderStatus] = UNSET,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        Any, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, GetOrderResponseV2Dto
    ]
]:
    """List Orders

     **Supported for:**

    `shopify` `square`

    Args:
        connection_uuid (str):
        offset (Union[Unset, float]):
        limit (Union[Unset, float]):
        order_by (Union[Unset, str]):
        id (Union[Unset, str]):
        fulfillment_status (Union[Unset, OrderFulfillmentStatus]):
        payment_status (Union[Unset, OrderPaymentStatus]):
        status (Union[Unset, OrderStatus]):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, GetOrderResponseV2Dto]]
    """

    kwargs = _get_kwargs(
        connection_uuid=connection_uuid,
        offset=offset,
        limit=limit,
        order_by=order_by,
        id=id,
        fulfillment_status=fulfillment_status,
        payment_status=payment_status,
        status=status,
        start_date=start_date,
        end_date=end_date,
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
    id: Union[Unset, str] = UNSET,
    fulfillment_status: Union[Unset, OrderFulfillmentStatus] = UNSET,
    payment_status: Union[Unset, OrderPaymentStatus] = UNSET,
    status: Union[Unset, OrderStatus] = UNSET,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        Any, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, GetOrderResponseV2Dto
    ]
]:
    """List Orders

     **Supported for:**

    `shopify` `square`

    Args:
        connection_uuid (str):
        offset (Union[Unset, float]):
        limit (Union[Unset, float]):
        order_by (Union[Unset, str]):
        id (Union[Unset, str]):
        fulfillment_status (Union[Unset, OrderFulfillmentStatus]):
        payment_status (Union[Unset, OrderPaymentStatus]):
        status (Union[Unset, OrderStatus]):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, GetOrderResponseV2Dto]
    """

    return (
        await asyncio_detailed(
            client=client,
            connection_uuid=connection_uuid,
            offset=offset,
            limit=limit,
            order_by=order_by,
            id=id,
            fulfillment_status=fulfillment_status,
            payment_status=payment_status,
            status=status,
            start_date=start_date,
            end_date=end_date,
        )
    ).parsed
