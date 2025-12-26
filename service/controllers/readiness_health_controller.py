from service.soap_client.wsfe import wsfe_dummy
from service.time.time_management import request_ntp_for_readiness
from service.utils.convert_to_dict import convert_zeep_object_to_dict
from service.utils.logger import logger


async def readiness_health_check() -> dict:
    logger.debug("Starting readiness health check")
    ntp = ""

    ntp_status = request_ntp_for_readiness()
    if ntp_status:
        ntp = "OK"
        logger.debug("NTP readiness check OK")

    else:
        ntp = {
            "status": "error",
            "message": "NTP query failed",
            "server": "time.afip.gov.ar"
        }
        logger.warning("NTP readiness check FAILED")

    # Check WSFE 
    wsfe_health_info = await wsfe_dummy()
    wsfe_health_info_parsed = convert_zeep_object_to_dict(wsfe_health_info)
    logger.debug("WSFE dummy check OK")

    logger.debug("Readiness health check finished")
    return {
        "ntp" : ntp,
        "wsfe_health" : wsfe_health_info_parsed
        }