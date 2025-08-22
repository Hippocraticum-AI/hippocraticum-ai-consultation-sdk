from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.consultation_state import ConsultationState

if TYPE_CHECKING:
    from ..models.pydantic_consultation_public_context_type_0 import PydanticConsultationPublicContextType0


T = TypeVar("T", bound="PydanticConsultationPublic")


@_attrs_define
class PydanticConsultationPublic:
    """
    Attributes:
        consultation_id (str):
        state (ConsultationState):
        context (Union['PydanticConsultationPublicContextType0', None]):
    """

    consultation_id: str
    state: ConsultationState
    context: Union["PydanticConsultationPublicContextType0", None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.pydantic_consultation_public_context_type_0 import PydanticConsultationPublicContextType0

        consultation_id = self.consultation_id

        state = self.state.value

        context: Union[None, dict[str, Any]]
        if isinstance(self.context, PydanticConsultationPublicContextType0):
            context = self.context.to_dict()
        else:
            context = self.context

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "consultation_id": consultation_id,
                "state": state,
                "context": context,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pydantic_consultation_public_context_type_0 import PydanticConsultationPublicContextType0

        d = dict(src_dict)
        consultation_id = d.pop("consultation_id")

        state = ConsultationState(d.pop("state"))

        def _parse_context(data: object) -> Union["PydanticConsultationPublicContextType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                context_type_0 = PydanticConsultationPublicContextType0.from_dict(data)

                return context_type_0
            except:  # noqa: E722
                pass
            return cast(Union["PydanticConsultationPublicContextType0", None], data)

        context = _parse_context(d.pop("context"))

        pydantic_consultation_public = cls(
            consultation_id=consultation_id,
            state=state,
            context=context,
        )

        pydantic_consultation_public.additional_properties = d
        return pydantic_consultation_public

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
