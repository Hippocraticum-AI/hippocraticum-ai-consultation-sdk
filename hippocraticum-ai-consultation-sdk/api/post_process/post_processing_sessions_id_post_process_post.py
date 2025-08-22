from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_post_processing_sessions_id_post_process_post import BodyPostProcessingSessionsIdPostProcessPost
from ...models.http_validation_error import HTTPValidationError
from ...models.pydantic_post_process_response import PydanticPostProcessResponse
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: BodyPostProcessingSessionsIdPostProcessPost,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/sessions/{id}/post-process",
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, PydanticPostProcessResponse]]:
    if response.status_code == 200:
        response_200 = PydanticPostProcessResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 413:
        response_413 = cast(Any, None)
        return response_413
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, HTTPValidationError, PydanticPostProcessResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: BodyPostProcessingSessionsIdPostProcessPost,
) -> Response[Union[Any, HTTPValidationError, PydanticPostProcessResponse]]:
    """Upload audio for post-processing

     Upload audio file for a consultation session to trigger AI analysis including transcription,
    insights, symptoms analysis, differential diagnosis, and follow-up recommendations. Returns
    operation ID for tracking progress.

    Args:
        id (str): Unique identifier for the consultation session
        body (BodyPostProcessingSessionsIdPostProcessPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, PydanticPostProcessResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: BodyPostProcessingSessionsIdPostProcessPost,
) -> Optional[Union[Any, HTTPValidationError, PydanticPostProcessResponse]]:
    """Upload audio for post-processing

     Upload audio file for a consultation session to trigger AI analysis including transcription,
    insights, symptoms analysis, differential diagnosis, and follow-up recommendations. Returns
    operation ID for tracking progress.

    Args:
        id (str): Unique identifier for the consultation session
        body (BodyPostProcessingSessionsIdPostProcessPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, PydanticPostProcessResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: BodyPostProcessingSessionsIdPostProcessPost,
) -> Response[Union[Any, HTTPValidationError, PydanticPostProcessResponse]]:
    """Upload audio for post-processing

     Upload audio file for a consultation session to trigger AI analysis including transcription,
    insights, symptoms analysis, differential diagnosis, and follow-up recommendations. Returns
    operation ID for tracking progress.

    Args:
        id (str): Unique identifier for the consultation session
        body (BodyPostProcessingSessionsIdPostProcessPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, PydanticPostProcessResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: BodyPostProcessingSessionsIdPostProcessPost,
) -> Optional[Union[Any, HTTPValidationError, PydanticPostProcessResponse]]:
    """Upload audio for post-processing

     Upload audio file for a consultation session to trigger AI analysis including transcription,
    insights, symptoms analysis, differential diagnosis, and follow-up recommendations. Returns
    operation ID for tracking progress.

    Args:
        id (str): Unique identifier for the consultation session
        body (BodyPostProcessingSessionsIdPostProcessPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, PydanticPostProcessResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
