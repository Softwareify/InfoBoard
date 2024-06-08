import os
import socket

import requests


class VarnishService:
    """Varnish service."""

    VARNISH_ADDRESS = os.getenv("VARNISH_ADDRESS", "varnish")
    VARNISH_PORT = os.getenv("VARNISH_PORT", "80")
    VARNISH_PROTO = os.getenv("VARNISH_PROTO", "http")

    def __init__(self):
        self.varnish_ip_list = self._get_varnish_ip_list()

    def slice_domain_suffix(self, *, domain: str) -> str:
        """
        Get domain without suffix.

        :param domain: domain address

        :return: clear domain
        """
        split_string = ".infosite-redesign."
        if split_string in domain:
            return domain.split(split_string)[0]

        return domain

    def _get_varnish_ip_list(self):
        """Get all varnishes ips."""
        try:
            varnish_ip_list = socket.gethostbyname_ex(self.VARNISH_ADDRESS)[2]
            print("Varnish addresses retrieved: " + str(varnish_ip_list))
            return varnish_ip_list
        except Exception as exception:  # noqa
            print("Could not get varnishes ips: %s", exception)
            return []

    def send_request(self, *, http_method: str, headers: dict) -> None:
        """
        Send request to varnish instance.

        :param http_method: specific varnish http method
        :param headers: payload

        """
        for varnish_ip in self.varnish_ip_list:
            try:
                request = requests.request(
                    http_method, f"{self.VARNISH_PROTO}://{varnish_ip}:{self.VARNISH_PORT}", headers=headers, timeout=5
                )
                if request.status_code == 200:
                    print("Varnish %s cache cleared - %s.", varnish_ip, headers)
                elif request.status_code == 403:
                    print(
                        "Could not clear cache for %s. Check acl purge varnish configuration.", varnish_ip
                    )
                else:
                    print("Could not clear cache for %s. Status code: %s.", varnish_ip, request.status_code)
            except Exception as exception:  # noqa
                print("Could not clear cache for %s. Exception: %s.", varnish_ip, exception)

    def purge_both(self, *, domain: str, path: str) -> None:
        """
        Clear cache for domain and slug.

        :param domain: domain address
        :param path: slug

        """
        domain = self.slice_domain_suffix(domain=domain)
        headers = {"X-Purge-Domain": domain, "X-Purge-Path": path}
        self.send_request(http_method="PURGEBOTH", headers=headers)

    def purge_path(self, *, path: str) -> None:
        """
        Clear cache for path file

        :param path: path file
        """
        headers = {"X-Purge-Path": path}
        self.send_request(http_method="PURGEPATH", headers=headers)
