"""Contains some shared types for properties"""

import base64
from http import HTTPStatus
from typing import BinaryIO, Generic, Literal, MutableMapping, Optional, Tuple, TypeVar

from attrs import define


class Unset:
    def __bool__(self) -> Literal[False]:
        return False


UNSET: Unset = Unset()

FileJsonType = Tuple[Optional[str], BinaryIO, Optional[str]]


@define
class File:
    """Contains information for file uploads"""

    payload: BinaryIO
    file_name: Optional[str] = None
    mime_type: Optional[str] = None

    def to_tuple(self) -> FileJsonType:
        """Return a tuple representation that httpx will accept for multipart/form-data"""
        return self.file_name, self.payload, self.mime_type

    def to_json(self) -> str:
        """Based on generated sample code from https://docs.railz.ai/reference/pushattachment."""
        return f"{self.mime_type};name={self.file_name};base64,{base64.b64encode(self.payload.read()).decode()}"


T = TypeVar("T")


@define
class Response(Generic[T]):
    """A response from an endpoint"""

    status_code: HTTPStatus
    content: bytes
    headers: MutableMapping[str, str]
    parsed: Optional[T]


__all__ = ["File", "Response", "FileJsonType", "Unset", "UNSET"]
