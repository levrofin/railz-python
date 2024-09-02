import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinancialForecastDataV1")


@_attrs_define
class FinancialForecastDataV1:
    """
    Attributes:
        section (str):  Example: Assets.
        sub_section (str):  Example: Current Assets.
        group (str):  Example: Cash And Cash Equivalents.
        sub_group (str):  Example: Checking.
        account (str):  Example: Bank of America.
        end_date (datetime.date):  Example: 2022-03-31.
        amount (float):  Example: 1500000.5.
        sub_account (Union[Unset, str]):
    """

    section: str
    sub_section: str
    group: str
    sub_group: str
    account: str
    end_date: datetime.date
    amount: float
    sub_account: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        section = self.section

        sub_section = self.sub_section

        group = self.group

        sub_group = self.sub_group

        account = self.account

        end_date = self.end_date.isoformat()

        amount = self.amount

        sub_account = self.sub_account

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "section": section,
                "subSection": sub_section,
                "group": group,
                "subGroup": sub_group,
                "account": account,
                "endDate": end_date,
                "amount": amount,
            }
        )
        if sub_account is not UNSET:
            field_dict["subAccount"] = sub_account

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        section = d.pop("section")

        sub_section = d.pop("subSection")

        group = d.pop("group")

        sub_group = d.pop("subGroup")

        account = d.pop("account")

        end_date = isoparse(d.pop("endDate")).date()

        amount = d.pop("amount")

        sub_account = d.pop("subAccount", UNSET)

        financial_forecast_data_v1 = cls(
            section=section,
            sub_section=sub_section,
            group=group,
            sub_group=sub_group,
            account=account,
            end_date=end_date,
            amount=amount,
            sub_account=sub_account,
        )

        financial_forecast_data_v1.additional_properties = d
        return financial_forecast_data_v1

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
