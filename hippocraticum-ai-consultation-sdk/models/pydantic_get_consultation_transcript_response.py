from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.consultation_state import ConsultationState

T = TypeVar("T", bound="PydanticGetConsultationTranscriptResponse")


@_attrs_define
class PydanticGetConsultationTranscriptResponse:
    """
    Attributes:
        consultation_id (str):
        state (ConsultationState):
        transcription (Union[None, str]):
    """

    consultation_id: str
    state: ConsultationState
    transcription: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        consultation_id = self.consultation_id

        state = self.state.value

        transcription: Union[None, str]
        transcription = self.transcription

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "consultation_id": consultation_id,
                "state": state,
                "transcription": transcription,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        consultation_id = d.pop("consultation_id")

        state = ConsultationState(d.pop("state"))

        def _parse_transcription(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        transcription = _parse_transcription(d.pop("transcription"))

        pydantic_get_consultation_transcript_response = cls(
            consultation_id=consultation_id,
            state=state,
            transcription=transcription,
        )

        pydantic_get_consultation_transcript_response.additional_properties = d
        return pydantic_get_consultation_transcript_response

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
