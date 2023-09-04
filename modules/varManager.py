import secrets
import base64


class varManager:
    vars = {
        "TRIGGER": {}
    }
    key = secrets.token_hex(16)

    @staticmethod
    def encrypt(data):
        keyBytes = bytes.fromhex(varManager.key)
        dataString = str(data)
        dataBytes = dataString.encode('utf-8')
        encryptedBytes = bytes(c ^ keyBytes[i % len(keyBytes)] for i, c in enumerate(dataBytes))
        encryptedData = base64.b64encode(encryptedBytes).decode('utf-8')
        return encryptedData

    @staticmethod
    def decrypt(encryptedData):
        keyBytes = bytes.fromhex(varManager.key)
        encryptedBytes = base64.b64decode(encryptedData)
        decryptedBytes = bytes(c ^ keyBytes[i % len(keyBytes)] for i, c in enumerate(encryptedBytes))
        decryptedData = decryptedBytes.decode('utf-8')
        return decryptedData

    @staticmethod
    def setVar(name, value, section=None):
        encrypted_value = varManager.encrypt(value)
        if section:
            varManager.vars[section][name] = encrypted_value
        else:
            varManager.vars[name] = encrypted_value

    @staticmethod
    def getVar(name, section=None):
        if section:
            encryptedValue = varManager.vars.get(section, {}).get(name)
        else:
            encryptedValue = varManager.vars.get(name)

        if encryptedValue is not None:
            return varManager.decrypt(encryptedValue)
        else:
            return None

    @staticmethod
    def getAllVars():
        decryptedVars = {}
        for name, encryptedValue in varManager.vars.items():
            if name == "GENERAL":
                continue
            if isinstance(encryptedValue, dict):
                decryptedVars[name] = {key: varManager.decrypt(value) if isinstance(value, str) else value for
                                       key, value in encryptedValue.items()}
            else:
                decryptedVars[name] = varManager.decrypt(encryptedValue) if isinstance(encryptedValue,
                                                                                       str) else encryptedValue
        return decryptedVars

    @staticmethod
    def delVar(name, section):
        if name in varManager.vars:
            if section:
                del varManager.vars[section][name]
            else:
                del varManager.vars[name]
