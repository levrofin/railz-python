from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fire_webhook_connection_v2_dto_data_request_status import (
    FireWebhookConnectionV2DtoDataRequestStatus,
    check_fire_webhook_connection_v2_dto_data_request_status,
)
from ..models.fire_webhook_connection_v2_dto_event import (
    FireWebhookConnectionV2DtoEvent,
    check_fire_webhook_connection_v2_dto_event,
)
from ..models.fire_webhook_connection_v2_dto_payload_type import (
    FireWebhookConnectionV2DtoPayloadType,
    check_fire_webhook_connection_v2_dto_payload_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="FireWebhookConnectionV2Dto")


@_attrs_define
class FireWebhookConnectionV2Dto:
    """
    Attributes:
        connection_uuid (str):  Example: CON-004f4cbe-e9ba-46c0-a7ef-2da661fe0e15.
        event (FireWebhookConnectionV2DtoEvent):
        request_type (Union[Unset, str]): Request types for data per type. Required when dataPerType event is present.
            Example: ACCOUNTING_TRANSACTION,ACCOUNTS,AGED_PAYABLE,AGED_RECEIVABLE,ATTACHMENT,BALANCE_SHEETS,BANKING_RECONCIL
            IATION,BANK_TRANSACTION_ACCOUNTING,BANK_ACCOUNT_ACCOUNTING,BANK_TRANSFERS,BILL_CREDIT_NOTES,BILL_PAYMENTS,BILLS,
            BUSINESS_INFO,BUSINESS_VALUATION,CASH_FLOW_STATEMENTS,CREDIT_SCORE,CUSTOMERS,DEPOSITS,ESTIMATES,FINANCIAL_BENCHM
            ARKING,FINANCIAL_FORECAST,FINANCIAL_RATIO,FRAUD_RISK_METRICS,INCOME_STATEMENTS,INVENTORY,INVOICE_CREDIT_NOTES,IN
            VOICE_PAYMENTS,INVOICES,JOURNAL_ENTRIES,JOURNAL,PROBABILITY_OF_DEFAULT,PURCHASE_ORDERS,REFUNDS,TAX_BENCHMARKING,
            TAX_RATES,TRACKING_CATEGORIES,TRIAL_BALANCES,VENDORS,PAYMENT_METHODS,PORTFOLIO_METRICS,EXPENSES,CONTACT,VENDOR_B
            ANK_ACCOUNT,CUSTOMER_BANK_ACCOUNT,BILL_PAYMENT_REQUEST,COMMERCE_TRANSACTION,COMMERCE_PRODUCT,COMMERCE_ORDER,COMM
            ERCE_DISPUTE,BANK_ACCOUNT,BANK_TRANSACTION,BANK_ASSET.
        push_communication_id (Union[Unset, str]):
        batch_id (Union[Unset, str]):
        delete_communication_id (Union[Unset, str]):
        customer_request_type (Union[Unset, str]):  Example: customersDataRequest.
        data_request_status (Union[Unset, FireWebhookConnectionV2DtoDataRequestStatus]): status to be returned for
            requests of data webhook Example: success.
        payload_type (Union[Unset, FireWebhookConnectionV2DtoPayloadType]): Webhook payload type.
    """

    connection_uuid: str
    event: FireWebhookConnectionV2DtoEvent
    request_type: Union[Unset, str] = UNSET
    push_communication_id: Union[Unset, str] = UNSET
    batch_id: Union[Unset, str] = UNSET
    delete_communication_id: Union[Unset, str] = UNSET
    customer_request_type: Union[Unset, str] = UNSET
    data_request_status: Union[Unset, FireWebhookConnectionV2DtoDataRequestStatus] = UNSET
    payload_type: Union[Unset, FireWebhookConnectionV2DtoPayloadType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_uuid = self.connection_uuid

        event: str = self.event

        request_type = self.request_type

        push_communication_id = self.push_communication_id

        batch_id = self.batch_id

        delete_communication_id = self.delete_communication_id

        customer_request_type = self.customer_request_type

        data_request_status: Union[Unset, str] = UNSET
        if not isinstance(self.data_request_status, Unset):
            data_request_status = self.data_request_status

        payload_type: Union[Unset, str] = UNSET
        if not isinstance(self.payload_type, Unset):
            payload_type = self.payload_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectionUuid": connection_uuid,
                "event": event,
            }
        )
        if request_type is not UNSET:
            field_dict["requestType"] = request_type
        if push_communication_id is not UNSET:
            field_dict["pushCommunicationId"] = push_communication_id
        if batch_id is not UNSET:
            field_dict["batchId"] = batch_id
        if delete_communication_id is not UNSET:
            field_dict["deleteCommunicationId"] = delete_communication_id
        if customer_request_type is not UNSET:
            field_dict["customerRequestType"] = customer_request_type
        if data_request_status is not UNSET:
            field_dict["dataRequestStatus"] = data_request_status
        if payload_type is not UNSET:
            field_dict["payloadType"] = payload_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connection_uuid = d.pop("connectionUuid")

        event = check_fire_webhook_connection_v2_dto_event(d.pop("event"))

        request_type = d.pop("requestType", UNSET)

        push_communication_id = d.pop("pushCommunicationId", UNSET)

        batch_id = d.pop("batchId", UNSET)

        delete_communication_id = d.pop("deleteCommunicationId", UNSET)

        customer_request_type = d.pop("customerRequestType", UNSET)

        _data_request_status = d.pop("dataRequestStatus", UNSET)
        data_request_status: Union[Unset, FireWebhookConnectionV2DtoDataRequestStatus]
        if isinstance(_data_request_status, Unset):
            data_request_status = UNSET
        else:
            data_request_status = check_fire_webhook_connection_v2_dto_data_request_status(_data_request_status)

        _payload_type = d.pop("payloadType", UNSET)
        payload_type: Union[Unset, FireWebhookConnectionV2DtoPayloadType]
        if isinstance(_payload_type, Unset):
            payload_type = UNSET
        else:
            payload_type = check_fire_webhook_connection_v2_dto_payload_type(_payload_type)

        fire_webhook_connection_v2_dto = cls(
            connection_uuid=connection_uuid,
            event=event,
            request_type=request_type,
            push_communication_id=push_communication_id,
            batch_id=batch_id,
            delete_communication_id=delete_communication_id,
            customer_request_type=customer_request_type,
            data_request_status=data_request_status,
            payload_type=payload_type,
        )

        fire_webhook_connection_v2_dto.additional_properties = d
        return fire_webhook_connection_v2_dto

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
