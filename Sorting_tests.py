import pytest

from Rytis_Parnarauskas_kursinis import Sort, BubbleSort, MergeSort, QuickSort, BogoSort, HeapSort

@pytest.fixture
def sample_list():
    return [-5, 1, 3, 9, 0, 15, -100]

@pytest.fixture
def empty_list():
    return []

@pytest.fixture
def single_element_list():
    return [42]

@pytest.fixture
def duplicate_list():
    return [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

@pytest.fixture
def sorted_list():
    return [1, 2, 3, 4, 5]

@pytest.fixture
def reverse_sorted_list():
    return [5, 4, 3, 2, 1]

def test_bubble_sort(sample_list):
    bubble_sort = BubbleSort(sample_list)
    sorted_result = bubble_sort.get_sorted_list
    assert sorted_result == sorted(sample_list)
    assert bubble_sort.isSorted

def test_merge_sort(sample_list):
    merge_sort = MergeSort(sample_list)
    sorted_result = merge_sort.get_sorted_list
    assert sorted_result == sorted(sample_list)
    assert merge_sort.isSorted

def test_quick_sort(sample_list):
    quick_sort = QuickSort(sample_list)
    sorted_result = quick_sort.get_sorted_list
    assert sorted_result == sorted(sample_list)
    assert quick_sort.isSorted

def test_heap_sort(sample_list):
    heap_sort = HeapSort(sample_list)
    sorted_result = heap_sort.get_sorted_list
    assert sorted_result == sorted(sample_list)
    assert heap_sort.isSorted

def test_bogo_sort_small_list():
    small_list = [3, 1, 4, 1, 5]
    bogo_sort = BogoSort(small_list)
    sorted_result = bogo_sort.get_sorted_list
    assert sorted_result == sorted(small_list)
    assert bogo_sort.isSorted

def test_base_sort(sample_list):
    base_sort = Sort(sample_list)
    sorted_result = base_sort.get_sorted_list
    assert sorted_result == sorted(sample_list)
    assert base_sort.isSorted

def test_empty_list():
    with pytest.raises(ValueError):
        Sort([])

def test_single_element():
    single_sort = Sort([42])
    sorted_result = single_sort.get_sorted_list
    assert sorted_result == [42]
    assert single_sort.isSorted

def test_duplicates(duplicate_list):
    bubble_sort = BubbleSort(duplicate_list.copy())
    sorted_result = bubble_sort.get_sorted_list
    assert sorted_result == sorted(duplicate_list)
    assert bubble_sort.isSorted

    merge_sort = MergeSort(duplicate_list.copy())
    sorted_result = merge_sort.get_sorted_list
    assert sorted_result == sorted(duplicate_list)
    assert merge_sort.isSorted

    quick_sort = QuickSort(duplicate_list.copy())
    sorted_result = quick_sort.get_sorted_list
    assert sorted_result == sorted(duplicate_list)
    assert quick_sort.isSorted

    heap_sort = HeapSort(duplicate_list.copy())
    sorted_result = heap_sort.get_sorted_list
    assert sorted_result == sorted(duplicate_list)
    assert heap_sort.isSorted

def test_already_sorted(sorted_list):
    bubble_sort = BubbleSort(sorted_list.copy())
    sorted_result = bubble_sort.get_sorted_list
    assert sorted_result == sorted_list
    assert bubble_sort.isSorted

def test_reverse_sorted(reverse_sorted_list):
    quick_sort = QuickSort(reverse_sorted_list.copy())
    sorted_result = quick_sort.get_sorted_list
    assert sorted_result == sorted(reverse_sorted_list)
    assert quick_sort.isSorted