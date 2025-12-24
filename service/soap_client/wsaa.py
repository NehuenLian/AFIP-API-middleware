import logging
from builtins import ConnectionResetError
from typing import Optional

from requests.exceptions import (  # Zeep uses requests behind it.
    ConnectionError, Timeout)
from tenacity import (before_sleep_log, retry, retry_if_exception_type,
                      stop_after_attempt, wait_fixed)
from zeep import Client
from zeep.exceptions import Fault, TransportError, XMLSyntaxError

from service.soap_client.format_error import build_error_response
from service.soap_client.wsdl.wsdl_manager import get_wsaa_wsdl
from service.utils.logger import logger

afip_wsdl = get_wsaa_wsdl()

# Implement retries with tenacity only for these Exceptions.
@retry(
        retry=retry_if_exception_type(( ConnectionResetError, ConnectionError, TransportError )),
        stop=stop_after_attempt(3),
        wait=wait_fixed(0.5),
        before_sleep=before_sleep_log(logger, logging.WARNING),
    )
def login_cms(b64_cms: str) -> dict:

    logger.info("Starting CMS login request to AFIP")
    METHOD = "loginCms"

    try:
        client = Client(wsdl=afip_wsdl)
        login_ticket_response = client.service.loginCms(b64_cms)
        logger.info("CMS login request to AFIP ended successfully.")

        logger.debug(f"login_ticket_response: {login_ticket_response}")
        return {
                "status" : "success",
                "response" : login_ticket_response
                }
    
    except (ConnectionError, Timeout) as e:
        return build_error_response(METHOD, "Network error", str(e))
    
    except TransportError as e:
        return build_error_response(METHOD, "HTTP Error", str(e))

    except Fault as e:
        # SOAP Faults indicate that the request could not be processed by the service, 
        # often due to invalid input, datatype mismatches, or business rule violations. 
        # These errors are the caller's responsibility to handle.

        logger.debug(f"SOAP FAULT in login_cms: {e}")
        return build_error_response(METHOD, "SoapFault", str(e))
    
    except XMLSyntaxError as e:
        return build_error_response(METHOD, "Invalid AFIP response", str(e))

    except Exception as e:
        logger.error(f"General exception in login_cms: {e}")
        return build_error_response(METHOD, "unknown", str(e))