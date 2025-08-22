from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.process_part import ProcessPart

T = TypeVar("T", bound="PydanticGetOperationResponse")


@_attrs_define
class PydanticGetOperationResponse:
    """
    Attributes:
        operation_id (str):
        process_part (ProcessPart):
    """

    operation_id: str
    process_part: ProcessPart
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operation_id = self.operation_id

        process_part = self.process_part.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operation_id": operation_id,
                "process_part": process_part,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        operation_id = d.pop("operation_id")

        process_part = ProcessPart(d.pop("process_part"))

        pydantic_get_operation_response = cls(
            operation_id=operation_id,
            process_part=process_part,
        )

        pydantic_get_operation_response.additional_properties = d
        return pydantic_get_operation_response

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
