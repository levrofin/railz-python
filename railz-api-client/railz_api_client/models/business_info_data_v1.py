from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.business_info_data_v1_business_type import (
    BusinessInfoDataV1BusinessType,
    check_business_info_data_v1_business_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.business_info_address import BusinessInfoAddress
    from ..models.business_info_currency_ref import BusinessInfoCurrencyRef
    from ..models.business_info_location_ref import BusinessInfoLocationRef
    from ..models.business_info_subsidiary_ref import BusinessInfoSubsidiaryRef


T = TypeVar("T", bound="BusinessInfoDataV1")


@_attrs_define
class BusinessInfoDataV1:
    """
    Attributes:
        business_name (Union[Unset, str]):  Example: Railz.
        legal_name (Union[Unset, str]):  Example: Railz Financial Technologies Inc.
        business_email (Union[Unset, str]):  Example: noreply@railz.ai.
        website (Union[Unset, str]):  Example: www.railz.ai.
        primary_phone_number (Union[Unset, str]):  Example: 416-555-1212.
        fiscal_year_end_day (Union[Unset, float]):  Example: 31.
        fiscal_year_end_month (Union[Unset, float]):  Example: 12.
        industry_type (Union[Unset, str]):  Example: Financial.
        industry_code (Union[Unset, str]):  Example: 123.
        business_short_code (Union[Unset, str]):  Example: 6Qfdg!.
        base_currency (Union[Unset, str]):  Example: USD.
        business_registration_number (Union[Unset, str]):  Example: BN123456789.
        currency_refs (Union[Unset, List['BusinessInfoCurrencyRef']]):
        subsidiary_refs (Union[Unset, List['BusinessInfoSubsidiaryRef']]):
        mailing_address (Union[Unset, BusinessInfoAddress]):
        legal_address (Union[Unset, BusinessInfoAddress]):
        location_refs (Union[Unset, List['BusinessInfoLocationRef']]):
        business_type (Union[Unset, BusinessInfoDataV1BusinessType]):  Example: organization.
        accounting_method (Union[Unset, str]):  Example: accrual.
    """

    business_name: Union[Unset, str] = UNSET
    legal_name: Union[Unset, str] = UNSET
    business_email: Union[Unset, str] = UNSET
    website: Union[Unset, str] = UNSET
    primary_phone_number: Union[Unset, str] = UNSET
    fiscal_year_end_day: Union[Unset, float] = UNSET
    fiscal_year_end_month: Union[Unset, float] = UNSET
    industry_type: Union[Unset, str] = UNSET
    industry_code: Union[Unset, str] = UNSET
    business_short_code: Union[Unset, str] = UNSET
    base_currency: Union[Unset, str] = UNSET
    business_registration_number: Union[Unset, str] = UNSET
    currency_refs: Union[Unset, List["BusinessInfoCurrencyRef"]] = UNSET
    subsidiary_refs: Union[Unset, List["BusinessInfoSubsidiaryRef"]] = UNSET
    mailing_address: Union[Unset, "BusinessInfoAddress"] = UNSET
    legal_address: Union[Unset, "BusinessInfoAddress"] = UNSET
    location_refs: Union[Unset, List["BusinessInfoLocationRef"]] = UNSET
    business_type: Union[Unset, BusinessInfoDataV1BusinessType] = UNSET
    accounting_method: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        business_name = self.business_name

        legal_name = self.legal_name

        business_email = self.business_email

        website = self.website

        primary_phone_number = self.primary_phone_number

        fiscal_year_end_day = self.fiscal_year_end_day

        fiscal_year_end_month = self.fiscal_year_end_month

        industry_type = self.industry_type

        industry_code = self.industry_code

        business_short_code = self.business_short_code

        base_currency = self.base_currency

        business_registration_number = self.business_registration_number

        currency_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.currency_refs, Unset):
            currency_refs = []
            for currency_refs_item_data in self.currency_refs:
                currency_refs_item = currency_refs_item_data.to_dict()
                currency_refs.append(currency_refs_item)

        subsidiary_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subsidiary_refs, Unset):
            subsidiary_refs = []
            for subsidiary_refs_item_data in self.subsidiary_refs:
                subsidiary_refs_item = subsidiary_refs_item_data.to_dict()
                subsidiary_refs.append(subsidiary_refs_item)

        mailing_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mailing_address, Unset):
            mailing_address = self.mailing_address.to_dict()

        legal_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.legal_address, Unset):
            legal_address = self.legal_address.to_dict()

        location_refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.location_refs, Unset):
            location_refs = []
            for location_refs_item_data in self.location_refs:
                location_refs_item = location_refs_item_data.to_dict()
                location_refs.append(location_refs_item)

        business_type: Union[Unset, str] = UNSET
        if not isinstance(self.business_type, Unset):
            business_type = self.business_type

        accounting_method = self.accounting_method

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if business_name is not UNSET:
            field_dict["businessName"] = business_name
        if legal_name is not UNSET:
            field_dict["legalName"] = legal_name
        if business_email is not UNSET:
            field_dict["businessEmail"] = business_email
        if website is not UNSET:
            field_dict["website"] = website
        if primary_phone_number is not UNSET:
            field_dict["primaryPhoneNumber"] = primary_phone_number
        if fiscal_year_end_day is not UNSET:
            field_dict["fiscalYearEndDay"] = fiscal_year_end_day
        if fiscal_year_end_month is not UNSET:
            field_dict["fiscalYearEndMonth"] = fiscal_year_end_month
        if industry_type is not UNSET:
            field_dict["industryType"] = industry_type
        if industry_code is not UNSET:
            field_dict["industryCode"] = industry_code
        if business_short_code is not UNSET:
            field_dict["businessShortCode"] = business_short_code
        if base_currency is not UNSET:
            field_dict["baseCurrency"] = base_currency
        if business_registration_number is not UNSET:
            field_dict["businessRegistrationNumber"] = business_registration_number
        if currency_refs is not UNSET:
            field_dict["currencyRefs"] = currency_refs
        if subsidiary_refs is not UNSET:
            field_dict["subsidiaryRefs"] = subsidiary_refs
        if mailing_address is not UNSET:
            field_dict["mailingAddress"] = mailing_address
        if legal_address is not UNSET:
            field_dict["legalAddress"] = legal_address
        if location_refs is not UNSET:
            field_dict["locationRefs"] = location_refs
        if business_type is not UNSET:
            field_dict["businessType"] = business_type
        if accounting_method is not UNSET:
            field_dict["accountingMethod"] = accounting_method

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.business_info_address import BusinessInfoAddress
        from ..models.business_info_currency_ref import BusinessInfoCurrencyRef
        from ..models.business_info_location_ref import BusinessInfoLocationRef
        from ..models.business_info_subsidiary_ref import BusinessInfoSubsidiaryRef

        d = src_dict.copy()
        business_name = d.pop("businessName", UNSET)

        legal_name = d.pop("legalName", UNSET)

        business_email = d.pop("businessEmail", UNSET)

        website = d.pop("website", UNSET)

        primary_phone_number = d.pop("primaryPhoneNumber", UNSET)

        fiscal_year_end_day = d.pop("fiscalYearEndDay", UNSET)

        fiscal_year_end_month = d.pop("fiscalYearEndMonth", UNSET)

        industry_type = d.pop("industryType", UNSET)

        industry_code = d.pop("industryCode", UNSET)

        business_short_code = d.pop("businessShortCode", UNSET)

        base_currency = d.pop("baseCurrency", UNSET)

        business_registration_number = d.pop("businessRegistrationNumber", UNSET)

        currency_refs = []
        _currency_refs = d.pop("currencyRefs", UNSET)
        for currency_refs_item_data in _currency_refs or []:
            currency_refs_item = BusinessInfoCurrencyRef.from_dict(currency_refs_item_data)

            currency_refs.append(currency_refs_item)

        subsidiary_refs = []
        _subsidiary_refs = d.pop("subsidiaryRefs", UNSET)
        for subsidiary_refs_item_data in _subsidiary_refs or []:
            subsidiary_refs_item = BusinessInfoSubsidiaryRef.from_dict(subsidiary_refs_item_data)

            subsidiary_refs.append(subsidiary_refs_item)

        _mailing_address = d.pop("mailingAddress", UNSET)
        mailing_address: Union[Unset, BusinessInfoAddress]
        if isinstance(_mailing_address, Unset):
            mailing_address = UNSET
        else:
            mailing_address = BusinessInfoAddress.from_dict(_mailing_address)

        _legal_address = d.pop("legalAddress", UNSET)
        legal_address: Union[Unset, BusinessInfoAddress]
        if isinstance(_legal_address, Unset):
            legal_address = UNSET
        else:
            legal_address = BusinessInfoAddress.from_dict(_legal_address)

        location_refs = []
        _location_refs = d.pop("locationRefs", UNSET)
        for location_refs_item_data in _location_refs or []:
            location_refs_item = BusinessInfoLocationRef.from_dict(location_refs_item_data)

            location_refs.append(location_refs_item)

        _business_type = d.pop("businessType", UNSET)
        business_type: Union[Unset, BusinessInfoDataV1BusinessType]
        if isinstance(_business_type, Unset):
            business_type = UNSET
        else:
            business_type = check_business_info_data_v1_business_type(_business_type)

        accounting_method = d.pop("accountingMethod", UNSET)

        business_info_data_v1 = cls(
            business_name=business_name,
            legal_name=legal_name,
            business_email=business_email,
            website=website,
            primary_phone_number=primary_phone_number,
            fiscal_year_end_day=fiscal_year_end_day,
            fiscal_year_end_month=fiscal_year_end_month,
            industry_type=industry_type,
            industry_code=industry_code,
            business_short_code=business_short_code,
            base_currency=base_currency,
            business_registration_number=business_registration_number,
            currency_refs=currency_refs,
            subsidiary_refs=subsidiary_refs,
            mailing_address=mailing_address,
            legal_address=legal_address,
            location_refs=location_refs,
            business_type=business_type,
            accounting_method=accounting_method,
        )

        business_info_data_v1.additional_properties = d
        return business_info_data_v1

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
