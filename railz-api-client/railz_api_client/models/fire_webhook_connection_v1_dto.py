from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fire_webhook_connection_v1_dto_event import (
    FireWebhookConnectionV1DtoEvent,
    check_fire_webhook_connection_v1_dto_event,
)
from ..models.fire_webhook_connection_v1_dto_service_name import (
    FireWebhookConnectionV1DtoServiceName,
    check_fire_webhook_connection_v1_dto_service_name,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="FireWebhookConnectionV1Dto")


@_attrs_define
class FireWebhookConnectionV1Dto:
    """
    Attributes:
        event (FireWebhookConnectionV1DtoEvent):
        business_name (Union[Unset, str]):  Example: Railz.
        service_name (Union[Unset, FireWebhookConnectionV1DtoServiceName]):  Example: quickbooks.
        connection_id (Union[Unset, str]):  Example: CON-004f4cbe-e9ba-46c0-a7ef-2da661fe0e15.
        request_type (Union[Unset, str]): Request types for data per type. Required when dataPerType event is present.
            Example: ACCOUNTING_TRANSACTION,ACCOUNTS,AGED_PAYABLE,AGED_RECEIVABLE,ATTACHMENT,BALANCE_SHEETS,BANKING_RECONCIL
            IATION,BANK_TRANSACTION_ACCOUNTING,BANK_ACCOUNT_ACCOUNTING,BANK_TRANSFERS,BILL_CREDIT_NOTES,BILL_PAYMENTS,BILLS,
            BUSINESS_INFO,BUSINESS_VALUATION,CASH_FLOW_STATEMENTS,CREDIT_SCORE,CUSTOMERS,DEPOSITS,ESTIMATES,FINANCIAL_BENCHM
            ARKING,FINANCIAL_FORECAST,FINANCIAL_RATIO,FRAUD_RISK_METRICS,INCOME_STATEMENTS,INVENTORY,INVOICE_CREDIT_NOTES,IN
            VOICE_PAYMENTS,INVOICES,JOURNAL_ENTRIES,JOURNAL,PROBABILITY_OF_DEFAULT,PURCHASE_ORDERS,REFUNDS,TAX_BENCHMARKING,
            TAX_RATES,TAX_AUTHORITY,TRACKING_CATEGORIES,TRIAL_BALANCES,VENDORS,PAYMENT_METHODS,PORTFOLIO_METRICS,EXPENSES,CO
            NTACT,VENDOR_BANK_ACCOUNT,CUSTOMER_BANK_ACCOUNT,BILL_PAYMENT_REQUEST,COMMERCE_TRANSACTION,COMMERCE_PRODUCT,COMME
            RCE_ORDER,COMMERCE_DISPUTE,BANK_ACCOUNT,BANK_TRANSACTION,BANK_ASSET.
        push_communication_id (Union[Unset, str]):
        batch_id (Union[Unset, str]):
        delete_communication_id (Union[Unset, str]):
        customer_request_type (Union[Unset, str]):  Example: customersDataRequest.
    """

    event: FireWebhookConnectionV1DtoEvent
    business_name: Union[Unset, str] = UNSET
    service_name: Union[Unset, FireWebhookConnectionV1DtoServiceName] = UNSET
    connection_id: Union[Unset, str] = UNSET
    request_type: Union[Unset, str] = UNSET
    push_communication_id: Union[Unset, str] = UNSET
    batch_id: Union[Unset, str] = UNSET
    delete_communication_id: Union[Unset, str] = UNSET
    customer_request_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event: str = self.event

        business_name = self.business_name

        service_name: Union[Unset, str] = UNSET
        if not isinstance(self.service_name, Unset):
            service_name = self.service_name

        connection_id = self.connection_id

        request_type = self.request_type

        push_communication_id = self.push_communication_id

        batch_id = self.batch_id

        delete_communication_id = self.delete_communication_id

        customer_request_type = self.customer_request_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event": event,
            }
        )
        if business_name is not UNSET:
            field_dict["businessName"] = business_name
        if service_name is not UNSET:
            field_dict["serviceName"] = service_name
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        event = check_fire_webhook_connection_v1_dto_event(d.pop("event"))

        business_name = d.pop("businessName", UNSET)

        _service_name = d.pop("serviceName", UNSET)
        service_name: Union[Unset, FireWebhookConnectionV1DtoServiceName]
        if isinstance(_service_name, Unset):
            service_name = UNSET
        else:
            service_name = check_fire_webhook_connection_v1_dto_service_name(_service_name)

        connection_id = d.pop("connectionId", UNSET)

        request_type = d.pop("requestType", UNSET)

        push_communication_id = d.pop("pushCommunicationId", UNSET)

        batch_id = d.pop("batchId", UNSET)

        delete_communication_id = d.pop("deleteCommunicationId", UNSET)

        customer_request_type = d.pop("customerRequestType", UNSET)

        fire_webhook_connection_v1_dto = cls(
            event=event,
            business_name=business_name,
            service_name=service_name,
            connection_id=connection_id,
            request_type=request_type,
            push_communication_id=push_communication_id,
            batch_id=batch_id,
            delete_communication_id=delete_communication_id,
            customer_request_type=customer_request_type,
        )

        fire_webhook_connection_v1_dto.additional_properties = d
        return fire_webhook_connection_v1_dto

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
