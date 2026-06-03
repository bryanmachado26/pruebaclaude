import pytest
from calculadora import sumar, restar, multiplicar, dividir


def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0


def test_restar():
    assert restar(5, 3) == 2
    assert restar(0, 5) == -5
    assert restar(-2, -2) == 0


def test_multiplicar():
    assert multiplicar(3, 4) == 12
    assert multiplicar(-2, 3) == -6
    assert multiplicar(0, 100) == 0


def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(7, 2) == 3.5
    assert dividir(-6, 3) == -2


def test_dividir_entre_cero():
    with pytest.raises(ValueError, match="No se puede dividir entre cero"):
        dividir(5, 0)
