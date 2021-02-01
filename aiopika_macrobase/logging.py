from contextvars import ContextVar
from logging import Logger
from uuid import uuid4

from structlog import get_logger as get_struct_logger, configure
from structlog._config import _BUILTIN_DEFAULT_PROCESSORS, _CONFIG

_cross_request_id = ContextVar('cross_request_id', default=None)

__all__ = ['get_request_id', 'set_request_id', 'configure_logger', 'get_logger']


def get_request_id() -> str:
    """
    get cross request id. generate and return if not set
    """
    req_id = _cross_request_id.get()

    if not req_id:
        req_id = str(uuid4())
        _cross_request_id.set(req_id)

    return req_id


def set_request_id(request_id: str = None):
    """
    set cross request id
    """
    if not request_id:
        request_id = str(uuid4())

    _cross_request_id.set(request_id)


def _cross_request_processor(logger, log_method, event_dict: dict) -> dict:
    event_dict['crossRequestId'] = get_request_id()
    return event_dict


def configure_logger():
    """
    configure structlog, add crossRequestId
    """
    if not _CONFIG.is_configured:
        configure(processors=[_cross_request_processor, *_BUILTIN_DEFAULT_PROCESSORS])


def get_logger(*args, **kwargs) -> Logger:
    configure_logger()
    return get_struct_logger(*args, **kwargs)
