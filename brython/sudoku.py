import browser as br
import random


my_div = br.document['sudoku-board']
for i in range(9):
    box = br.html.DIV(id=f'sudoku-box-{i}')
    box.class_name = 'sudoku-box'
    for j in range(9):
        cell = br.html.DIV(id=f'sudoku-cell-{i * 9 + j}')
        cell.class_name = 'sudoku-cell'
        cell <= (cell_num := br.html.P())
        if random.random() > .8:
            cell_num.textContent = random.randint(1, 9)
        box <= cell
    my_div <= box


@br.bind('#echo', 'click')
def my_click(ev):
    pass
