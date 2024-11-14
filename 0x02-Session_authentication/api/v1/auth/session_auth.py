#!/usr/bin/env python3
"""
SessionAuth
"""
from api.v1.auth.auth import Auth
from typing import TypeVar
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """
    session authentication class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        creates a Session ID for a user_id
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        SessionAuth.user_id_by_session_id[user_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        returns a User ID based on Session ID
        """
        if not session_id or type(session_id) != str:
            return None
        return SessionAuth.user_id_by_session_id.get(session_id, None)

    def current_user(self, request=None):
        """
        return: user instance based on a cookie value
        """
        session_cookie = self.session_cookie(request)
        if session_cookie is None:
            return None
        user_id = self.user_id_for_session_id(session_cookie)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """
        destroy active user session
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if not session_id:
            return False
        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return False
        del self.user_id_by_session_id[session_id]
        return True
