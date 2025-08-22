from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PydanticConsultationRealtimeFeatures")


@_attrs_define
class PydanticConsultationRealtimeFeatures:
    """
    Attributes:
        insights (Union[Unset, bool]):  Default: False.
        symptoms (Union[Unset, bool]):  Default: False.
        differential_diagnosis (Union[Unset, bool]):  Default: False.
        follow_up (Union[Unset, bool]):  Default: False.
        stats (Union[Unset, bool]):  Default: False.
    """

    insights: Union[Unset, bool] = False
    symptoms: Union[Unset, bool] = False
    differential_diagnosis: Union[Unset, bool] = False
    follow_up: Union[Unset, bool] = False
    stats: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        insights = self.insights

        symptoms = self.symptoms

        differential_diagnosis = self.differential_diagnosis

        follow_up = self.follow_up

        stats = self.stats

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if insights is not UNSET:
            field_dict["insights"] = insights
        if symptoms is not UNSET:
            field_dict["symptoms"] = symptoms
        if differential_diagnosis is not UNSET:
            field_dict["differential_diagnosis"] = differential_diagnosis
        if follow_up is not UNSET:
            field_dict["follow_up"] = follow_up
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        insights = d.pop("insights", UNSET)

        symptoms = d.pop("symptoms", UNSET)

        differential_diagnosis = d.pop("differential_diagnosis", UNSET)

        follow_up = d.pop("follow_up", UNSET)

        stats = d.pop("stats", UNSET)

        pydantic_consultation_realtime_features = cls(
            insights=insights,
            symptoms=symptoms,
            differential_diagnosis=differential_diagnosis,
            follow_up=follow_up,
            stats=stats,
        )

        pydantic_consultation_realtime_features.additional_properties = d
        return pydantic_consultation_realtime_features

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
