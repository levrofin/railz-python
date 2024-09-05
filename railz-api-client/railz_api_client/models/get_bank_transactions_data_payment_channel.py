from typing import Literal, Set, cast

GetBankTransactionsDataPaymentChannel = Literal["inStore", "online", "other"]

GET_BANK_TRANSACTIONS_DATA_PAYMENT_CHANNEL_VALUES: Set[GetBankTransactionsDataPaymentChannel] = {
    "inStore",
    "online",
    "other",
}


def check_get_bank_transactions_data_payment_channel(value: str) -> GetBankTransactionsDataPaymentChannel:
    if value in GET_BANK_TRANSACTIONS_DATA_PAYMENT_CHANNEL_VALUES:
        return cast(GetBankTransactionsDataPaymentChannel, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_BANK_TRANSACTIONS_DATA_PAYMENT_CHANNEL_VALUES!r}"
    )
