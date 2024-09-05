import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_product_data_status import GetProductDataStatus, check_get_product_data_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_variants import ProductVariants


T = TypeVar("T", bound="GetProductData")


@_attrs_define
class GetProductData:
    """
    Attributes:
        id (str):  Example: 632910392.
        name (str):  Example: Amazon Echo.
        created_date (datetime.datetime):  Example: 2021-03-09T10:18:29.985Z.
        source_modified_date (datetime.datetime):  Example: 2021-03-09T10:18:29.985Z.
        status (GetProductDataStatus):  Example: active.
        type (Union[Unset, str]):  Example: Speakers.
        description (Union[Unset, str]):  Example: Sample product description.
        is_gift_card (Union[Unset, bool]):  Example: True.
        product_variants (Union[Unset, List['ProductVariants']]):
    """

    id: str
    name: str
    created_date: datetime.datetime
    source_modified_date: datetime.datetime
    status: GetProductDataStatus
    type: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    is_gift_card: Union[Unset, bool] = UNSET
    product_variants: Union[Unset, List["ProductVariants"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        created_date = self.created_date.isoformat()

        source_modified_date = self.source_modified_date.isoformat()

        status: str = self.status

        type = self.type

        description = self.description

        is_gift_card = self.is_gift_card

        product_variants: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.product_variants, Unset):
            product_variants = []
            for product_variants_item_data in self.product_variants:
                product_variants_item = product_variants_item_data.to_dict()
                product_variants.append(product_variants_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "createdDate": created_date,
                "sourceModifiedDate": source_modified_date,
                "status": status,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type
        if description is not UNSET:
            field_dict["description"] = description
        if is_gift_card is not UNSET:
            field_dict["isGiftCard"] = is_gift_card
        if product_variants is not UNSET:
            field_dict["productVariants"] = product_variants

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.product_variants import ProductVariants

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        created_date = isoparse(d.pop("createdDate"))

        source_modified_date = isoparse(d.pop("sourceModifiedDate"))

        status = check_get_product_data_status(d.pop("status"))

        type = d.pop("type", UNSET)

        description = d.pop("description", UNSET)

        is_gift_card = d.pop("isGiftCard", UNSET)

        product_variants = []
        _product_variants = d.pop("productVariants", UNSET)
        for product_variants_item_data in _product_variants or []:
            product_variants_item = ProductVariants.from_dict(product_variants_item_data)

            product_variants.append(product_variants_item)

        get_product_data = cls(
            id=id,
            name=name,
            created_date=created_date,
            source_modified_date=source_modified_date,
            status=status,
            type=type,
            description=description,
            is_gift_card=is_gift_card,
            product_variants=product_variants,
        )

        get_product_data.additional_properties = d
        return get_product_data

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
