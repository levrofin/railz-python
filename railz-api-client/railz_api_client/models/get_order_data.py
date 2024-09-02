import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_order_data_fulfillment_status import GetOrderDataFulfillmentStatus
from ..models.get_order_data_payment_status import GetOrderDataPaymentStatus
from ..models.get_order_data_status import GetOrderDataStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.billing_address import BillingAddress
    from ..models.commerce_currency_ref import CommerceCurrencyRef
    from ..models.fulfillment_refs import FulfillmentRefs
    from ..models.lines import Lines
    from ..models.order_customer_ref import OrderCustomerRef
    from ..models.order_transaction_source_refs import OrderTransactionSourceRefs
    from ..models.refund_refs import RefundRefs
    from ..models.shipping_address import ShippingAddress


T = TypeVar("T", bound="GetOrderData")


@_attrs_define
class GetOrderData:
    """
    Attributes:
        id (str):  Example: 450789469.
        total_tax_amount (float):  Example: 11.94.
        total_amount (float):  Example: 598.94.
        created_date (datetime.datetime):  Example: 2022-03-11T11:29:03-05:00.
        source_modified_date (datetime.datetime):  Example: 2022-03-11T11:29:03-05:00.
        status (GetOrderDataStatus):
        payment_status (GetOrderDataPaymentStatus):
        fulfillment_status (GetOrderDataFulfillmentStatus):
        order_number (Union[Unset, str]):  Example: 1001.
        fulfillment_refs (Union[Unset, List['FulfillmentRefs']]):
        lines (Union[Unset, List['Lines']]):
        refund_refs (Union[Unset, List['RefundRefs']]):
        transaction_source_refs (Union[Unset, List['OrderTransactionSourceRefs']]):
        shipping_address (Union[Unset, ShippingAddress]):
        billing_address (Union[Unset, BillingAddress]):
        customer_ref (Union[Unset, OrderCustomerRef]):
        currency_ref (Union[Unset, CommerceCurrencyRef]):
        total_shipping_amount (Union[Unset, float]):  Example: 30.
        total_gratuity_amount (Union[Unset, float]):  Example: 4.87.
        total_discount_amount (Union[Unset, float]):
    """

    id: str
    total_tax_amount: float
    total_amount: float
    created_date: datetime.datetime
    source_modified_date: datetime.datetime
    status: GetOrderDataStatus
    payment_status: GetOrderDataPaymentStatus
    fulfillment_status: GetOrderDataFulfillmentStatus
    order_number: Union[Unset, str] = UNSET
    fulfillment_refs: Union[Unset, List["FulfillmentRefs"]] = UNSET
    lines: Union[Unset, List["Lines"]] = UNSET
    refund_refs: Union[Unset, List["RefundRefs"]] = UNSET
    transaction_source_refs: Union[Unset, List["OrderTransactionSourceRefs"]] = UNSET
    shipping_address: Union[Unset, "ShippingAddress"] = UNSET
    billing_address: Union[Unset, "BillingAddress"] = UNSET
    customer_ref: Union[Unset, "OrderCustomerRef"] = UNSET
    currency_ref: Union[Unset, "CommerceCurrencyRef"] = UNSET
    total_shipping_amount: Union[Unset, float] = UNSET
    total_gratuity_amount: Union[Unset, float] = UNSET
    total_discount_amount: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        total_tax_amount = self.total_tax_amount

        total_amount = self.total_amount

        created_date = self.created_date.isoformat()

        source_modified_date = self.source_modified_date.isoformat()

        status = self.status

        payment_status = self.payment_status

        fulfillment_status = self.fulfillment_status

        order_number = self.order_number

        fulfillment_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fulfillment_refs, Unset):
            fulfillment_refs = []
            for fulfillment_refs_item_data in self.fulfillment_refs:
                fulfillment_refs_item = fulfillment_refs_item_data.to_dict()
                fulfillment_refs.append(fulfillment_refs_item)

        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        refund_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.refund_refs, Unset):
            refund_refs = []
            for refund_refs_item_data in self.refund_refs:
                refund_refs_item = refund_refs_item_data.to_dict()
                refund_refs.append(refund_refs_item)

        transaction_source_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.transaction_source_refs, Unset):
            transaction_source_refs = []
            for transaction_source_refs_item_data in self.transaction_source_refs:
                transaction_source_refs_item = transaction_source_refs_item_data.to_dict()
                transaction_source_refs.append(transaction_source_refs_item)

        shipping_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_address, Unset):
            shipping_address = self.shipping_address.to_dict()

        billing_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.billing_address, Unset):
            billing_address = self.billing_address.to_dict()

        customer_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_ref, Unset):
            customer_ref = self.customer_ref.to_dict()

        currency_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.currency_ref, Unset):
            currency_ref = self.currency_ref.to_dict()

        total_shipping_amount = self.total_shipping_amount

        total_gratuity_amount = self.total_gratuity_amount

        total_discount_amount = self.total_discount_amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "totalTaxAmount": total_tax_amount,
                "totalAmount": total_amount,
                "createdDate": created_date,
                "sourceModifiedDate": source_modified_date,
                "status": status,
                "paymentStatus": payment_status,
                "fulfillmentStatus": fulfillment_status,
            }
        )
        if order_number is not UNSET:
            field_dict["orderNumber"] = order_number
        if fulfillment_refs is not UNSET:
            field_dict["fulfillmentRefs"] = fulfillment_refs
        if lines is not UNSET:
            field_dict["lines"] = lines
        if refund_refs is not UNSET:
            field_dict["refundRefs"] = refund_refs
        if transaction_source_refs is not UNSET:
            field_dict["transactionSourceRefs"] = transaction_source_refs
        if shipping_address is not UNSET:
            field_dict["shippingAddress"] = shipping_address
        if billing_address is not UNSET:
            field_dict["billingAddress"] = billing_address
        if customer_ref is not UNSET:
            field_dict["customerRef"] = customer_ref
        if currency_ref is not UNSET:
            field_dict["currencyRef"] = currency_ref
        if total_shipping_amount is not UNSET:
            field_dict["totalShippingAmount"] = total_shipping_amount
        if total_gratuity_amount is not UNSET:
            field_dict["totalGratuityAmount"] = total_gratuity_amount
        if total_discount_amount is not UNSET:
            field_dict["totalDiscountAmount"] = total_discount_amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.billing_address import BillingAddress
        from ..models.commerce_currency_ref import CommerceCurrencyRef
        from ..models.fulfillment_refs import FulfillmentRefs
        from ..models.lines import Lines
        from ..models.order_customer_ref import OrderCustomerRef
        from ..models.order_transaction_source_refs import OrderTransactionSourceRefs
        from ..models.refund_refs import RefundRefs
        from ..models.shipping_address import ShippingAddress

        d = src_dict.copy()
        id = d.pop("id")

        total_tax_amount = d.pop("totalTaxAmount")

        total_amount = d.pop("totalAmount")

        created_date = isoparse(d.pop("createdDate"))

        source_modified_date = isoparse(d.pop("sourceModifiedDate"))

        status = d.pop("status")

        payment_status = d.pop("paymentStatus")

        fulfillment_status = d.pop("fulfillmentStatus")

        order_number = d.pop("orderNumber", UNSET)

        fulfillment_refs = []
        _fulfillment_refs = d.pop("fulfillmentRefs", UNSET)
        for fulfillment_refs_item_data in _fulfillment_refs or []:
            fulfillment_refs_item = FulfillmentRefs.from_dict(fulfillment_refs_item_data)

            fulfillment_refs.append(fulfillment_refs_item)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = Lines.from_dict(lines_item_data)

            lines.append(lines_item)

        refund_refs = []
        _refund_refs = d.pop("refundRefs", UNSET)
        for refund_refs_item_data in _refund_refs or []:
            refund_refs_item = RefundRefs.from_dict(refund_refs_item_data)

            refund_refs.append(refund_refs_item)

        transaction_source_refs = []
        _transaction_source_refs = d.pop("transactionSourceRefs", UNSET)
        for transaction_source_refs_item_data in _transaction_source_refs or []:
            transaction_source_refs_item = OrderTransactionSourceRefs.from_dict(transaction_source_refs_item_data)

            transaction_source_refs.append(transaction_source_refs_item)

        _shipping_address = d.pop("shippingAddress", UNSET)
        shipping_address: Union[Unset, ShippingAddress]
        if isinstance(_shipping_address, Unset):
            shipping_address = UNSET
        else:
            shipping_address = ShippingAddress.from_dict(_shipping_address)

        _billing_address = d.pop("billingAddress", UNSET)
        billing_address: Union[Unset, BillingAddress]
        if isinstance(_billing_address, Unset):
            billing_address = UNSET
        else:
            billing_address = BillingAddress.from_dict(_billing_address)

        _customer_ref = d.pop("customerRef", UNSET)
        customer_ref: Union[Unset, OrderCustomerRef]
        if isinstance(_customer_ref, Unset):
            customer_ref = UNSET
        else:
            customer_ref = OrderCustomerRef.from_dict(_customer_ref)

        _currency_ref = d.pop("currencyRef", UNSET)
        currency_ref: Union[Unset, CommerceCurrencyRef]
        if isinstance(_currency_ref, Unset):
            currency_ref = UNSET
        else:
            currency_ref = CommerceCurrencyRef.from_dict(_currency_ref)

        total_shipping_amount = d.pop("totalShippingAmount", UNSET)

        total_gratuity_amount = d.pop("totalGratuityAmount", UNSET)

        total_discount_amount = d.pop("totalDiscountAmount", UNSET)

        get_order_data = cls(
            id=id,
            total_tax_amount=total_tax_amount,
            total_amount=total_amount,
            created_date=created_date,
            source_modified_date=source_modified_date,
            status=status,
            payment_status=payment_status,
            fulfillment_status=fulfillment_status,
            order_number=order_number,
            fulfillment_refs=fulfillment_refs,
            lines=lines,
            refund_refs=refund_refs,
            transaction_source_refs=transaction_source_refs,
            shipping_address=shipping_address,
            billing_address=billing_address,
            customer_ref=customer_ref,
            currency_ref=currency_ref,
            total_shipping_amount=total_shipping_amount,
            total_gratuity_amount=total_gratuity_amount,
            total_discount_amount=total_discount_amount,
        )

        get_order_data.additional_properties = d
        return get_order_data

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
