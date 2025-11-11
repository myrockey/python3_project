#!/usr/bin/python3

import hashlib

def hash_encode(str,type):
    hash = hashlib.new(type)
    hash.update(str)
    return hash.hexdigest()

print(hash_encode(b'RUNOOB','sha256'))
print(hash_encode(b'RUNOOB','md5'))

def hash_sha256(str):
    hash = hashlib.sha256(str)
    return hash.hexdigest()

print(hash_sha256(b'RUNOOB'))

def hash_md5(str):
    hash = hashlib.md5(str)
    return hash.hexdigest()

print(hash_md5(b'RUNOOB'))

# hexdigest(): 获取十六进制表示的哈希值
# digest(): 获取二进制表示的哈希值。
def hash_encode_data(str,type,returnType = 16):
    hash = hashlib.new(type)
    hash.update(str)
    if(returnType == 2):
        return hash.digest()
    return hash.hexdigest()

print(hash_encode_data(b'RUNOOB','sha256',2))
print(hash_encode_data(b'RUNOOB','md5',2))
    
def hash_encode_data(str,type,returnType = 16):
    hash = hashlib.new(type)
    hash.update(str.encode()) # str.encode 字符串转2进制， b'hello' == 'hello'.encode()
    if(returnType == 2):
        return hash.digest()
    return hash.hexdigest()

print(hash_encode_data('RUNOOB','sha256',2))
print(hash_encode_data('RUNOOB','md5',2))


print(hash_encode_data('RUNOOB','sha512'))

def hash_sha512(str):
    hash = hashlib.sha512(str.encode())
    return hash.hexdigest()

print(hash_sha512('RUNOOB'))


'''
输出：
673dc967d03201db7fe47b7eabd56c47ca5bc694222de303106a5504e5d0daa8
18fa661e2a4a7dd6471cc1407290cf6e
673dc967d03201db7fe47b7eabd56c47ca5bc694222de303106a5504e5d0daa8
18fa661e2a4a7dd6471cc1407290cf6e
b'g=\xc9g\xd02\x01\xdb\x7f\xe4{~\xab\xd5lG\xca[\xc6\x94"-\xe3\x03\x10jU\x04\xe5\xd0\xda\xa8'
b'\x18\xfaf\x1e*J}\xd6G\x1c\xc1@r\x90\xcfn'
b'g=\xc9g\xd02\x01\xdb\x7f\xe4{~\xab\xd5lG\xca[\xc6\x94"-\xe3\x03\x10jU\x04\xe5\xd0\xda\xa8'
b'\x18\xfaf\x1e*J}\xd6G\x1c\xc1@r\x90\xcfn'
7cfe50493eebd48ee7330c797459c2d0d5ca943bd1c84ad7a0b6783b11cd49d06b4a1dc84ee9ea5e20d0bfedbdb67e716500a20e5870abecea3f32dc8484a811
7cfe50493eebd48ee7330c797459c2d0d5ca943bd1c84ad7a0b6783b11cd49d06b4a1dc84ee9ea5e20d0bfedbdb67e716500a20e5870abecea3f32dc8484a811
'''