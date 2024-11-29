const myList = document.querySelector('.my_list');
const addItem = document.querySelector('#add_item');
addItem.addEventListener('click', function() {
    const newList = document.createElement('li');
    newList.textContent = 'Item';
    myList.appendChild(newList);
});