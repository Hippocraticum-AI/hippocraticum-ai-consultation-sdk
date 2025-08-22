from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.medical_response_format import MedicalResponseFormat

if TYPE_CHECKING:
    from ..models.created_at import CreatedAt
    from ..models.id import Id
    from ..models.medical_response_body import MedicalResponseBody
    from ..models.pathto_pdf import PathtoPDF
    from ..models.update_at import UpdateAt


T = TypeVar("T", bound="MedicalReportEntity")


@_attrs_define
class MedicalReportEntity:
    """
    Attributes:
        id (Id):
        consultation_id (Id):
        created_at (CreatedAt):
        updated_at (UpdateAt):
        format_ (MedicalResponseFormat):
        body (MedicalResponseBody):
        path_to_pdf (PathtoPDF):
    """

    id: "Id"
    consultation_id: "Id"
    created_at: "CreatedAt"
    updated_at: "UpdateAt"
    format_: MedicalResponseFormat
    body: "MedicalResponseBody"
    path_to_pdf: "PathtoPDF"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id.to_dict()

        consultation_id = self.consultation_id.to_dict()

        created_at = self.created_at.to_dict()

        updated_at = self.updated_at.to_dict()

        format_ = self.format_.value

        body = self.body.to_dict()

        path_to_pdf = self.path_to_pdf.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "consultation_id": consultation_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "format": format_,
                "body": body,
                "path_to_pdf": path_to_pdf,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.created_at import CreatedAt
        from ..models.id import Id
        from ..models.medical_response_body import MedicalResponseBody
        from ..models.pathto_pdf import PathtoPDF
        from ..models.update_at import UpdateAt

        d = dict(src_dict)
        id = Id.from_dict(d.pop("id"))

        consultation_id = Id.from_dict(d.pop("consultation_id"))

        created_at = CreatedAt.from_dict(d.pop("created_at"))

        updated_at = UpdateAt.from_dict(d.pop("updated_at"))

        format_ = MedicalResponseFormat(d.pop("format"))

        body = MedicalResponseBody.from_dict(d.pop("body"))

        path_to_pdf = PathtoPDF.from_dict(d.pop("path_to_pdf"))

        medical_report_entity = cls(
            id=id,
            consultation_id=consultation_id,
            created_at=created_at,
            updated_at=updated_at,
            format_=format_,
            body=body,
            path_to_pdf=path_to_pdf,
        )

        medical_report_entity.additional_properties = d
        return medical_report_entity

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
