import json

from strelka import strelka


class ScanManifest(strelka.Scanner):
    """Parses browser extension's  manifest.json."""

    def scan(self, data, file, options, expire_at):
        try:
            jsondata = json.loads(data)
            required_keys = ["name", "manifest_version", "version"]
            optional_keys = [
                "content_scripts",
                "content_security_policy",
                "description",
                "permissions",
                "update_url",
                "key",
            ]
            for key in required_keys:
                self.event[key] = jsondata[key]
            for key in optional_keys:
                if jsondata.get(key):
                    self.event[key] = jsondata[key]
        except strelka.ScannerTimeout:
            raise
        except Exception:
            self.flags.append("error parsing manifest")
            return
