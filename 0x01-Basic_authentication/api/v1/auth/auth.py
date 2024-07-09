#!/usr/bin/env python3
"""
Auth class
"""
from flask import request
from typing import TypeVar, List
User = TypeVar('User')


class Auth:
    """
    class: Auth
    """
    def __init__(self) -> None:
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        """
        check = path
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != "/":
            check += "/"
        if check in excluded_paths or path in excluded_paths:
            return False
        return True

    def authorization_header(self, request: None) -> str:
        """
        """
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar:
        """
        """
        if request is None:
            return None
