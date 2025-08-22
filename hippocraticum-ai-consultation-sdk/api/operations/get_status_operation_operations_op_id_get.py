from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.pydantic_get_operation_response import PydanticGetOperationResponse
from ...types import Response


def _get_kwargs(
    op_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/operations/{op_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, PydanticGetOperationResponse]]:
    if response.status_code == 200:
        response_200 = PydanticGetOperationResponse.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, HTTPValidationError, PydanticGetOperationResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    op_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, HTTPValidationError, PydanticGetOperationResponse]]:
    """Get operation status

     Retrieve the current status and progress of a background operation (e.g., audio processing, AI
    analysis). Returns operation state, progress percentage, and any error information.

    Args:
        op_id (str): Unique identifier for the operation

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, PydanticGetOperationResponse]]
    """

    kwargs = _get_kwargs(
        op_id=op_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    op_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, HTTPValidationError, PydanticGetOperationResponse]]:
    """Get operation status

     Retrieve the current status and progress of a background operation (e.g., audio processing, AI
    analysis). Returns operation state, progress percentage, and any error information.

    Args:
        op_id (str): Unique identifier for the operation

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, PydanticGetOperationResponse]
    """

    return sync_detailed(
        op_id=op_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    op_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, HTTPValidationError, PydanticGetOperationResponse]]:
    """Get operation status

     Retrieve the current status and progress of a background operation (e.g., audio processing, AI
    analysis). Returns operation state, progress percentage, and any error information.

    Args:
        op_id (str): Unique identifier for the operation

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, PydanticGetOperationResponse]]
    """

    kwargs = _get_kwargs(
        op_id=op_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    op_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, HTTPValidationError, PydanticGetOperationResponse]]:
    """Get operation status

     Retrieve the current status and progress of a background operation (e.g., audio processing, AI
    analysis). Returns operation state, progress percentage, and any error information.

    Args:
        op_id (str): Unique identifier for the operation

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, PydanticGetOperationResponse]
    """

    return (
        await asyncio_detailed(
            op_id=op_id,
            client=client,
        )
    ).parsed
