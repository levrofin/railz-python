from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400_response_dto_v2 import Error400ResponseDtoV2
from ...models.error_401_response_dto import Error401ResponseDto
from ...models.error_403_response_dto import Error403ResponseDto
from ...models.error_500_response_dto import Error500ResponseDto
from ...models.push_journal_entries_v2_dto import PushJournalEntriesV2Dto
from ...models.push_journal_entries_v2_response_dto import PushJournalEntriesV2ResponseDto
from ...types import Response


def _get_kwargs(
    *,
    body: PushJournalEntriesV2Dto,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v2/accounting/journalEntries",
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
        PushJournalEntriesV2ResponseDto,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PushJournalEntriesV2ResponseDto.from_dict(response.json())

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
        PushJournalEntriesV2ResponseDto,
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
    body: PushJournalEntriesV2Dto,
) -> Response[
    Union[
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        PushJournalEntriesV2ResponseDto,
    ]
]:
    """Create a Journal Entry

     **Supported for:**

    `quickbooks` `xero` `freshbooks` `sageIntacct` `sageBusinessCloud` `oracleNetsuite`
    `dynamicsBusinessCentral` `zohoBooks`

    Args:
        body (PushJournalEntriesV2Dto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, PushJournalEntriesV2ResponseDto]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PushJournalEntriesV2Dto,
) -> Optional[
    Union[
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        PushJournalEntriesV2ResponseDto,
    ]
]:
    """Create a Journal Entry

     **Supported for:**

    `quickbooks` `xero` `freshbooks` `sageIntacct` `sageBusinessCloud` `oracleNetsuite`
    `dynamicsBusinessCentral` `zohoBooks`

    Args:
        body (PushJournalEntriesV2Dto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, PushJournalEntriesV2ResponseDto]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PushJournalEntriesV2Dto,
) -> Response[
    Union[
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        PushJournalEntriesV2ResponseDto,
    ]
]:
    """Create a Journal Entry

     **Supported for:**

    `quickbooks` `xero` `freshbooks` `sageIntacct` `sageBusinessCloud` `oracleNetsuite`
    `dynamicsBusinessCentral` `zohoBooks`

    Args:
        body (PushJournalEntriesV2Dto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, PushJournalEntriesV2ResponseDto]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PushJournalEntriesV2Dto,
) -> Optional[
    Union[
        Error400ResponseDtoV2,
        Error401ResponseDto,
        Error403ResponseDto,
        Error500ResponseDto,
        PushJournalEntriesV2ResponseDto,
    ]
]:
    """Create a Journal Entry

     **Supported for:**

    `quickbooks` `xero` `freshbooks` `sageIntacct` `sageBusinessCloud` `oracleNetsuite`
    `dynamicsBusinessCentral` `zohoBooks`

    Args:
        body (PushJournalEntriesV2Dto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto, PushJournalEntriesV2ResponseDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
