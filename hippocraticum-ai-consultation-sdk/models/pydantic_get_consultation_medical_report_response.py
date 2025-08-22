from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.medical_report_entity import MedicalReportEntity


T = TypeVar("T", bound="PydanticGetConsultationMedicalReportResponse")


@_attrs_define
class PydanticGetConsultationMedicalReportResponse:
    """
    Attributes:
        medical_report (MedicalReportEntity):
    """

    medical_report: "MedicalReportEntity"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        medical_report = self.medical_report.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "medical_report": medical_report,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.medical_report_entity import MedicalReportEntity

        d = dict(src_dict)
        medical_report = MedicalReportEntity.from_dict(d.pop("medical_report"))

        pydantic_get_consultation_medical_report_response = cls(
            medical_report=medical_report,
        )

        pydantic_get_consultation_medical_report_response.additional_properties = d
        return pydantic_get_consultation_medical_report_response

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
