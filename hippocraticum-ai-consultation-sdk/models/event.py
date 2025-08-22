from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Event")


@_attrs_define
class Event:
    """
    Attributes:
        speaker (str):
        event_type (str):
        event_msg (str):
        text (str):
        start (float):
        end (float):
    """

    speaker: str
    event_type: str
    event_msg: str
    text: str
    start: float
    end: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        speaker = self.speaker

        event_type = self.event_type

        event_msg = self.event_msg

        text = self.text

        start = self.start

        end = self.end

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "speaker": speaker,
                "event_type": event_type,
                "event_msg": event_msg,
                "text": text,
                "start": start,
                "end": end,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        speaker = d.pop("speaker")

        event_type = d.pop("event_type")

        event_msg = d.pop("event_msg")

        text = d.pop("text")

        start = d.pop("start")

        end = d.pop("end")

        event = cls(
            speaker=speaker,
            event_type=event_type,
            event_msg=event_msg,
            text=text,
            start=start,
            end=end,
        )

        event.additional_properties = d
        return event

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
