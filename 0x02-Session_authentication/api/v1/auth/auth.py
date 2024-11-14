#!/usr/bin/env python3
"""
Auth class
"""
from tabnanny import check
from flask import request
from os import getenv
from typing import List, TypeVar
User = TypeVar('User')


class Auth:
    """
    a class to manage API authenticaation
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        this function returns False - path and exclude_paths
        """
        check = path
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != "/":
            check += "/"
        if check in excluded_paths or path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        returns None - request
        """
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> User:
        """
        returns None - request
        """
        return None

    def session_cookie(self, request=None):
        """
        returns a cookie value from a request
        """
        if request is None:
            return None
        session_name = getenv("SESSION_NAME")
        return request.cookies.get(session_name, None)
