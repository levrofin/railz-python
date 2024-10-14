from http import HTTPStatus
from typing import Any, Dict, Mapping, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_status_response_v2_dto import DataStatusResponseV2Dto
from ...models.error_400_response_dto_v2 import Error400ResponseDtoV2
from ...models.error_401_response_dto import Error401ResponseDto
from ...models.error_403_response_dto import Error403ResponseDto
from ...models.error_500_response_dto import Error500ResponseDto
from ...models.sync_status_accounting_method import SyncStatusAccountingMethod
from ...models.sync_status_data_type import SyncStatusDataType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    connection_uuid: str,
    offset: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = UNSET,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    data_type: Union[Unset, SyncStatusDataType] = UNSET,
    report_frequency: Union[Unset, str] = UNSET,
    current_status: Union[Unset, str] = UNSET,
    accounting_method: Union[Unset, SyncStatusAccountingMethod] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    request_id: Union[Unset, str] = UNSET,
    additional_query_params: Mapping[str, str | list[str]] | None = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    if additional_query_params:
        params.update(additional_query_params)

    params["connectionUuid"] = connection_uuid

    params["offset"] = offset

    params["limit"] = limit

    params["startDate"] = start_date

    params["endDate"] = end_date

    json_data_type: Union[Unset, str] = UNSET
    if not isinstance(data_type, Unset):
        json_data_type = data_type

    params["dataType"] = json_data_type

    params["reportFrequency"] = report_frequency

    params["currentStatus"] = current_status

    json_accounting_method: Union[Unset, str] = UNSET
    if not isinstance(accounting_method, Unset):
        json_accounting_method = accounting_method

    params["accountingMethod"] = json_accounting_method

    params["orderBy"] = order_by

    params["requestId"] = request_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v2/data/syncStatus",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[DataStatusResponseV2Dto, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DataStatusResponseV2Dto.from_dict(response.json())

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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response, skip_parsing: bool = False
) -> Response[
    Union[DataStatusResponseV2Dto, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=None if skip_parsing else _parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    connection_uuid: str,
    offset: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = UNSET,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    data_type: Union[Unset, SyncStatusDataType] = UNSET,
    report_frequency: Union[Unset, str] = UNSET,
    current_status: Union[Unset, str] = UNSET,
    accounting_method: Union[Unset, SyncStatusAccountingMethod] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    request_id: Union[Unset, str] = UNSET,
    additional_query_params: Mapping[str, str | list[str]] | None = None,
    skip_parsing: bool = False,
) -> Response[
    Union[DataStatusResponseV2Dto, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto]
]:
    """Fetch Status of Data Syncs

     **Supported for:**

    `freshbooks` `quickbooks` `xero` `oracleNetsuite` `sageBusinessCloud` `sageIntacct`
    `dynamicsBusinessCentral` `wave` `shopify` `square` `plaid` `zohoBooks`

    Args:
        connection_uuid (str):
        offset (Union[Unset, float]):
        limit (Union[Unset, float]):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        data_type (Union[Unset, SyncStatusDataType]):
        report_frequency (Union[Unset, str]):
        current_status (Union[Unset, str]):
        accounting_method (Union[Unset, SyncStatusAccountingMethod]):
        order_by (Union[Unset, str]):
        request_id (Union[Unset, str]):
        additional_query_params: extra query params

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataStatusResponseV2Dto, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto]]
    """

    kwargs = _get_kwargs(
        connection_uuid=connection_uuid,
        offset=offset,
        limit=limit,
        start_date=start_date,
        end_date=end_date,
        data_type=data_type,
        report_frequency=report_frequency,
        current_status=current_status,
        accounting_method=accounting_method,
        order_by=order_by,
        request_id=request_id,
        additional_query_params=additional_query_params,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response, skip_parsing=skip_parsing)


def sync(
    *,
    client: AuthenticatedClient,
    connection_uuid: str,
    offset: Union[Unset, float] = UNSET,
    limit: Union[Unset, float] = UNSET,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    data_type: Union[Unset, SyncStatusDataType] = UNSET,
    report_frequency: Union[Unset, str] = UNSET,
    current_status: Union[Unset, str] = UNSET,
    accounting_method: Union[Unset, SyncStatusAccountingMethod] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    request_id: Union[Unset, str] = UNSET,
    additional_query_params: Mapping[str, str | list[str]] | None = None,
    skip_parsing: bool = False,
) -> Optional[
    Union[DataStatusResponseV2Dto, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto]
]:
    """Fetch Status of Data Syncs

     **Supported for:**

    `freshbooks` `quickbooks` `xero` `oracleNetsuite` `sageBusinessCloud` `sageIntacct`
    `dynamicsBusinessCentral` `wave` `shopify` `square` `plaid` `zohoBooks`

    Args:
        connection_uuid (str):
        offset (Union[Unset, float]):
        limit (Union[Unset, float]):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        data_type (Union[Unset, SyncStatusDataType]):
        report_frequency (Union[Unset, str]):
        current_status (Union[Unset, str]):
        accounting_method (Union[Unset, SyncStatusAccountingMethod]):
        order_by (Union[Unset, str]):
        request_id (Union[Unset, str]):
        additional_query_params: extra query params

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DataStatusResponseV2Dto, Error400ResponseDtoV2, Error401ResponseDto, Error403ResponseDto, Error500ResponseDto]
    """

    return sync_detailed(
        client=client,
        connection_uuid=connection_uuid,
        offset=offset,
        limit=limit,
        start_date=start_date,
        end_date=end_date,
        data_type=data_type,
        report_frequency=report_frequency,
        current_status=current_status,
        accounting_method=accounting_method,
        order_by=order_by,
        request_id=request_id,
        additional_query_params=additional_query_params,
        skip_parsing=skip_parsing,
    ).parsed
