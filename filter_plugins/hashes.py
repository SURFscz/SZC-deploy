import hashlib
import base64


# hashing filters
class FilterModule(object):

    # generate a base64-encoded sha1 hash, as 'slappasswd -h {SHA}' gives
    @staticmethod
    def _sha1_b64(str):
        m = hashlib.sha1()
        m.update(str.encode('ASCII'))
        hash_bin = m.digest()
        hash_b64 = base64.b64encode(hash_bin)
        return hash_b64.decode('ASCII')

    # generate a MySQL-type password hash
    # see https://unix.stackexchange.com/questions/44883/encrypt-a-password-the-same-way-mysql-does
    @staticmethod
    def _sha1_mysql(str):
        str2 = str.encode('ASCII')
        res = hashlib.sha1(hashlib.sha1(str2).digest()).hexdigest()
        return '*' + res.upper()

    def filters(self):
        return {
            'sha1_b64':   self._sha1_b64,
            'slapd_hash': lambda a: '{SHA}' + self._sha1_b64(a),
            'mysql_hash': self._sha1_mysql,
        }
