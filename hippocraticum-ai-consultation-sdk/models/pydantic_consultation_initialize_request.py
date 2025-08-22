from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.consultation_type import ConsultationType
from ..models.google_language_code import GoogleLanguageCode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pydantic_consultation_realtime_features import PydanticConsultationRealtimeFeatures


T = TypeVar("T", bound="PydanticConsultationInitializeRequest")


@_attrs_define
class PydanticConsultationInitializeRequest:
    """
    Attributes:
        consultation_type (ConsultationType):
        patient_id (Union[Unset, str]):  Default: '688a0211c7b194b0d26cb6b9'.
        doctor_id (Union[Unset, str]):  Default: '688a02a9c7b194b0d26cb6bb'.
        enabled_features (Union[Unset, PydanticConsultationRealtimeFeatures]):
        translate_lang_code (Union[GoogleLanguageCode, None, Unset]):
    """

    consultation_type: ConsultationType
    patient_id: Union[Unset, str] = "688a0211c7b194b0d26cb6b9"
    doctor_id: Union[Unset, str] = "688a02a9c7b194b0d26cb6bb"
    enabled_features: Union[Unset, "PydanticConsultationRealtimeFeatures"] = UNSET
    translate_lang_code: Union[GoogleLanguageCode, None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        consultation_type = self.consultation_type.value

        patient_id = self.patient_id

        doctor_id = self.doctor_id

        enabled_features: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.enabled_features, Unset):
            enabled_features = self.enabled_features.to_dict()

        translate_lang_code: Union[None, Unset, str]
        if isinstance(self.translate_lang_code, Unset):
            translate_lang_code = UNSET
        elif isinstance(self.translate_lang_code, GoogleLanguageCode):
            translate_lang_code = self.translate_lang_code.value
        else:
            translate_lang_code = self.translate_lang_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "consultation_type": consultation_type,
            }
        )
        if patient_id is not UNSET:
            field_dict["patient_id"] = patient_id
        if doctor_id is not UNSET:
            field_dict["doctor_id"] = doctor_id
        if enabled_features is not UNSET:
            field_dict["enabled_features"] = enabled_features
        if translate_lang_code is not UNSET:
            field_dict["translate_lang_code"] = translate_lang_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pydantic_consultation_realtime_features import PydanticConsultationRealtimeFeatures

        d = dict(src_dict)
        consultation_type = ConsultationType(d.pop("consultation_type"))

        patient_id = d.pop("patient_id", UNSET)

        doctor_id = d.pop("doctor_id", UNSET)

        _enabled_features = d.pop("enabled_features", UNSET)
        enabled_features: Union[Unset, PydanticConsultationRealtimeFeatures]
        if isinstance(_enabled_features, Unset):
            enabled_features = UNSET
        else:
            enabled_features = PydanticConsultationRealtimeFeatures.from_dict(_enabled_features)

        def _parse_translate_lang_code(data: object) -> Union[GoogleLanguageCode, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                translate_lang_code_type_0 = GoogleLanguageCode(data)

                return translate_lang_code_type_0
            except:  # noqa: E722
                pass
            return cast(Union[GoogleLanguageCode, None, Unset], data)

        translate_lang_code = _parse_translate_lang_code(d.pop("translate_lang_code", UNSET))

        pydantic_consultation_initialize_request = cls(
            consultation_type=consultation_type,
            patient_id=patient_id,
            doctor_id=doctor_id,
            enabled_features=enabled_features,
            translate_lang_code=translate_lang_code,
        )

        pydantic_consultation_initialize_request.additional_properties = d
        return pydantic_consultation_initialize_request

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
