from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...models.http_validation_error import HTTPValidationError
from ...models.medical_response_format import MedicalResponseFormat
from ...models.pydantic_get_consultation_medical_report_response import PydanticGetConsultationMedicalReportResponse
from ...types import Response


def _get_kwargs(
    id: str,
    type_of_medical_report: MedicalResponseFormat,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/sessions/{id}/report/{type_of_medical_report}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient, response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, PydanticGetConsultationMedicalReportResponse]]:
    if response.status_code == 200:
        response_200 = PydanticGetConsultationMedicalReportResponse.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient, response: httpx.Response
) -> Response[Union[Any, HTTPValidationError, PydanticGetConsultationMedicalReportResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    type_of_medical_report: MedicalResponseFormat,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, HTTPValidationError, PydanticGetConsultationMedicalReportResponse]]:
    """Get medical report

     Retrieve a formatted medical report based on the consultation data. Available formats include PDF,
    HTML, and structured JSON formats for different use cases.

    Args:
        id (str): Unique identifier for the consultation session
        type_of_medical_report (MedicalResponseFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, PydanticGetConsultationMedicalReportResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        type_of_medical_report=type_of_medical_report,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    type_of_medical_report: MedicalResponseFormat,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, HTTPValidationError, PydanticGetConsultationMedicalReportResponse]]:
    """Get medical report

     Retrieve a formatted medical report based on the consultation data. Available formats include PDF,
    HTML, and structured JSON formats for different use cases.

    Args:
        id (str): Unique identifier for the consultation session
        type_of_medical_report (MedicalResponseFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, PydanticGetConsultationMedicalReportResponse]
    """

    return sync_detailed(
        id=id,
        type_of_medical_report=type_of_medical_report,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    type_of_medical_report: MedicalResponseFormat,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, HTTPValidationError, PydanticGetConsultationMedicalReportResponse]]:
    """Get medical report

     Retrieve a formatted medical report based on the consultation data. Available formats include PDF,
    HTML, and structured JSON formats for different use cases.

    Args:
        id (str): Unique identifier for the consultation session
        type_of_medical_report (MedicalResponseFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, PydanticGetConsultationMedicalReportResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        type_of_medical_report=type_of_medical_report,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    type_of_medical_report: MedicalResponseFormat,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, HTTPValidationError, PydanticGetConsultationMedicalReportResponse]]:
    """Get medical report

     Retrieve a formatted medical report based on the consultation data. Available formats include PDF,
    HTML, and structured JSON formats for different use cases.

    Args:
        id (str): Unique identifier for the consultation session
        type_of_medical_report (MedicalResponseFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, PydanticGetConsultationMedicalReportResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            type_of_medical_report=type_of_medical_report,
            client=client,
        )
    ).parsed
