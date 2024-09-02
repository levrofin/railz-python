from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.outlier_transactions import OutlierTransactions
    from ..models.transaction_keywords import TransactionKeywords
    from ..models.transaction_patterns import TransactionPatterns
    from ..models.transactions_section_stats import TransactionsSectionStats


T = TypeVar("T", bound="FinancialFraudRiskData")


@_attrs_define
class FinancialFraudRiskData:
    """
    Attributes:
        benford_law_score (float):  Example: 20.92.
        outlier_score (Union[Unset, float]):  Example: 0.659176337.
        outlier_ratio (Union[Unset, float]):  Example: 0.093829111.
        outlier_transactions (Union[Unset, List['OutlierTransactions']]):
        transaction_keywords (Union[Unset, List['TransactionKeywords']]):
        transactions_section_stats (Union[Unset, List['TransactionsSectionStats']]):
        transaction_patterns (Union[Unset, List['TransactionPatterns']]):
        current_ratio_delta (Union[Unset, float]):  Example: 1.
        quick_ratio_delta (Union[Unset, float]):  Example: 1.
        debt_to_equity_ratio_delta (Union[Unset, float]):  Example: 1.
        net_profit_margin_ratio_delta (Union[Unset, float]):  Example: 1.
    """

    benford_law_score: float
    outlier_score: Union[Unset, float] = UNSET
    outlier_ratio: Union[Unset, float] = UNSET
    outlier_transactions: Union[Unset, List["OutlierTransactions"]] = UNSET
    transaction_keywords: Union[Unset, List["TransactionKeywords"]] = UNSET
    transactions_section_stats: Union[Unset, List["TransactionsSectionStats"]] = UNSET
    transaction_patterns: Union[Unset, List["TransactionPatterns"]] = UNSET
    current_ratio_delta: Union[Unset, float] = UNSET
    quick_ratio_delta: Union[Unset, float] = UNSET
    debt_to_equity_ratio_delta: Union[Unset, float] = UNSET
    net_profit_margin_ratio_delta: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        benford_law_score = self.benford_law_score

        outlier_score = self.outlier_score

        outlier_ratio = self.outlier_ratio

        outlier_transactions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.outlier_transactions, Unset):
            outlier_transactions = []
            for outlier_transactions_item_data in self.outlier_transactions:
                outlier_transactions_item = outlier_transactions_item_data.to_dict()
                outlier_transactions.append(outlier_transactions_item)

        transaction_keywords: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.transaction_keywords, Unset):
            transaction_keywords = []
            for transaction_keywords_item_data in self.transaction_keywords:
                transaction_keywords_item = transaction_keywords_item_data.to_dict()
                transaction_keywords.append(transaction_keywords_item)

        transactions_section_stats: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.transactions_section_stats, Unset):
            transactions_section_stats = []
            for transactions_section_stats_item_data in self.transactions_section_stats:
                transactions_section_stats_item = transactions_section_stats_item_data.to_dict()
                transactions_section_stats.append(transactions_section_stats_item)

        transaction_patterns: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.transaction_patterns, Unset):
            transaction_patterns = []
            for transaction_patterns_item_data in self.transaction_patterns:
                transaction_patterns_item = transaction_patterns_item_data.to_dict()
                transaction_patterns.append(transaction_patterns_item)

        current_ratio_delta = self.current_ratio_delta

        quick_ratio_delta = self.quick_ratio_delta

        debt_to_equity_ratio_delta = self.debt_to_equity_ratio_delta

        net_profit_margin_ratio_delta = self.net_profit_margin_ratio_delta

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "benfordLawScore": benford_law_score,
            }
        )
        if outlier_score is not UNSET:
            field_dict["outlierScore"] = outlier_score
        if outlier_ratio is not UNSET:
            field_dict["outlierRatio"] = outlier_ratio
        if outlier_transactions is not UNSET:
            field_dict["outlierTransactions"] = outlier_transactions
        if transaction_keywords is not UNSET:
            field_dict["transactionKeywords"] = transaction_keywords
        if transactions_section_stats is not UNSET:
            field_dict["transactionsSectionStats"] = transactions_section_stats
        if transaction_patterns is not UNSET:
            field_dict["transactionPatterns"] = transaction_patterns
        if current_ratio_delta is not UNSET:
            field_dict["currentRatioDelta"] = current_ratio_delta
        if quick_ratio_delta is not UNSET:
            field_dict["quickRatioDelta"] = quick_ratio_delta
        if debt_to_equity_ratio_delta is not UNSET:
            field_dict["debtToEquityRatioDelta"] = debt_to_equity_ratio_delta
        if net_profit_margin_ratio_delta is not UNSET:
            field_dict["netProfitMarginRatioDelta"] = net_profit_margin_ratio_delta

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.outlier_transactions import OutlierTransactions
        from ..models.transaction_keywords import TransactionKeywords
        from ..models.transaction_patterns import TransactionPatterns
        from ..models.transactions_section_stats import TransactionsSectionStats

        d = src_dict.copy()
        benford_law_score = d.pop("benfordLawScore")

        outlier_score = d.pop("outlierScore", UNSET)

        outlier_ratio = d.pop("outlierRatio", UNSET)

        outlier_transactions = []
        _outlier_transactions = d.pop("outlierTransactions", UNSET)
        for outlier_transactions_item_data in _outlier_transactions or []:
            outlier_transactions_item = OutlierTransactions.from_dict(outlier_transactions_item_data)

            outlier_transactions.append(outlier_transactions_item)

        transaction_keywords = []
        _transaction_keywords = d.pop("transactionKeywords", UNSET)
        for transaction_keywords_item_data in _transaction_keywords or []:
            transaction_keywords_item = TransactionKeywords.from_dict(transaction_keywords_item_data)

            transaction_keywords.append(transaction_keywords_item)

        transactions_section_stats = []
        _transactions_section_stats = d.pop("transactionsSectionStats", UNSET)
        for transactions_section_stats_item_data in _transactions_section_stats or []:
            transactions_section_stats_item = TransactionsSectionStats.from_dict(transactions_section_stats_item_data)

            transactions_section_stats.append(transactions_section_stats_item)

        transaction_patterns = []
        _transaction_patterns = d.pop("transactionPatterns", UNSET)
        for transaction_patterns_item_data in _transaction_patterns or []:
            transaction_patterns_item = TransactionPatterns.from_dict(transaction_patterns_item_data)

            transaction_patterns.append(transaction_patterns_item)

        current_ratio_delta = d.pop("currentRatioDelta", UNSET)

        quick_ratio_delta = d.pop("quickRatioDelta", UNSET)

        debt_to_equity_ratio_delta = d.pop("debtToEquityRatioDelta", UNSET)

        net_profit_margin_ratio_delta = d.pop("netProfitMarginRatioDelta", UNSET)

        financial_fraud_risk_data = cls(
            benford_law_score=benford_law_score,
            outlier_score=outlier_score,
            outlier_ratio=outlier_ratio,
            outlier_transactions=outlier_transactions,
            transaction_keywords=transaction_keywords,
            transactions_section_stats=transactions_section_stats,
            transaction_patterns=transaction_patterns,
            current_ratio_delta=current_ratio_delta,
            quick_ratio_delta=quick_ratio_delta,
            debt_to_equity_ratio_delta=debt_to_equity_ratio_delta,
            net_profit_margin_ratio_delta=net_profit_margin_ratio_delta,
        )

        financial_fraud_risk_data.additional_properties = d
        return financial_fraud_risk_data

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
