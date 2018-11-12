# coding: utf-8
import random
import hashlib
import xmltodict

def sorted_str(params, key, null=False):
    """ key按照ASCII排序 """
    if null:
        s = '&'.join((str(k) + '=' + str(params[k])) for k in sorted(params))
    else:
        s = '&'.join((str(k) + '=' + str(params[k])) for k in sorted(params) if params[k])

    return s + '&key={}'.format(key)


def sign_md5(s, upper=True):
    """ md5 """
    if upper:
        return hashlib.md5(s.encode("utf-8")).hexdigest().upper()
    else:
        return hashlib.md5(s.encode("utf-8")).hexdigest()


def to_xml(params, cdata=True, encoding='utf-8'):
    """ dict转xml """
    tag = '<{0}><![CDATA[{1}]]></{0}>' if cdata else '<{0}>{1}</{0}>'
    s = ''.join(tag.format(k, v) for k, v in params.items())
    return '<xml>{}</xml>'.format(s).encode(encoding)


def to_dict(content):
    """ xml转dict """
    data = xmltodict.parse(content).get('xml')
    if '#text' in data:
        del data['#text']
    return data


def random_str(length, upper=True):
    """ 随机字符串 """
    sample = 'abcdefghijklmnopqrstuvwxyz'
    sample += sample.upper()
    sample += '1234567890'
    result = ''.join(random.sample(sample, length))
    return result.upper() if upper else result

