from cipher_ln2444 import __version__
from cipher_ln2444 import cipher_ln2444

def test_version():
    assert __version__ == '0.1.0'
    
import pytest

def test_cipher():
    example = 'hello'
    shift = 2
    expected = 'jgnnq'
    actual = cipher_ln2444.cipher(example, shift)
    assert actual == expected