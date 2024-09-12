from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400_response_dto_v2 import Error400ResponseDtoV2
from ...models.error_401_response_dto import Error401ResponseDto
from ...models.error_403_response_dto import Error403ResponseDto
from ...models.error_500_response_dto import Error500ResponseDto
from ...models.update_bills_response_v2_dto import UpdateBillsResponseV2Dto
from ...models.update_bills_v2_dto import UpdateBillsV2Dto
from ...types import UNSET, Response


def _get_kwargs(
    id: str,
    *,
    body: UpdateBillsV2Dto,
    additional_query_params: dict[str, str | list[str]] | None = None,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    if additional_query_params:
        params.update(additional_query_params)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/v2/accounting/bills/{id}",
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
        Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, UpdateBillsResponseV2Dto
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UpdateBillsResponseV2Dto.from_dict(response.json())

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
        Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, UpdateBillsResponseV2Dto
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateBillsV2Dto,
    additional_query_params: dict[str, str | list[str]] | None = None,
) -> Response[
    Union[
        Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, UpdateBillsResponseV2Dto
    ]
]:
    """Update a Bill

     **Supported for:**

    `quickbooks` `xero` `sageIntacct` `sageBusinessCloud` `oracleNetsuite`

    Args:
        id (str):
        body (UpdateBillsV2Dto):
        additional_query_params: extra query params

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, UpdateBillsResponseV2Dto]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        additional_query_params=additional_query_params,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateBillsV2Dto,
    additional_query_params: dict[str, str | list[str]] | None = None,
) -> Optional[
    Union[
        Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, UpdateBillsResponseV2Dto
    ]
]:
    """Update a Bill

     **Supported for:**

    `quickbooks` `xero` `sageIntacct` `sageBusinessCloud` `oracleNetsuite`

    Args:
        id (str):
        body (UpdateBillsV2Dto):
        additional_query_params: extra query params

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, UpdateBillsResponseV2Dto]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        additional_query_params=additional_query_params,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateBillsV2Dto,
    additional_query_params: dict[str, str | list[str]] | None = None,
) -> Response[
    Union[
        Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, UpdateBillsResponseV2Dto
    ]
]:
    """Update a Bill

     **Supported for:**

    `quickbooks` `xero` `sageIntacct` `sageBusinessCloud` `oracleNetsuite`

    Args:
        id (str):
        body (UpdateBillsV2Dto):
        additional_query_params: extra query params

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, UpdateBillsResponseV2Dto]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        additional_query_params=additional_query_params,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateBillsV2Dto,
    additional_query_params: dict[str, str | list[str]] | None = None,
) -> Optional[
    Union[
        Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, UpdateBillsResponseV2Dto
    ]
]:
    """Update a Bill

     **Supported for:**

    `quickbooks` `xero` `sageIntacct` `sageBusinessCloud` `oracleNetsuite`

    Args:
        id (str):
        body (UpdateBillsV2Dto):
        additional_query_params: extra query params

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, UpdateBillsResponseV2Dto]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            additional_query_params=additional_query_params,
        )
    ).parsed
