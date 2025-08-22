from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.consultation_state import ConsultationState

if TYPE_CHECKING:
    from ..models.icd10_candidate import ICD10Candidate


T = TypeVar("T", bound="PydanticGetConsultationIcd10Response")


@_attrs_define
class PydanticGetConsultationIcd10Response:
    """
    Attributes:
        consultation_id (str):
        state (ConsultationState):
        icd10_candidates (list['ICD10Candidate']):
    """

    consultation_id: str
    state: ConsultationState
    icd10_candidates: list["ICD10Candidate"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        consultation_id = self.consultation_id

        state = self.state.value

        icd10_candidates = []
        for icd10_candidates_item_data in self.icd10_candidates:
            icd10_candidates_item = icd10_candidates_item_data.to_dict()
            icd10_candidates.append(icd10_candidates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "consultation_id": consultation_id,
                "state": state,
                "icd10_candidates": icd10_candidates,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.icd10_candidate import ICD10Candidate

        d = dict(src_dict)
        consultation_id = d.pop("consultation_id")

        state = ConsultationState(d.pop("state"))

        icd10_candidates = []
        _icd10_candidates = d.pop("icd10_candidates")
        for icd10_candidates_item_data in _icd10_candidates:
            icd10_candidates_item = ICD10Candidate.from_dict(icd10_candidates_item_data)

            icd10_candidates.append(icd10_candidates_item)

        pydantic_get_consultation_icd_10_response = cls(
            consultation_id=consultation_id,
            state=state,
            icd10_candidates=icd10_candidates,
        )

        pydantic_get_consultation_icd_10_response.additional_properties = d
        return pydantic_get_consultation_icd_10_response

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
