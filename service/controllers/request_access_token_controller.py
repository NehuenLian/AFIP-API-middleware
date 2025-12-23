from service.crypto.sign import get_binary_cms, sign_login_ticket_request
from service.soap_client.wsaa import login_cms
from service.utils.logger import logger
from service.xml_management.xml_builder import (
    build_login_ticket_request, parse_and_save_loginticketresponse, save_xml)


def generate_token_from_scratch() -> None:

    root = build_login_ticket_request()
    save_xml(root, "loginTicketRequest.xml")
    sign_login_ticket_request()
    b64_cms = get_binary_cms()
    login_ticket_response = login_cms(b64_cms)

    if login_ticket_response["status"] == "success":
        parse_and_save_loginticketresponse(login_ticket_response["response"])
        logger.info("Token generated.")

def generate_token_from_existing() -> None:

    logger.info("Token still valid. Generating loginTicketResponse without signing or creating new loginTicketRequest.")
    b64_cms = get_binary_cms()
    login_ticket_response = login_cms(b64_cms)

    if login_ticket_response["status"] == "success":
        parse_and_save_loginticketresponse(login_ticket_response["response"])
        logger.info("Token generated.")