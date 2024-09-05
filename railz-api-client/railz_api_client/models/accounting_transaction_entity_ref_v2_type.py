from typing import Literal, Set, cast

AccountingTransactionEntityRefV2Type = Literal["customer", "unknown", "vendor"]

ACCOUNTING_TRANSACTION_ENTITY_REF_V2_TYPE_VALUES: Set[AccountingTransactionEntityRefV2Type] = {
    "customer",
    "unknown",
    "vendor",
}


def check_accounting_transaction_entity_ref_v2_type(value: str) -> AccountingTransactionEntityRefV2Type:
    if value in ACCOUNTING_TRANSACTION_ENTITY_REF_V2_TYPE_VALUES:
        return cast(AccountingTransactionEntityRefV2Type, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACCOUNTING_TRANSACTION_ENTITY_REF_V2_TYPE_VALUES!r}")
