from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.medical_response_body_value_type_0 import MedicalResponseBodyValueType0


T = TypeVar("T", bound="MedicalResponseBody")


@_attrs_define
class MedicalResponseBody:
    """
    Attributes:
        value (Union['MedicalResponseBodyValueType0', None]):
    """

    value: Union["MedicalResponseBodyValueType0", None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.medical_response_body_value_type_0 import MedicalResponseBodyValueType0

        value: Union[None, dict[str, Any]]
        if isinstance(self.value, MedicalResponseBodyValueType0):
            value = self.value.to_dict()
        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.medical_response_body_value_type_0 import MedicalResponseBodyValueType0

        d = dict(src_dict)

        def _parse_value(data: object) -> Union["MedicalResponseBodyValueType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_0 = MedicalResponseBodyValueType0.from_dict(data)

                return value_type_0
            except:  # noqa: E722
                pass
            return cast(Union["MedicalResponseBodyValueType0", None], data)

        value = _parse_value(d.pop("value"))

        medical_response_body = cls(
            value=value,
        )

        medical_response_body.additional_properties = d
        return medical_response_body

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
