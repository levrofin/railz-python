from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_types_data_type import DataTypesDataType
from ...models.data_types_response_v2_dto import DataTypesResponseV2Dto
from ...models.data_types_service_name import DataTypesServiceName
from ...models.error_400_response_dto_v2 import Error400ResponseDtoV2
from ...models.error_500_response_dto import Error500ResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    service_type: Union[Unset, str] = UNSET,
    service_name: Union[Unset, DataTypesServiceName] = UNSET,
    is_beta: Union[Unset, bool] = UNSET,
    data_type: Union[Unset, DataTypesDataType] = UNSET,
    is_more_readable: Union[Unset, bool] = UNSET,
    additional_query_params: dict[str, str | list[str]] | None = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    if additional_query_params:
        params.update(additional_query_params)

    params["serviceType"] = service_type

    json_service_name: Union[Unset, str] = UNSET
    if not isinstance(service_name, Unset):
        json_service_name = service_name

    params["serviceName"] = json_service_name

    params["isBeta"] = is_beta

    json_data_type: Union[Unset, str] = UNSET
    if not isinstance(data_type, Unset):
        json_data_type = data_type

    params["dataType"] = json_data_type

    params["isMoreReadable"] = is_more_readable

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v2/data/dataTypes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error400ResponseDtoV2, Error500ResponseDto, List["DataTypesResponseV2Dto"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DataTypesResponseV2Dto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Error400ResponseDtoV2.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Error500ResponseDto.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error400ResponseDtoV2, Error500ResponseDto, List["DataTypesResponseV2Dto"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    service_type: Union[Unset, str] = UNSET,
    service_name: Union[Unset, DataTypesServiceName] = UNSET,
    is_beta: Union[Unset, bool] = UNSET,
    data_type: Union[Unset, DataTypesDataType] = UNSET,
    is_more_readable: Union[Unset, bool] = UNSET,
    additional_query_params: dict[str, str | list[str]] | None = None,
) -> Response[Union[Error400ResponseDtoV2, Error500ResponseDto, List["DataTypesResponseV2Dto"]]]:
    """List Supported Data Types

     **Supported for:**

    `freshbooks` `quickbooks` `quickbooksDesktop` `xero` `oracleNetsuite` `sageBusinessCloud`
    `sageIntacct` `dynamicsBusinessCentral` `wave` `shopify` `square` `plaid` `zohoBooks`

    Args:
        service_type (Union[Unset, str]):
        service_name (Union[Unset, DataTypesServiceName]):
        is_beta (Union[Unset, bool]):
        data_type (Union[Unset, DataTypesDataType]):
        is_more_readable (Union[Unset, bool]):
        additional_query_params: extra query params

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400ResponseDtoV2, Error500ResponseDto, List['DataTypesResponseV2Dto']]]
    """

    kwargs = _get_kwargs(
        service_type=service_type,
        service_name=service_name,
        is_beta=is_beta,
        data_type=data_type,
        is_more_readable=is_more_readable,
        additional_query_params=additional_query_params,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    service_type: Union[Unset, str] = UNSET,
    service_name: Union[Unset, DataTypesServiceName] = UNSET,
    is_beta: Union[Unset, bool] = UNSET,
    data_type: Union[Unset, DataTypesDataType] = UNSET,
    is_more_readable: Union[Unset, bool] = UNSET,
    additional_query_params: dict[str, str | list[str]] | None = None,
) -> Optional[Union[Error400ResponseDtoV2, Error500ResponseDto, List["DataTypesResponseV2Dto"]]]:
    """List Supported Data Types

     **Supported for:**

    `freshbooks` `quickbooks` `quickbooksDesktop` `xero` `oracleNetsuite` `sageBusinessCloud`
    `sageIntacct` `dynamicsBusinessCentral` `wave` `shopify` `square` `plaid` `zohoBooks`

    Args:
        service_type (Union[Unset, str]):
        service_name (Union[Unset, DataTypesServiceName]):
        is_beta (Union[Unset, bool]):
        data_type (Union[Unset, DataTypesDataType]):
        is_more_readable (Union[Unset, bool]):
        additional_query_params: extra query params

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400ResponseDtoV2, Error500ResponseDto, List['DataTypesResponseV2Dto']]
    """

    return sync_detailed(
        client=client,
        service_type=service_type,
        service_name=service_name,
        is_beta=is_beta,
        data_type=data_type,
        is_more_readable=is_more_readable,
        additional_query_params=additional_query_params,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    service_type: Union[Unset, str] = UNSET,
    service_name: Union[Unset, DataTypesServiceName] = UNSET,
    is_beta: Union[Unset, bool] = UNSET,
    data_type: Union[Unset, DataTypesDataType] = UNSET,
    is_more_readable: Union[Unset, bool] = UNSET,
    additional_query_params: dict[str, str | list[str]] | None = None,
) -> Response[Union[Error400ResponseDtoV2, Error500ResponseDto, List["DataTypesResponseV2Dto"]]]:
    """List Supported Data Types

     **Supported for:**

    `freshbooks` `quickbooks` `quickbooksDesktop` `xero` `oracleNetsuite` `sageBusinessCloud`
    `sageIntacct` `dynamicsBusinessCentral` `wave` `shopify` `square` `plaid` `zohoBooks`

    Args:
        service_type (Union[Unset, str]):
        service_name (Union[Unset, DataTypesServiceName]):
        is_beta (Union[Unset, bool]):
        data_type (Union[Unset, DataTypesDataType]):
        is_more_readable (Union[Unset, bool]):
        additional_query_params: extra query params

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400ResponseDtoV2, Error500ResponseDto, List['DataTypesResponseV2Dto']]]
    """

    kwargs = _get_kwargs(
        service_type=service_type,
        service_name=service_name,
        is_beta=is_beta,
        data_type=data_type,
        is_more_readable=is_more_readable,
        additional_query_params=additional_query_params,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    service_type: Union[Unset, str] = UNSET,
    service_name: Union[Unset, DataTypesServiceName] = UNSET,
    is_beta: Union[Unset, bool] = UNSET,
    data_type: Union[Unset, DataTypesDataType] = UNSET,
    is_more_readable: Union[Unset, bool] = UNSET,
    additional_query_params: dict[str, str | list[str]] | None = None,
) -> Optional[Union[Error400ResponseDtoV2, Error500ResponseDto, List["DataTypesResponseV2Dto"]]]:
    """List Supported Data Types

     **Supported for:**

    `freshbooks` `quickbooks` `quickbooksDesktop` `xero` `oracleNetsuite` `sageBusinessCloud`
    `sageIntacct` `dynamicsBusinessCentral` `wave` `shopify` `square` `plaid` `zohoBooks`

    Args:
        service_type (Union[Unset, str]):
        service_name (Union[Unset, DataTypesServiceName]):
        is_beta (Union[Unset, bool]):
        data_type (Union[Unset, DataTypesDataType]):
        is_more_readable (Union[Unset, bool]):
        additional_query_params: extra query params

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400ResponseDtoV2, Error500ResponseDto, List['DataTypesResponseV2Dto']]
    """

    return (
        await asyncio_detailed(
            client=client,
            service_type=service_type,
            service_name=service_name,
            is_beta=is_beta,
            data_type=data_type,
            is_more_readable=is_more_readable,
            additional_query_params=additional_query_params,
        )
    ).parsed
