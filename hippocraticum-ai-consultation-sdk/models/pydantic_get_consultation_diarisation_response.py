from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.consultation_state import ConsultationState

if TYPE_CHECKING:
    from ..models.pydantic_get_consultation_diarisation_response_diarisation_item import (
        PydanticGetConsultationDiarisationResponseDiarisationItem,
    )


T = TypeVar("T", bound="PydanticGetConsultationDiarisationResponse")


@_attrs_define
class PydanticGetConsultationDiarisationResponse:
    """
    Attributes:
        consultation_id (str):
        state (ConsultationState):
        diarisation (list['PydanticGetConsultationDiarisationResponseDiarisationItem']):
    """

    consultation_id: str
    state: ConsultationState
    diarisation: list["PydanticGetConsultationDiarisationResponseDiarisationItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        consultation_id = self.consultation_id

        state = self.state.value

        diarisation = []
        for diarisation_item_data in self.diarisation:
            diarisation_item = diarisation_item_data.to_dict()
            diarisation.append(diarisation_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "consultation_id": consultation_id,
                "state": state,
                "diarisation": diarisation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pydantic_get_consultation_diarisation_response_diarisation_item import (
            PydanticGetConsultationDiarisationResponseDiarisationItem,
        )

        d = dict(src_dict)
        consultation_id = d.pop("consultation_id")

        state = ConsultationState(d.pop("state"))

        diarisation = []
        _diarisation = d.pop("diarisation")
        for diarisation_item_data in _diarisation:
            diarisation_item = PydanticGetConsultationDiarisationResponseDiarisationItem.from_dict(
                diarisation_item_data
            )

            diarisation.append(diarisation_item)

        pydantic_get_consultation_diarisation_response = cls(
            consultation_id=consultation_id,
            state=state,
            diarisation=diarisation,
        )

        pydantic_get_consultation_diarisation_response.additional_properties = d
        return pydantic_get_consultation_diarisation_response

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
