from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PydanticPostProcessResponse")


@_attrs_define
class PydanticPostProcessResponse:
    """
    Attributes:
        consultation_id (str):
        operation_id (str):
        message (Union[Unset, str]):  Default: 'Audio upload successful, processing started'.
    """

    consultation_id: str
    operation_id: str
    message: Union[Unset, str] = "Audio upload successful, processing started"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        consultation_id = self.consultation_id

        operation_id = self.operation_id

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "consultation_id": consultation_id,
                "operation_id": operation_id,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        consultation_id = d.pop("consultation_id")

        operation_id = d.pop("operation_id")

        message = d.pop("message", UNSET)

        pydantic_post_process_response = cls(
            consultation_id=consultation_id,
            operation_id=operation_id,
            message=message,
        )

        pydantic_post_process_response.additional_properties = d
        return pydantic_post_process_response

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
