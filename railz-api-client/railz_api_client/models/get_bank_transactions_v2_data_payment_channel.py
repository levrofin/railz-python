from typing import Literal, Set, cast

GetBankTransactionsV2DataPaymentChannel = Literal["inStore", "online", "other"]

GET_BANK_TRANSACTIONS_V2_DATA_PAYMENT_CHANNEL_VALUES: Set[GetBankTransactionsV2DataPaymentChannel] = {
    "inStore",
    "online",
    "other",
}


def check_get_bank_transactions_v2_data_payment_channel(value: str) -> GetBankTransactionsV2DataPaymentChannel:
    if value in GET_BANK_TRANSACTIONS_V2_DATA_PAYMENT_CHANNEL_VALUES:
        return cast(GetBankTransactionsV2DataPaymentChannel, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_BANK_TRANSACTIONS_V2_DATA_PAYMENT_CHANNEL_VALUES!r}"
    )
