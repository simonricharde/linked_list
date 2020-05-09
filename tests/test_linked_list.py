from linked_list import __version__
from linked_list.linked_list import LinkedList, Node
import pytest

def test_version():
	assert __version__ == '0.1.0'

def test_error_linked_list():

    with pytest.raises(TypeError):
        LinkedList("?")

def test_error_node():
    
    with pytest.raises(TypeError):
        Node("?", "?", "?")

def test_error_missing_arguments_nodes():
    
    with pytest.raises(TypeError):
        Node()
	
def test_linked_list_creation():
	empty_list = LinkedList()
	assert empty_list.head == None

@pytest.fixture
def build_cars():
    cars = LinkedList()
    cars.insert("Ferrari")
    cars.insert("BMW")
    cars.insert("Lexus")
    return cars

def test_node_value():
    car= Node("Ferrari")
    assert car.value == "Ferrari"
    

def test_node_next_value():
    car= Node("Ferrari")
    assert car.next == None

def test_node_next_multiple_values():
	cars = LinkedList()
	cars.insert("Ferrari")
	cars.insert("BMW")
	assert cars.head.value == "BMW"
	assert cars.head.next.value == "Ferrari"	
	

def test_head_values(build_cars):
	
	assert build_cars.head.value == "Lexus"
	assert build_cars.head.next.value == "BMW"
	assert build_cars.head.next.next.value == "Ferrari"


def test_includes(build_cars):
	
	assert build_cars.includes("BMW") 
	

def test_not_includes(build_cars):
	
	assert build_cars.includes("Audi")  == False

def test_linked_list_str(build_cars):
    assert '{ Lexus } -> { BMW } -> { Ferrari } -> None' == build_cars.__str__()

def test_empty_linked_list_str():
    empty_list = LinkedList()
    assert 'None' == empty_list.__str__()
	