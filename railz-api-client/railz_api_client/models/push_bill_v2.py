import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.purchase_order_ref_dto import PurchaseOrderRefDto
    from ..models.push_bill_line_item_v2 import PushBillLineItemV2
    from ..models.push_bill_v2_pass_through import PushBillV2PassThrough
    from ..models.subsidiary_ref_dto import SubsidiaryRefDto
    from ..models.vendor_ref_dto import VendorRefDto


T = TypeVar("T", bound="PushBillV2")


@_attrs_define
class PushBillV2:
    """
    Attributes:
        vendor_ref (VendorRefDto):
        lines (List['PushBillLineItemV2']):
        vendor_invoice_number (Union[Unset, str]):  Example: 254.
        posted_date (Union[Unset, datetime.date]):  Example: 2021-03-29.
        due_date (Union[Unset, datetime.date]):  Example: 2021-03-29.
        currency_rate (Union[Unset, float]):  Example: 1.13.
        memo (Union[Unset, str]):  Example: Example bill memo..
        currency (Union[Unset, str]):  Example: CAD.
        subsidiary_refs (Union[Unset, List['SubsidiaryRefDto']]):
        purchase_order_refs (Union[Unset, List['PurchaseOrderRefDto']]):
        pass_through (Union[Unset, PushBillV2PassThrough]):  Example: {'CustomField': [{'DefinitionId': '1',
            'StringValue': 'my custom value', 'Name': 'Field One'}]}.
    """

    vendor_ref: "VendorRefDto"
    lines: List["PushBillLineItemV2"]
    vendor_invoice_number: Union[Unset, str] = UNSET
    posted_date: Union[Unset, datetime.date] = UNSET
    due_date: Union[Unset, datetime.date] = UNSET
    currency_rate: Union[Unset, float] = UNSET
    memo: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    subsidiary_refs: Union[Unset, List["SubsidiaryRefDto"]] = UNSET
    purchase_order_refs: Union[Unset, List["PurchaseOrderRefDto"]] = UNSET
    pass_through: Union[Unset, "PushBillV2PassThrough"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        vendor_ref = self.vendor_ref.to_dict()

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        vendor_invoice_number = self.vendor_invoice_number

        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        currency_rate = self.currency_rate

        memo = self.memo

        currency = self.currency

        subsidiary_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subsidiary_refs, Unset):
            subsidiary_refs = []
            for subsidiary_refs_item_data in self.subsidiary_refs:
                subsidiary_refs_item = subsidiary_refs_item_data.to_dict()
                subsidiary_refs.append(subsidiary_refs_item)

        purchase_order_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.purchase_order_refs, Unset):
            purchase_order_refs = []
            for purchase_order_refs_item_data in self.purchase_order_refs:
                purchase_order_refs_item = purchase_order_refs_item_data.to_dict()
                purchase_order_refs.append(purchase_order_refs_item)

        pass_through: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pass_through, Unset):
            pass_through = self.pass_through.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vendorRef": vendor_ref,
                "lines": lines,
            }
        )
        if vendor_invoice_number is not UNSET:
            field_dict["vendorInvoiceNumber"] = vendor_invoice_number
        if posted_date is not UNSET:
            field_dict["postedDate"] = posted_date
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if memo is not UNSET:
            field_dict["memo"] = memo
        if currency is not UNSET:
            field_dict["currency"] = currency
        if subsidiary_refs is not UNSET:
            field_dict["subsidiaryRefs"] = subsidiary_refs
        if purchase_order_refs is not UNSET:
            field_dict["purchaseOrderRefs"] = purchase_order_refs
        if pass_through is not UNSET:
            field_dict["passThrough"] = pass_through

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.purchase_order_ref_dto import PurchaseOrderRefDto
        from ..models.push_bill_line_item_v2 import PushBillLineItemV2
        from ..models.push_bill_v2_pass_through import PushBillV2PassThrough
        from ..models.subsidiary_ref_dto import SubsidiaryRefDto
        from ..models.vendor_ref_dto import VendorRefDto

        d = src_dict.copy()
        vendor_ref = VendorRefDto.from_dict(d.pop("vendorRef"))

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = PushBillLineItemV2.from_dict(lines_item_data)

            lines.append(lines_item)

        vendor_invoice_number = d.pop("vendorInvoiceNumber", UNSET)

        _posted_date = d.pop("postedDate", UNSET)
        posted_date: Union[Unset, datetime.date]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date).date()

        _due_date = d.pop("dueDate", UNSET)
        due_date: Union[Unset, datetime.date]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date).date()

        currency_rate = d.pop("currencyRate", UNSET)

        memo = d.pop("memo", UNSET)

        currency = d.pop("currency", UNSET)

        subsidiary_refs = []
        _subsidiary_refs = d.pop("subsidiaryRefs", UNSET)
        for subsidiary_refs_item_data in _subsidiary_refs or []:
            subsidiary_refs_item = SubsidiaryRefDto.from_dict(subsidiary_refs_item_data)

            subsidiary_refs.append(subsidiary_refs_item)

        purchase_order_refs = []
        _purchase_order_refs = d.pop("purchaseOrderRefs", UNSET)
        for purchase_order_refs_item_data in _purchase_order_refs or []:
            purchase_order_refs_item = PurchaseOrderRefDto.from_dict(purchase_order_refs_item_data)

            purchase_order_refs.append(purchase_order_refs_item)

        _pass_through = d.pop("passThrough", UNSET)
        pass_through: Union[Unset, PushBillV2PassThrough]
        if isinstance(_pass_through, Unset):
            pass_through = UNSET
        else:
            pass_through = PushBillV2PassThrough.from_dict(_pass_through)

        push_bill_v2 = cls(
            vendor_ref=vendor_ref,
            lines=lines,
            vendor_invoice_number=vendor_invoice_number,
            posted_date=posted_date,
            due_date=due_date,
            currency_rate=currency_rate,
            memo=memo,
            currency=currency,
            subsidiary_refs=subsidiary_refs,
            purchase_order_refs=purchase_order_refs,
            pass_through=pass_through,
        )

        push_bill_v2.additional_properties = d
        return push_bill_v2

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
