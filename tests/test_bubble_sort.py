import pytest
from src.bubble_sort.bubble_sort import bubble_sort

# Happy Path Testing
@pytest.mark.parametrize('lista',[
    ([1,4,3,8,7]),
    ([5,7,2,3,6,3,2,89,8,3,2,6,12]),
    ([43264,786856123123,78987,23234,9087,33242]), 
    ([-5,-10,22,-4,123]),   
    ([1.111,-1.111,0,12])
])
def test_bubble_sort_good_values_with_changes(lista):
    assert bubble_sort(lista)[0] == sorted(lista)

@pytest.mark.parametrize('lista_posortowana', [
    ([0,1,2,3,4,5,6,7]),
    ([-10,-9,-8,-7,-6]),
    ([1,1,1,1,1,1,1,1]),
    ([1.111,1.112,1.113])
])
def test_bubble_sort_good_values_without_changes(lista_posortowana):
    wynik, ilosc_iteracji = bubble_sort(lista_posortowana)
    assert (wynik, ilosc_iteracji) == (sorted(lista_posortowana),0)

# Sad Path Testing
@pytest.mark.parametrize('lista',[
    (['a','b','c','a']),
    (['123','12','13','-1','30']),
    ([(12,34),'123',43,"abc", None]),
    ({'a':12, 'b': 45, 'c':[1,3,5]}),
])
def test_bubble_sort_wrong_types(lista):
    with pytest.raises(TypeError) as exc_info:
        bubble_sort(lista)
    assert exc_info.value.args[0] == "Provied list contains corrupted values!"

@pytest.mark.parametrize('lista',[
    (123.15),
    (123),
    (0),
])
def test_bubble_sort_one_value(lista):
    with pytest.raises(Exception) as exc_info:
        bubble_sort(lista)
    assert "object is not iterable" in exc_info.value.args[0]  


@pytest.mark.parametrize('lista',[
    ({'a':15}),
    ('ABC'),
    (lambda x: 123),
    (int),
    (None),
])
def test_bubble_sort_not_a_list_type(lista):
    with pytest.raises(Exception) as exc_info:
        raise Exception('Provied list contains corrupted values!')
    assert exc_info.value.args[0] == 'Provied list contains corrupted values!'
