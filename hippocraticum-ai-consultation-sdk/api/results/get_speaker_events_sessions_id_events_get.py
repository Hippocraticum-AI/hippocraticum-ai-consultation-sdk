from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    use_language_translate: Union[None, Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_use_language_translate: Union[None, Unset, bool]
    if isinstance(use_language_translate, Unset):
        json_use_language_translate = UNSET
    else:
        json_use_language_translate = use_language_translate
    params["use_language_translate"] = json_use_language_translate

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/sessions/{id}/events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Union[Any, HTTPValidationError]]:
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
    use_language_translate: Union[None, Unset, bool] = False,
) -> Response[Union[Any, HTTPValidationError]]:
    """Get consultation events

     Retrieve structured events extracted from the consultation. Events include medical findings, patient
    statements, and doctor observations with timestamps.

    Args:
        id (str): Unique identifier for the consultation session
        use_language_translate (Union[None, Unset, bool]): Whether to translate events using
            consultation's default language Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        id=id,
        use_language_translate=use_language_translate,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    use_language_translate: Union[None, Unset, bool] = False,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Get consultation events

     Retrieve structured events extracted from the consultation. Events include medical findings, patient
    statements, and doctor observations with timestamps.

    Args:
        id (str): Unique identifier for the consultation session
        use_language_translate (Union[None, Unset, bool]): Whether to translate events using
            consultation's default language Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        id=id,
        client=client,
        use_language_translate=use_language_translate,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    use_language_translate: Union[None, Unset, bool] = False,
) -> Response[Union[Any, HTTPValidationError]]:
    """Get consultation events

     Retrieve structured events extracted from the consultation. Events include medical findings, patient
    statements, and doctor observations with timestamps.

    Args:
        id (str): Unique identifier for the consultation session
        use_language_translate (Union[None, Unset, bool]): Whether to translate events using
            consultation's default language Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        id=id,
        use_language_translate=use_language_translate,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    use_language_translate: Union[None, Unset, bool] = False,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Get consultation events

     Retrieve structured events extracted from the consultation. Events include medical findings, patient
    statements, and doctor observations with timestamps.

    Args:
        id (str): Unique identifier for the consultation session
        use_language_translate (Union[None, Unset, bool]): Whether to translate events using
            consultation's default language Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            use_language_translate=use_language_translate,
        )
    ).parsed
